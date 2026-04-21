import pandas as pd

# ===============================
# EXTRAÇÃO
# ===============================
def extract():
    """
    Lê os dados do arquivo CSV que está na mesma pasta.
    """
    try:
        # Removido o "data/" pois o arquivo está na raiz
        df = pd.read_csv("ids.csv") 
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print("Erro: O arquivo 'ids.csv' não foi encontrado na pasta.")
        return []

# ===============================
# TRANSFORMAÇÃO
# ===============================
def generate_message(user_id):
    """
    Gera a mensagem usando o UserID.
    """
    return f"Olá usuário {user_id}, investir hoje é o melhor caminho para garantir seu futuro financeiro!"

def transform(users):
    """
    Enriquece os dados usando o UserID.
    """
    for user in users:
        # Alterado para 'UserID' para bater com o seu CSV atual
        user["mensagem"] = generate_message(user["UserID"])
    return users

# ===============================
# CARGA
# ===============================
def load(users):
    """
    Salva o resultado em 'output.csv' na mesma pasta.
    """
    if users:
        df = pd.DataFrame(users)
        df.to_csv("output.csv", index=False)
        print("Arquivo 'output.csv' gerado com sucesso!")

# ===============================
# PIPELINE PRINCIPAL
# ===============================
def main():
    users = extract()
    if users:
        users = transform(users)
        load(users)
        print("Pipeline ETL executado com sucesso!")

if __name__ == "__main__":
    main()