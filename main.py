import streamlit as st
import html
from database import init_db, register_user, validate_login, save_message, get_chat_history
# Add at the top of main.py
from advisor_response import get_advice


# -------------------- DB Initialization --------------------
init_db()

# -------------------- Session State Setup --------------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'first_login' not in st.session_state:
    st.session_state.first_login = True

# -------------------- Chat UI --------------------
def chat_message(message, is_user=False):
    bubble_color = "#4CAF50" if is_user else "#ECECEC"
    text_color = "white" if is_user else "black"
    align = "flex-end" if is_user else "flex-start"
    bubble_margin = "margin-left:auto;" if is_user else "margin-right:auto;"
    border_radius = "18px 18px 0px 18px" if is_user else "18px 18px 18px 0px"

    st.markdown(
        f"""
        <div style='display:flex; justify-content:{align}; {bubble_margin} margin-top:6px; margin-bottom:6px;'>
            <div style='background-color:{bubble_color}; color:{text_color}; padding:12px 16px; border-radius:{border_radius}; max-width:70%; word-wrap:break-word;'>
                {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------- Login/Register --------------------
def login_register():
    st.title("Finwise - Login / Register 🛡️")

    menu = st.sidebar.selectbox("Choose Action", ["Login", "Register"])

    if menu == "Register":
        st.subheader("Create a New Account")
        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")
        confirm_pass = st.text_input("Confirm Password", type="password")
        if st.button("Register"):
            if new_pass != confirm_pass:
                st.warning("Passwords do not match!")
            elif register_user(new_user, new_pass):
                st.success("User Registered. Please login.")
            else:
                st.warning("Username already exists!")

    elif menu == "Login":
        st.subheader("Login to your account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if validate_login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.first_login = True
                # Load chat history from DB
                st.session_state.chat_history = get_chat_history(username)
                st.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password")

# -------------------- Chatbot --------------------
def chatbot_page():
    st.title("Finwise Chatbot 💬")
    st.sidebar.write(f"Logged in as: **{st.session_state.username}**")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.chat_history = []
        st.rerun()

    # First greeting (sirf jab pehli baar ho)
    if st.session_state.first_login:
        if not st.session_state.chat_history:
            greeting = "Hello! I'm your personal financial advisor. Let me understand your profile first."
            st.session_state.chat_history.append({"role": "advisor", "text": greeting})
            save_message(st.session_state.username, "advisor", greeting)
        st.session_state.first_login = False

    # Show chat history
    for msg in st.session_state.chat_history:
        chat_message(msg["text"], is_user=(msg["role"] == "user"))

    # Message input area
    with st.container():
        user_message = st.text_area("Type your message...", height=80, key="chat_input", placeholder="Type something...")
        col1, col2 = st.columns([0.85, 0.15])
        with col2:
            if st.button("Send", use_container_width=True):
                if user_message.strip():
                    cleaned_user_message = html.escape(user_message.strip())
                    st.session_state.chat_history.append({"role": "user", "text": cleaned_user_message})
                    save_message(st.session_state.username, "user", cleaned_user_message)

                    # Example advisor response
                    # advisor_reply = "Okay, please tell me more."
                    # Get actual advice from vector store
                    advisor_reply = get_advice(cleaned_user_message)
                    st.session_state.chat_history.append({"role": "advisor", "text": advisor_reply})
                    save_message(st.session_state.username, "advisor", advisor_reply)

                    st.rerun()

# -------------------- Main Flow --------------------
if not st.session_state.logged_in:
    login_register()
else:
    chatbot_page()
