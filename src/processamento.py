import pandas as pd

def carregar_dados(caminho):
    try:
        return pd.read_csv(caminho)
    except Exception as e:
        raise Exception(f"Erro ao carregar os dados: {e}")
    
def tratar_dados(df):
    # Exemplo: remover valores nulos e duplicados
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def salvar_resultado(df, caminho):
    try:
        df.to_excel(caminho, index=False)
    except Exception as e:
        raise Exception(f"Error ao salvar resultado: {e}")