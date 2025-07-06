import streamlit as st
import requests

st.title("Google Calendar Booking Bot")
st.info(
    "Please enter your event in this format:\n"
    "`Event Name | YYYY-MM-DD | HH:MM (24hr)`\n\n"
    "You can chat with the AI for suggestions or help. When ready, click 'Mail Me' to receive your invite."
)

user_email = st.text_input("Enter your email to receive the invite:")

if "history" not in st.session_state:
    st.session_state["history"] = []
if "last_event" not in st.session_state:
    st.session_state["last_event"] = None

user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input:
    st.session_state["history"].append({"role": "user", "content": user_input})
    resp = requests.post(
        "http://localhost:8000/chat",
        json={
            "message": user_input,
            "history": st.session_state["history"],
        },
    )
    data = resp.json()
    bot_reply = data["response"]
    st.session_state["history"] = data["history"]
    st.session_state["last_event"] = data.get("event")  # Save event details if parsed

for msg in st.session_state["history"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

if st.session_state.get("last_event") and user_email:
    if st.button("Mail Me"):
        resp = requests.post(
            "http://localhost:8000/mail",
            json={
                "email": user_email,
                "event": st.session_state["last_event"],
            },
        )
        if resp.status_code == 200:
            st.success("Invite sent to your email!")
        else:
            st.error("Failed to send invite.")