# pages/analyzes_page.py
import os
import streamlit as st

from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
) 
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

from pages.components.filters import filters

def agentAI(system_prompt, groq_chat, memory, textEmpty):
    # Template de prompt do chat
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ]
    )

    # Criar a cadeia de conversação usando o modelo LLM
    conversation = LLMChain(
        llm=groq_chat,
        prompt=prompt,
        verbose=False,
        memory=memory,
    )

    # Gerar a resposta do chatbot
    response = conversation.predict(human_input=textEmpty)

    return response


def analyzes_page():
    selected_filters = filters()
    # Obter a chave de API do Groq a partir das variáveis de ambiente
    groq_api_key = os.environ['GROQ_API_KEY']
    model = 'llama3-8b-8192'
    
    # Prompt do sistema e configurações de memória da conversa
    system_prompt = f'Hoje é dia 16 de outubro de 2024. Você é um chatbot de conversação amigável de análise de dados. Posso escolher um tipo de análise e me retorne resultados quaisquer baseado em redes sociais (como se fosse um cliente de uma agência de marketing). use facebook, instagram, google ads. então me gere um relatório "exemplo" com dados fictíceis de {selected_filters['data_inicial']} até {selected_filters['data_final']}. Respostas sempre em portugês - Brasil.'
    conversational_memory_length = 5

    # Inicializar o objeto de chat do Groq Langchain
    groq_chat = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name=model
    )

    # Criar a memória da conversa
    memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

    # Colocando três botões em uma única linha
    col1, col2, col3 = st.columns(3)

    # Variável para armazenar qual botão foi clicado
    botao_clicado = None

    # Definindo a ação para cada botão
    with col1:
        if st.button("Descritiva"):
            botao_clicado = "descritiva"

    with col2:
        if st.button("Preditiva"):
            botao_clicado = "preditiva"

    with col3:
        if st.button("Prescritiva"):
            botao_clicado = "prescritiva"

    # Exibindo respostas com base no botão clicado
    if botao_clicado:
        response = agentAI(system_prompt, groq_chat, memory, botao_clicado)
        st.write(response)
    else:
        st.write("\nClique em um dos botões para ver um relatório de análise.")
