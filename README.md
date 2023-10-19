## Configuração Inicial

### Instalar o Docker e o Docker Compose:

Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina. Caso não tenha, siga as instruções nos links abaixo:

Docker: https://docs.docker.com/get-docker/

Docker Compose: https://docs.docker.com/compose/install/

### Com o Docker instalado e dentro do repositório, basta subir o banco e rodar o script para populá-lo

- Subir o banco de dados:
  Execute o comando a seguir para subir o banco de dados PostgreSQL:

```
docker-compose up -d
```

- Instalar as dependências Python:
  Execute o comando para instalar as dependências necessárias no seu ambiente Python:

```
pip install -r requirements.txt
```

- Rodar o script de importação:
  Execute o comando para rodar o script de importação de dados e criação da camada bronze no banco de dados:

```
python3 ./camada_bronze/import_data.py

```

O script baixará os dados dos arquivos CSV especificados e os importará para o banco de dados PostgreSQL.

### Para passar para os processos da camada silver, basta acessar o diretório `camada_silver` e abrir o Jupyter `camada_silver.ipynb`, a primeira célula recupera os dados e coloca-os e dataframes.
