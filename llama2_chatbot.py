"""
LLaMA 2 Chatbot app
======================

This is a Streamlit chatbot app with LLaMA2 that includes session chat history and an option to select multiple LLM
API endpoints on Replicate. The 7B and 13B models run on Replicate on one A100 40Gb. The 70B runs in one A100 80Gb. The weights have been tensorized.

Contributors: Alexander Martinez Fajardo
Created: September 2023
Version: 0.1.0 (Experimental)
Status: Development
Python version: 3.10

"""
# External libraries:
import streamlit as st
import state_init as si

from utils import debounce_replicate_run
from sidebar import render_sidebar


if not (
    si.REPLICATE_MODEL_ENDPOINT70B
    and si.REPLICATE_MODEL_ENDPOINT13B
    and si.REPLICATE_MODEL_ENDPOINT7B
):
    st.warning(
        "Add a `.env` file to your app directory with the keys specified in `.env_template` to continue."
    )
    st.stop()

###Initial UI configuration:###
st.set_page_config(
    page_title="LLaMA2 Chatbot by a16z-infra", page_icon="🦙", layout="wide"
)


def handle_input():
    if prompt := st.chat_input("Type your question here"):
        # Add user message to chat history
        st.session_state.chat_dialogue.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.write(prompt)


def generate_llama2_response():
    string_dialogue = st.session_state["pre_prompt"]
    # Building the chat history or also called context
    for dict_message in st.session_state.chat_dialogue:
        if dict_message["role"] == "user":
            string_dialogue = (
                string_dialogue + "User: " + dict_message["content"] + "\n\n"
            )
        else:
            string_dialogue = (
                string_dialogue + "Assistant: " + dict_message["content"] + "\n\n"
            )

    # Generating a response give the context and the model intance
    output = debounce_replicate_run(
        st.session_state["llm"],
        string_dialogue,
        st.session_state["max_seq_len"],
        st.session_state["temperature"],
        st.session_state["top_p"],
        si.REPLICATE_API_TOKEN,
    )
    return output


def render_app():
    # reduce font sizes for input text boxes
    custom_css = """
        <style>
            .stTextArea textarea {font-size: 13px;}
            div[data-baseweb="select"] > div {font-size: 13px !important;}
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Left sidebar menu
    st.sidebar.header("LLaMA2 Chatbot")

    # Set config for a cleaner menu, footer & background:
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    si.initialize()

    render_sidebar()
    if not si.REPLICATE_API_TOKEN:
        st.info("Please add your Replicate API key to continue.")
        st.stop()

    # Display chat messages from history on app rerun
    for message in st.session_state.chat_dialogue:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    handle_input()

    if st.session_state.chat_dialogue[-1]["role"] == "user":
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            # Generate a response
            output = generate_llama2_response()

            # Display response as it comes in generator
            for item in output:
                full_response += item
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.chat_dialogue.append(
            {"role": "assistant", "content": full_response}
        )


render_app()
