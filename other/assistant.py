import streamlit as st
import time
from openai import OpenAI
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Configuração da API e do ID do Assistente
ASSISTANT_ID = "asst_2VLOBkoS184ayCditD4n6H1l"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Função para enviar uma pergunta ao assistente e obter a resposta
def responder_pergunta(pergunta):
    # Cria um novo thread com a mensagem do usuário
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": f"hoje é dia {datetime.now()}. {pergunta}"
            }
        ]
    )

    # Envia a thread para o assistente (como uma nova execução)
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
    st.write(f"Conversa id: {run.id}")

    # Aguarda a conclusão da execução
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        st.write(f"Run status: {run.status}")
        time.sleep(1)

    st.write(f"Rin Completed!")

    # Obtém a última mensagem da thread
    message_response = client.beta.threads.messages.list(thread_id=thread.id)
    messages = message_response.data

    # Extrai e retorna a resposta mais recente
    laster_message = messages[0]
    return laster_message.content[0].text.value.strip()

# Interface do streamlit
st.title("Agente - Pergunte ao assistente")

# Caixa de entrada para perguntas
pergunta = st.text_input("Digite sua pergunta: ")

# Quando a pergunta é feita, envia para o assistente e exibe a resposta
if pergunta:
    resposta = responder_pergunta(pergunta)
    st.write(f"Resposta: {resposta}")