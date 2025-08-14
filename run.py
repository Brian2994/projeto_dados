import yaml
import logging
from src import processamento

# Carregar configurações
with open("config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

# Configurar log
logging.basicConfig(filename=config["log_path"], level=logging.INFO, format="%(asctime)s - %(message)s")

def main():
    try:
        logging.info("Iniciando tratamento de dados...")

        df = processamento.carregar_dados(config["input_path"])
        df_tratado = processamento.tratar_dados(df)
        processamento.salvar_resultado(df_tratado, config["output_path"])

        logging.info("Processamento finalizado com sucesso.")
    except Exception as e:
        logging.error(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    main()