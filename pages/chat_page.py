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

def chat_page():
    """
    Função principal para configurar o chatbot Groq e a interface Streamlit.
    """
    # Obter a chave de API do Groq a partir das variáveis de ambiente
    groq_api_key = os.environ['GROQ_API_KEY']
    model = 'llama3-8b-8192'
    
    # Prompt do sistema e configurações de memória da conversa
    system_prompt = 'Você é um chatbot de conversação amigável.'
    conversational_memory_length = 5

    # Inicializar o objeto de chat do Groq Langchain
    groq_chat = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name=model
    )

    # Criar a memória da conversa
    memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)
    
    user_input = st.text_input("Digite sua mensagem:", "", key="user_input")
    
    # Exibindo respostas com base no botão clicado e input do usuário
    response = agentAI(system_prompt, groq_chat, memory, user_input)
    st.write(response)