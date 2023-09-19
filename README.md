#  LLaMA 2 Chatbot App ⚡
 ![image](llama-logo.png)

[![Develop in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/alex00pep/llama2-chatbot?quickstart=1)

## 🤔 What is this?

This is an experimental Streamlit chatbot app built for LLaMA2 (or any other LLM). The app includes session chat history and provides an option to select multiple LLaMA2 API endpoints on Replicate.

Live demo: [LLaMA2.ai](https://llama2.ai/)

For the LLaMA2 license agreement, please check the Meta Platforms, Inc official license documentation on their website. 
[More info.](https://ai.meta.com/llama/)

<img width="1710" alt="llama2 demo" src="https://github.com/a16z-infra/llama2-chatbot/assets/5958899/7512cbd3-ef90-4a9f-b9f6-eab5be7a483f">

## Features

- Chat history is maintained for each session (if you refresh, chat history clears)
- Option to select between different LLaMA2 chat API endpoints (7B, 13B or 70B). The default is 70B.
- Configure model hyperparameters from the sidebar (Temperature, Top P, Max Sequence Length).
- Includes "User:" and "Assistant:" prompts for the chat conversation.
- Each model (7B, 13B & 70B) runs on Replicate - (7B and 13B run on one A100 40Gb, and 70B runs on one A100 80Gb).
- Docker image included to deploy this app in Fly.io

## Installation

- Clone the repository
- [Recommended] Create a virtual python environment with the command `python -m venv .venv` and activate it with `source .venv/bin/activate`
- Install dependencies with `pip install -r requirements.txt`
- Create an account on [Replicate](https://replicate.com/)
- Make your own `.env` file with the command `cp .env_template .env`. Then edit the `.env` file and add your:
    - [Replicate API token](https://replicate.com/account) as `REPLICATE_API_TOKEN`
    - For your convenience, we include common model endpoints already in the `.env_template` file
- Run the app with `streamlit run llama2_chatbot.py`
- Dockerfile included to [deploy this app](#deploying-on-flyio) in Fly.io or run Docker locally with:
    ```
    docker build -t llama2-chatbot .
    docker run -d -p 80:8080 llama2-chatbot
    ```

(Note: if you are using a Mac, you may need to use the command `python3` instead of `python` and `pip3` instead of `pip`)

## Usage

- Start the chatbot by selecting an API endpoint from the sidebar.
- Configure model hyperparameters from the sidebar.
- Type your question in the input field at the bottom of the app and press enter.


## 🛠️ Libraries Used

Here's a table of the main libraries used in this project:

| Library               | Version | Description                                          |
| --------------------- | ------- | ---------------------------------------------------- |
| `replicate`           |         | Library for interacting with Replicate               |
| `os`                  |         | Operating system related utilities                   |
| `streamlit`           |         | Python Library to build and share web and AI/ML apps |



## Deploying on fly.io
1. First you should [install flyctl](https://fly.io/docs/hands-on/install-flyctl/) and login from command line
2. `fly launch` -> this will generate a fly.toml for you automatically
3. `fly deploy --dockerfile Dockerfile` --> this will automatically package up the repo and deploy it on fly. If you have a free account, you can use `--ha=false` flag to only spin up one instance
4. Go to your deployed fly app dashboard, click on `Secrets` from the left hand side nav, and click on `Use the Web CLI to manage your secrets without leaving your browser`. Once you are on your app's web CLI, export all secrets needed. i.e `export REPLICATE_API_TOKEN=your_replicate_token`. Refer to .env.example file for necessary secrets. 

## Authors

- Alexander Martinez Fajardo - [alex00pep](https://github.com/alex00pep)

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

This project is under development. Contributions are welcome!

## License

- Web chatbot license (this repo): Apache 2.0
- For the LLaMA models license, please refer to the License Agreement from Meta Platforms, Inc.

## Acknowledgements

- Special thanks to the team at Meta AI, Replicate, a16z-infra and the entire open-source community.

## Disclaimer

This is an experimental version of the app. Use at your own risk. While the app has been tested, the authors hold no liability for any kind of losses arising out of using this application. 

## UI Configuration

The app has been styled and configured for a cleaner look. Main menu and footer visibility have been hidden. Feel free to modify this to your custom application.

## Resources

- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [GitHub to deploy LLaMA2 on Replicate](https://github.com/a16z-infra/cog-llama-template)
