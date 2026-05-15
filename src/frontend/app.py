import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="RAG Chatbot",
    layout="centered"
)

st.title("LLM-Powered RAG Chatbot")

st.markdown(
    "Ask questions about your uploaded PDFs."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input(
    "Ask a question..."
)

if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    try:

        # Send request to FastAPI backend
        response = requests.post(
            API_URL,
            json={
                "query": user_input
            }
        )

        # Display assistant response
        with st.chat_message("assistant"):

            if response.status_code == 200:

                data = response.json()

                # Display answer
                st.subheader("Answer")
                st.write(data["answer"])

                # Display sources
                st.subheader("Sources")

                for source in data["sources"]:
                    st.write(f"- {source}")

                # Save assistant response to chat history
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": data["answer"]
                    }
                )

            else:

                error_message = (
                    f"API Error: {response.status_code}"
                )

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )

    except Exception as error:

        error_message = (
            f"Error connecting to API: {error}"
        )

        with st.chat_message("assistant"):
            st.error(error_message)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": error_message
            }
        )