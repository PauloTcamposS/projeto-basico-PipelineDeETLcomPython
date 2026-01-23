import pandas as pd

# ===============================
# EXTRAÇÃO
# ===============================
def extract():
    """
    Lê os dados do arquivo CSV e retorna uma lista de usuários
    """
    df = pd.read_csv("data/ids.csv")
    users = df.to_dict(orient="records")
    return users


# ===============================
# TRANSFORMAÇÃO
# ===============================
def generate_message(name):
    """
    Simula a geração de uma mensagem personalizada (IA simulada)
    """
    return f"Olá {name}, investir hoje é o melhor caminho para garantir seu futuro financeiro!"


def transform(users):
    """
    Enriquecer os dados dos usuários com mensagens personalizadas
    """
    for user in users:
        user["mensagem"] = generate_message(user["name"])
    return users


# ===============================
# CARGA
# ===============================
def load(users):
    """
    Salva os dados transformados em um novo arquivo CSV
    """
    df = pd.DataFrame(users)
    df.to_csv("data/output.csv", index=False)


# ===============================
# PIPELINE PRINCIPAL
# ===============================
def main():
    users = extract()
    users = transform(users)
    load(users)
    print("Pipeline ETL executado com sucesso!")


if __name__ == "__main__":
    main()
