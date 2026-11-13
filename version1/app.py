
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from google import genai

from game_prompt import GAME_PROMPT


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Escape Room - Version 1",
    page_icon="🔐",
    layout="wide"
)


# ============================================================
# 2. LOAD GEMINI CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL")

if API_KEY and MODEL_NAME:
    client = genai.Client(api_key=API_KEY)
else:
    client = None


# ============================================================
# 3. SIMPLE GAME INTERFACE
# ============================================================

st.markdown("""
<style>
.stApp {
    background-color: #17202a;
    color: white;
}

h1, h2, h3 {
    color: #f5c76a !important;
}

div.stButton > button {
    background-color: #34495e;
    color: white;
    border: 1px solid #d4ac6e;
    border-radius: 8px;
    min-height: 55px;
}

div.stButton > button:hover {
    background-color: #566573;
    color: white;
}

.room-box {
    padding: 20px;
    background-color: #273746;
    border: 2px solid #d4ac6e;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    margin-bottom: 20px;
}

.object-card {
    background-color: #273746;
    border: 1px solid #d4ac6e;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 40px;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# 4. INITIAL GAME STATE
# ============================================================

OPENING_SCENE = """
You awaken inside an ancient library.

Rain taps against the windows.
The heavy wooden exit door is locked.

Around you are bookshelves, a wooden desk,
a mysterious painting, and a grandfather clock.

Explore the room and find a way to escape.
"""


def new_game():
    return {
        "bookshelf_solved": False,
        "drawer_open": False,
        "key_collected": False,
        "clock_solved": False,
        "escaped": False,
    }


if "v1_game" not in st.session_state:
    st.session_state.v1_game = new_game()

if "v1_messages" not in st.session_state:
    st.session_state.v1_messages = [
        {
            "role": "assistant",
            "content": OPENING_SCENE
        }
    ]

if "v1_selected" not in st.session_state:
    st.session_state.v1_selected = "Room"

if "v1_victory_shown" not in st.session_state:
    st.session_state.v1_victory_shown = False


game = st.session_state.v1_game


# ============================================================
# 5. RESTART GAME
# ============================================================

def restart_game():

    st.session_state.v1_game = new_game()

    st.session_state.v1_messages = [
        {
            "role": "assistant",
            "content": OPENING_SCENE
        }
    ]

    st.session_state.v1_selected = "Room"
    st.session_state.v1_victory_shown = False

    for key in [
        "v1_bookshelf_code",
        "v1_drawer_code",
        "v1_exit_code",
    ]:
        st.session_state.pop(key, None)


def select_object(name):
    st.session_state.v1_selected = name


# ============================================================
# 6. TITLE AND SIDEBAR
# ============================================================

st.title("🔐 AI Escape Room")

st.subheader("Version 1 — The Locked Library")

st.write(
    "An interactive escape room powered by "
    "Python, Streamlit, and Google Gemini."
)

with st.sidebar:

    st.header("🎒 Player Inventory")

    if game["key_collected"]:
        st.success("🗝️ Brass Key")
    else:
        st.info("Inventory is empty.")

    st.divider()

    st.header("📊 Game Progress")

    completed = sum([
        game["bookshelf_solved"],
        game["drawer_open"],
        game["clock_solved"],
        game["escaped"],
    ])

    st.progress(completed / 4)

    st.write(f"{completed} of 4 puzzles completed")

    st.divider()

    if st.button(
        "🔄 Restart Game",
        use_container_width=True
    ):
        restart_game()
        st.rerun()


# ============================================================
# 7. LIBRARY ROOM
# ============================================================

st.divider()

st.header("🏛️ Explore the Library")

st.markdown("""
<div class="room-box">
<h2>🏛️ THE LOCKED LIBRARY</h2>
<p>
You stand inside an old mysterious library.
Four objects may help you escape.
</p>
<p>
📚 Bookshelf &nbsp;&nbsp;
🗄️ Desk &nbsp;&nbsp;
🕰️ Clock &nbsp;&nbsp;
🚪 Exit Door
</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# 8. INTERACTIVE OBJECT BUTTONS
# ============================================================

columns = st.columns(4)

objects = [
    ("📚 Bookshelf", "Bookshelf"),
    ("🗄️ Desk Drawer", "Drawer"),
    ("🕰️ Clock", "Clock"),
    ("🚪 Exit Door", "Door"),
]

for column, (label, object_name) in zip(
    columns,
    objects
):
    with column:

        st.button(
            label,
            key=f"v1_object_{object_name}",
            use_container_width=True,
            on_click=select_object,
            args=(object_name,)
        )

st.button(
    "↩ Return to Room",
    on_click=select_object,
    args=("Room",)
)


# ============================================================
# 9. INTERACTIVE PUZZLES
# ============================================================

st.divider()

selected = st.session_state.v1_selected


# ------------------------------------------------------------
# MAIN ROOM
# ------------------------------------------------------------

if selected == "Room":

    st.subheader("🏛️ Main Library")

    st.write(
        "The library contains four mysterious objects. "
        "Click an object above to investigate."
    )


# ------------------------------------------------------------
# BOOKSHELF
# ------------------------------------------------------------

elif selected == "Bookshelf":

    st.subheader("📚 Mysterious Bookshelf")

    st.write(
        "Four books have numbers written on their spines."
    )

    st.markdown("""
    📕 Book 1 — **4**

    📗 Book 2 — **2**

    📘 Book 3 — **7**

    📙 Book 4 — **1**
    """)

    if game["bookshelf_solved"]:

        st.success(
            "The bookshelf puzzle is solved!"
        )

    else:

        with st.form("v1_bookshelf_form"):

            code = st.text_input(
                "Enter the four-digit code",
                max_chars=4,
                key="v1_bookshelf_code"
            )

            submitted = st.form_submit_button(
                "Solve Puzzle"
            )

            if submitted:

                if code.strip() == "4271":

                    game["bookshelf_solved"] = True

                    st.success(
                        "Correct! You solved the bookshelf."
                    )

                    st.rerun()

                else:

                    st.error(
                        "Incorrect code. Try again."
                    )


# ------------------------------------------------------------
# DESK DRAWER
# ------------------------------------------------------------

elif selected == "Drawer":

    st.subheader("🗄️ Wooden Desk Drawer")

    st.write(
        "A wooden desk contains a locked drawer."
    )

    if not game["bookshelf_solved"]:

        st.warning(
            "The drawer is locked. "
            "Solve the bookshelf puzzle first."
        )

    elif not game["drawer_open"]:

        with st.form("v1_drawer_form"):

            code = st.text_input(
                "Enter the drawer code",
                max_chars=4,
                key="v1_drawer_code"
            )

            submitted = st.form_submit_button(
                "Open Drawer"
            )

            if submitted:

                if code.strip() == "4271":

                    game["drawer_open"] = True

                    st.rerun()

                else:

                    st.error(
                        "Incorrect combination."
                    )

    else:

        st.success(
            "The drawer is open!"
        )

        if not game["key_collected"]:

            st.write(
                "A small brass key is inside."
            )

            if st.button(
                "🗝️ Collect Key"
            ):

                game["key_collected"] = True

                st.rerun()

        else:

            st.info(
                "You already collected the key."
            )


# ------------------------------------------------------------
# GRANDFATHER CLOCK
# ------------------------------------------------------------

elif selected == "Clock":

    st.subheader("🕰️ Grandfather Clock")

    st.write(
        "The clock contains a hidden compartment."
    )

    if game["clock_solved"]:

        st.success(
            "The compartment is unlocked!"
        )

        st.info(
            "A note reveals the exit code: 6382"
        )

    elif not game["key_collected"]:

        st.warning(
            "You need a key to open the compartment."
        )

    else:

        if st.button(
            "🗝️ Use Key on Clock"
        ):

            game["clock_solved"] = True

            st.rerun()


# ------------------------------------------------------------
# EXIT DOOR
# ------------------------------------------------------------

elif selected == "Door":

    st.subheader("🚪 Locked Exit Door")

    st.write(
        "The exit door requires a secret code."
    )

    if game["escaped"]:

        st.success(
            "The door is open. You escaped!"
        )

    else:

        with st.form("v1_exit_form"):

            code = st.text_input(
                "Enter the exit code",
                max_chars=4,
                key="v1_exit_code"
            )

            submitted = st.form_submit_button(
                "Unlock Door"
            )

            if submitted:

                if not game["clock_solved"]:

                    st.error(
                        "You must unlock the clock first."
                    )

                elif code.strip() == "6382":

                    game["escaped"] = True

                    st.rerun()

                else:

                    st.error(
                        "Incorrect exit code."
                    )


# ============================================================
# 10. VICTORY SCREEN
# ============================================================

if game["escaped"]:

    st.divider()

    st.title("🎉 YOU ESCAPED!")

    st.success(
        "Congratulations! "
        "You escaped The Locked Library."
    )

    if not st.session_state.v1_victory_shown:

        st.balloons()

        st.session_state.v1_victory_shown = True


# ============================================================
# 11. SIMPLE LOCAL GAME MASTER
# ============================================================

def local_hint(message):

    message = message.lower()

    if game["escaped"]:
        return (
            "Congratulations! "
            "You have escaped the library."
        )

    if "book" in message:
        return (
            "Look at the four numbered books "
            "on the bookshelf."
        )

    if "drawer" in message or "desk" in message:
        return (
            "The desk drawer contains something useful. "
            "Try solving the bookshelf first."
        )

    if "clock" in message:
        return (
            "The grandfather clock may require a key."
        )

    if "door" in message or "exit" in message:
        return (
            "The exit door requires a code "
            "hidden somewhere in the library."
        )

    if "key" in message:
        if game["key_collected"]:
            return "You already have the brass key."
        return "Search the desk drawer for a key."

    return (
        "Explore the bookshelf, desk drawer, "
        "clock, and exit door."
    )


# ============================================================
# 12. GEMINI GAME MASTER CHAT
# ============================================================

st.divider()

st.header("🧙 AI Game Master")

if client:
    st.success(
        f"Gemini configured: {MODEL_NAME}"
    )
else:
    st.warning(
        "Gemini is not configured. "
        "Local hints are available."
    )

for message in st.session_state.v1_messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


player_input = st.chat_input(
    "Ask the Game Master for help..."
)


if player_input:

    st.session_state.v1_messages.append({
        "role": "user",
        "content": player_input
    })

    with st.chat_message("user"):
        st.write(player_input)

    with st.chat_message("assistant"):

        if client is None:

            ai_reply = local_hint(player_input)

        else:

            try:

                conversation = []

                for message in st.session_state.v1_messages:

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

                game_context = f"""
CURRENT GAME STATE:
Bookshelf solved: {game["bookshelf_solved"]}
Drawer open: {game["drawer_open"]}
Key collected: {game["key_collected"]}
Clock solved: {game["clock_solved"]}
Escaped: {game["escaped"]}

IMPORTANT:
You are only the Game Master.
Python controls puzzle completion.
Do not claim objects are unlocked unless
the game state confirms it.
Do not reveal the bookshelf code before
the bookshelf is solved.
Do not reveal the exit code before
the clock is solved.
Guide the player to use the clickable
objects and puzzle controls.
Keep responses short.
"""

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=conversation,
                    config={
                        "system_instruction": (
                            GAME_PROMPT
                            + "\n\n"
                            + game_context
                        ),
                        "max_output_tokens": 300
                    }
                )

                ai_reply = response.text

                if not ai_reply:
                    ai_reply = local_hint(player_input)

                ai_reply = ai_reply.replace(
                    "ESCAPE_SUCCESS",
                    ""
                ).strip()

            except Exception as error:

                print(
                    "Gemini error:",
                    type(error).__name__,
                    str(error)
                )

                st.warning(
                    "Gemini is unavailable. "
                    "Using local hints."
                )

                ai_reply = local_hint(player_input)

        st.write(ai_reply)

        st.session_state.v1_messages.append({
            "role": "assistant",
            "content": ai_reply
        })


# ============================================================
# 13. FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Escape Room — Version 1 Interactive Prototype"
)
