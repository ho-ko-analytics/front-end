import psycopg2

# Conectar ao banco de dados PostgreSQL
try:
    # Conexão ao banco de dados PostgreSQL no Render
    conn = psycopg2.connect(
        host="dpg-crmqgat6l47c739unto0-a.oregon-postgres.render.com",  # Substituir com o host do Render
        database="banco_de_dados_teste_ho_ko",  # Nome do banco de dados
        user="postgresadm",  # Nome do usuário
        password="0KEHiT66NIncvSe0EhPk67c4gI0QJogf",  # Senha do banco de dados
        port="5432",  # A porta padrão do PostgreSQL
        options='-c client_encoding=UTF8'  # Forçando UTF-8
    )
    print("Conexão bem-sucedida!")
    
    # Criar um cursor
    cur = conn.cursor()

    # Executar a query para buscar todos os dados da tabela facebook_ads
    cur.execute("SELECT * FROM facebook_ads;")

    # Recuperar todos os dados
    rows = cur.fetchall()

    # Exibir os dados retornados
    for row in rows:
        print(f"ID: {row[0]}, Alcance: {row[1]}, Impressões: {row[2]}, Compartilhamento: {row[3]}, "
              f"Curtidas: {row[4]}, Cliques: {row[5]}, Comentários: {row[6]}, Gasto: {row[7]}")

    # Fechar o cursor e a conexão
    cur.close()
    conn.close()

except Exception as e:
    print(f"Erro ao conectar: {e}")
