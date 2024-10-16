import chromadb
chroma_client = chromadb.Client()

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(name="colecao_trafego_pago")

# switch `add` to `upsert` to avoid adding the same documents every time
collection.upsert(
    documents=[
        "Facebook Ads, CPC: R$0,50, CTR: 2%, Conversão: 5%, Setembro 2023.",
        "Google Ads, CPC: R$0,80, CTR: 1,5%, Conversão: 3%, Setembro 2023.",
        "LinkedIn Ads, CPC: R$1,20, CTR: 3%, Conversão: 1,5%, Setembro 2023.",
        "Facebook Ads, CPC: R$0,45, CTR: 1,8%, Conversão: 4%, Agosto 2023.",
        "Google Ads, CPC: R$0,75, CTR: 1,6%, Conversão: 3,5%, Agosto 2023.",
        "LinkedIn Ads, CPC: R$1,10, CTR: 2,8%, Conversão: 2%, Agosto 2023."
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5", "doc6"]
)

# Pergunta mais complexa: qual plataforma teve o maior aumento na CTR de agosto para setembro de 2023?
results = collection.query(
    query_texts=["Qual plataforma de tráfego pago teve o menor CTR em setembro de 2023?"],  # O Chroma vai gerar embeddings para isso
    n_results=2  # quantos resultados retornar
)

print(results)
