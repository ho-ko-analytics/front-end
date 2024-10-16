import psycopg2
import random

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    host="dpg-crmqgat6l47c739unto0-a.oregon-postgres.render.com",
    database="banco_de_dados_teste_ho_ko",
    user="postgresadm",
    password="0KEHiT66NIncvSe0EhPk67c4gI0QJogf",
    port="5432"
)

cur = conn.cursor()

# Função de validação e tratamento de dados antes da inserção (ETL)
def validar_e_tratar_dados(alcance, impressoes, compartilhamento, curtidas, cliques, comentarios, gasto):
    # Garantir que os valores numéricos são positivos
    alcance = max(0, alcance)
    impressoes = max(0, impressoes)
    compartilhamento = max(0, compartilhamento)
    curtidas = max(0, curtidas)
    cliques = max(0, cliques)
    comentarios = max(0, comentarios)

    # Garantir que o gasto tenha no máximo duas casas decimais
    gasto = round(gasto, 2)
    
    return alcance, impressoes, compartilhamento, curtidas, cliques, comentarios, gasto

# Gerando e inserindo 20 linhas com valores crescentes
alcance = 1000
impressoes = 1500
compartilhamento = 10
curtidas = 100
cliques = 50
comentarios = 20
gasto = 10.00

for i in range(20):
    # Incremento nos valores para simular crescimento
    alcance += random.randint(100, 200)
    impressoes += random.randint(200, 300)
    compartilhamento += random.randint(1, 3)
    curtidas += random.randint(10, 20)
    cliques += random.randint(5, 10)
    comentarios += random.randint(2, 5)
    gasto += random.uniform(5.00, 10.00)  # Gerar um valor aleatório para gasto

    # Validação e tratamento de dados antes da inserção
    alcance, impressoes, compartilhamento, curtidas, cliques, comentarios, gasto = validar_e_tratar_dados(
        alcance, impressoes, compartilhamento, curtidas, cliques, comentarios, gasto
    )

    # Inserir os dados tratados na tabela
    cur.execute('''
        INSERT INTO facebook_ads (alcance, impressoes, compartilhamento, curtidas, cliques, comentarios, gasto)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    ''', (alcance, impressoes, compartilhamento, curtidas, cliques, comentarios, gasto))

# Salvar as alterações e fechar a conexão
conn.commit()
cur.close()
conn.close()

print("Inserção concluída com sucesso!")
