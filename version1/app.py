
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from google import genai

from game_prompt import GAME_PROMPT


# ---------------------------------
# 1. Load Gemini configuration
# ---------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL")

if not API_KEY:
    st.error("GEMINI_API_KEY is missing from .env")
    st.stop()

if not MODEL_NAME:
    st.error("GEMINI_MODEL is missing from .env")
    st.stop()

client = genai.Client(api_key=API_KEY)


# ---------------------------------
# 2. Streamlit interface
# ---------------------------------

st.title("🔐 AI Escape Room")
st.subheader("Version 1 - The Locked Library")
st.write("Welcome to the AI Escape Room!")

st.success("Gemini client initialized successfully!")
st.caption(f"Configured model: {MODEL_NAME}")

st.divider()
st.subheader("🎮 Play the Escape Room")


# ---------------------------------
# 3. Opening scene
# ---------------------------------

OPENING_SCENE = """
You awaken inside an ancient library.
Rain taps against the windows, and the
heavy wooden exit door is locked.

Around you are towering bookshelves,
an old wooden desk with a locked drawer,
a mysterious painting, and a grandfather clock.

What would you like to investigate first?
"""


# ---------------------------------
# 4. Initialize conversation memory
# ---------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": OPENING_SCENE
        }
    ]


# ---------------------------------
# 5. Restart game
# ---------------------------------

if st.button("🔄 Restart Game"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": OPENING_SCENE
        }
    ]
    st.rerun()


# ---------------------------------
# 6. Display conversation history
# ---------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# ---------------------------------
# 7. Player input
# ---------------------------------

player_input = st.chat_input(
    "What would you like to do?"
)


if player_input:

    # Save the player's message
    st.session_state.messages.append({
        "role": "user",
        "content": player_input
    })

    # Display player's message
    with st.chat_message("user"):
        st.write(player_input)

    # ---------------------------------
    # 8. Prepare Gemini conversation
    # ---------------------------------

    conversation = []

    for message in st.session_state.messages:
        conversation.append({
            "role": (
                "user"
                if message["role"] == "user"
                else "model"
            ),
            "parts": [
                {"text": message["content"]}
            ]
        })

    # ---------------------------------
    # 9. Generate Gemini response
    # ---------------------------------

    with st.chat_message("assistant"):
        with st.spinner("The Game Master is thinking..."):

            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=conversation,
                    config={
                        "system_instruction": GAME_PROMPT
                    }
                )

                ai_reply = response.text

                if not ai_reply:
                    raise ValueError(
                        "Gemini returned an empty response."
                    )

                # -------------------------
                # 10. Escape detection
                # -------------------------

                if "ESCAPE_SUCCESS" in ai_reply:

                    clean_reply = ai_reply.replace(
                        "ESCAPE_SUCCESS", ""
                    ).strip()

                    st.write(clean_reply)

                    st.success(
                        "🎉 Congratulations! "
                        "You escaped The Locked Library!"
                    )

                    st.balloons()

                else:
                    clean_reply = ai_reply
                    st.write(clean_reply)

                # -------------------------
                # 11. Save Gemini response
                # -------------------------

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": clean_reply
                })

            except Exception as e:
                st.error(
                    f"Gemini request failed: {e}"
                )
