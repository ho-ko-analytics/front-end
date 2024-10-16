import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega variaveis de ambiente
load_dotenv()

# Configura api
client = OpenAI(api_key=os.getenv("API_KEY_OPENAI"))

# Função para criar o assistente com File Search habilitado
def create_assistant_with_file_search():
    assistant = client.beta.assistants.create(
        name="Meu ajudante de análise",
        instructions="Você é um assistente para me ajudar com análise de dados.",
        model="gpt-4o",
        tools=[{"type": "file_search"}], # Habilitando o file_search
    )
    print(f"Assistente criado com ID: {assistant}")
    return assistant

# Criar um Vector Store para armazenar arquivos
def create_vector_store():
    vector_store = client.beta.vector_stores.create(name="Vendas Data Store")
    print(f"Vecto Store criado com ID: {vector_store.id}")
    return vector_store

# Carrega os arquivos JSON no Vector Store e aguarda o processamento
def upload_files_to_vector_store(vector_store, file_paths):
    file_streams = []
    for file_path in file_paths:
        try:
            with open(file_path, "rb") as file:
                file_streams.append(file)
            print(f"Arquivo {file_path} preparado para upload.")
        except FileNotFoundError:
            print(f"Arquivo {file_path} não encontrado.")

    if file_streams:
        file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store.id, files=file_streams
        )
        print(f"Status do upload: {file_batch.status}")
        print(f"Contagem de arquivos: {file_batch.file_counts}")
    else:
        print("Nenhum arquivo foi preparado para upload.")

# Atualizar o assistente para usar o Vector Store
def upload_assistant_with_vector_store(assistant, vector_store):
    client.beta.assistants.update(
        assistant_id=assistant.id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
    )
    print("Assistente atualizado para usar o Vector Store")

# Criar o assistente com file_search habilitado
assistant = create_assistant_with_file_search()

# Criar um Vector Store e fazer o upload dos arquivos JSON
vector_store = create_vector_store()
upload_files_to_vector_store(vector_store, ["array de nome de arquivos no mesmo diretório"])

# Atualizar o assistente com Vector Store criado
upload_assistant_with_vector_store(assistant, vector_store)