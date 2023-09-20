import streamlit as st
import state_init as si


def clear_history():
    """
    Clears the chat dialogue history by setting the "chat_dialogue" key in the session state dictionary to an empty list.

    Parameters:
        None

    Returns:
        None
    """
    st.session_state["chat_dialogue"] = []


# add logout button
def logout():
    """
    Deletes the "user_info" key from the session state.

    This function does not take any parameters.

    This function does not return anything.
    """
    try:
        del st.session_state["user_info"]
    except KeyError:
        pass


def render_sidebar():
    with st.sidebar:
        if not si.REPLICATE_API_TOKEN:
            api_key = st.text_input(
                "Replicate API Key", key="chatbot_api_key", type="password"
            )

            "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
            if api_key:
                si.REPLICATE_API_TOKEN = api_key
                st.info("Please refresh your browser.")
            else:
                st.warning("Please add your Replicate API key to continue.")
                st.stop()
        # Dropdown menu to select the model edpoint:
        selected_option = st.sidebar.selectbox(
            "Choose a LLaMA2 model:",
            ["LLaMA2-70B", "LLaMA2-13B", "LLaMA2-7B"],
            key="model",
        )
        if selected_option == "LLaMA2-7B":
            st.session_state["llm"] = si.REPLICATE_MODEL_ENDPOINT7B
        elif selected_option == "LLaMA2-13B":
            st.session_state["llm"] = si.REPLICATE_MODEL_ENDPOINT13B
        else:
            st.session_state["llm"] = si.REPLICATE_MODEL_ENDPOINT70B
        # Model hyper parameters:
        st.session_state["temperature"] = st.sidebar.slider(
            "Temperature:", min_value=0.01, max_value=5.0, value=0.1, step=0.01
        )
        st.session_state["top_p"] = st.sidebar.slider(
            "Top P:", min_value=0.01, max_value=1.0, value=0.9, step=0.01
        )
        st.session_state["max_seq_len"] = st.sidebar.slider(
            "Max Sequence Length:", min_value=64, max_value=4096, value=2048, step=8
        )

        NEW_P = st.sidebar.text_area(
            "Prompt before the chat starts. Edit here if desired:",
            si.PRE_PROMPT,
            height=60,
        )
        if NEW_P != si.PRE_PROMPT and NEW_P:
            st.session_state["pre_prompt"] = NEW_P + "\n\n"
        else:
            st.session_state["pre_prompt"] = si.PRE_PROMPT

        btn_col1, btn_col2 = st.sidebar.columns(2)

        # Add the "Clear Chat History" button to the sidebar

        btn_col1.button(
            "Clear History", use_container_width=True, on_click=clear_history
        )

        btn_col2.button("Logout", use_container_width=True, on_click=logout)

        # add links to relevant resources for users to select
        st.sidebar.write(" ")

        text1 = "Chatbot Demo Code"
        text2 = "LLaMA2 70B Model on Replicate"
        text3 = "LLaMa2 Cog Template"

        text1_link = "https://github.com/a16z-infra/llama2-chatbot"
        text2_link = "https://replicate.com/replicate/llama70b-v2-chat"
        text3_link = "https://github.com/a16z-infra/cog-llama-template"

        logo1 = "https://storage.googleapis.com/llama2_release/a16z_logo.png"
        logo2 = "https://storage.googleapis.com/llama2_release/Screen%20Shot%202023-07-21%20at%2012.34.05%20PM.png"

        st.sidebar.markdown(
            "**Resources**  \n"
            f"<img src='{logo2}' style='height: 1em'> [{text2}]({text2_link})  \n"
            f"<img src='{logo1}' style='height: 1em'> [{text1}]({text1_link})  \n"
            f"<img src='{logo1}' style='height: 1em'> [{text3}]({text3_link})",
            unsafe_allow_html=True,
        )

        st.sidebar.write(" ")
        st.sidebar.markdown(
            "*Made with ❤️ by a16z Infra and Replicate. Not associated with Meta Platforms, Inc.*"
        )
