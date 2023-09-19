FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install .

CMD streamlit run --server.port 8080 --server.address 0.0.0.0 llama2_chatbot.py
