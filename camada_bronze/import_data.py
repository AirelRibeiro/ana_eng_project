import requests
import io
import pandas as pd
from sqlalchemy import create_engine

# URLs dos arquivos CSVs
urls = {
    'reviews': "http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2023-09-22/data/reviews.csv.gz",
    'listings': "http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2023-09-22/data/listings.csv.gz",
    'calendar': "http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2023-09-22/data/calendar.csv.gz",
}

# Função para baixar e carregar o arquivo em um DataFrame
def download_df(url):
    response = requests.get(url)
    if response.status_code == 200:
        file_buffer = io.BytesIO(response.content)
        num_rows_to_read = 1000 # Limite de dados, para não sobrecarregar processador
        df = pd.read_csv(file_buffer, nrows=num_rows_to_read, compression='gzip')
        return df
    else:
        print(f"Falha ao baixar o arquivo de {url}")
        return None

# Função para enviar os dados para o banco de dados
def save_to_db(df, table_name, engine):
    if df is not None:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Dados inseridos na tabela {table_name}")

def main():
    # Configuração de conexão com o banco de dados PostgreSQL
    conn_str = "postgresql://postgres:postgres@localhost:5432/postgres"
    engine = create_engine(conn_str)

    # Baixando e carregando os três arquivos
    reviews_df = download_df(urls['reviews'])
    listings_df = download_df(urls['listings'])
    calendar_df = download_df(urls['calendar'])

    # Enviando os dados para o banco de dados
    save_to_db(reviews_df, 'reviews', engine)
    save_to_db(listings_df, 'listings', engine)
    save_to_db(calendar_df, 'calendar', engine)

if __name__ == "__main__":
    main()
