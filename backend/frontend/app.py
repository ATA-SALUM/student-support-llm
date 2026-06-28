import streamlit as st
import requests

BACKEND = "http://127.0.0.1:8000"
API_KEY = "student123"

st.set_page_config(page_title="Student Support Assistant")

st.title("🎓 University Student Support Assistant")

# ---------------- LOGIN ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "question" not in st.session_state:
    st.session_state.question = ""

if not st.session_state.logged_in:

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == "admin" and password == "1234":

            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()

        else:

            st.error("Invalid username or password")

else:

    st.success("Logged in")

    question = st.text_input("Ask a question")

    if st.button("Ask"):

        if question.strip() == "":

            st.warning("Please enter a question")

        else:

            with st.spinner("Thinking..."):

                try:

                    response = requests.post(

                        BACKEND + "/ask",

                        headers={
                            "x-api-key": API_KEY
                        },

                        json={
                            "question": question
                        }

                    )

                    data = response.json()

                    if "answer" in data:

                        st.session_state.answer = data["answer"]
                        st.session_state.question = question

                    else:

                        st.error(data["error"])

                except:

                    st.error("Backend is not running")

    if st.session_state.answer != "":

        st.subheader("Answer")

        st.write(st.session_state.answer)

        rating = st.radio(

            "Rate this answer",

            [

                "Good",

                "Average",

                "Poor"

            ]

        )

        if st.button("Submit Feedback"):

            requests.post(

                BACKEND + "/feedback",

                headers={
                    "x-api-key": API_KEY
                },

                json={

                    "question":
                    st.session_state.question,

                    "answer":
                    st.session_state.answer,

                    "rating":
                    rating

                }

            )

            st.success("Feedback saved successfully!")