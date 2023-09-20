import os
import streamlit as st

from dotenv import load_dotenv


load_dotenv()
###Global variables:###
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN", default="")


# Your your (Replicate) models' endpoints:
REPLICATE_MODEL_ENDPOINT7B = os.environ.get("REPLICATE_MODEL_ENDPOINT7B", default="")
REPLICATE_MODEL_ENDPOINT13B = os.environ.get("REPLICATE_MODEL_ENDPOINT13B", default="")
REPLICATE_MODEL_ENDPOINT70B = os.environ.get("REPLICATE_MODEL_ENDPOINT70B", default="")
PRE_PROMPT = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as Assistant."


def initialize() -> None:
    """
    Set up/Initialize Session State variables.
    """
    # Set up/Initialize Session State variables:
    if "chat_dialogue" not in st.session_state:
        st.session_state["chat_dialogue"] = [
            {"role": "assistant", "content": "How may I assist you today?"}
        ]
    if "llm" not in st.session_state:
        # st.session_state['llm'] = REPLICATE_MODEL_ENDPOINT13B
        st.session_state["llm"] = REPLICATE_MODEL_ENDPOINT70B
    if "temperature" not in st.session_state:
        st.session_state["temperature"] = 0.1
    if "top_p" not in st.session_state:
        st.session_state["top_p"] = 0.9
    if "max_seq_len" not in st.session_state:
        st.session_state["max_seq_len"] = 512
    if "pre_prompt" not in st.session_state:
        st.session_state["pre_prompt"] = PRE_PROMPT
    if "string_dialogue" not in st.session_state:
        st.session_state["string_dialogue"] = ""
