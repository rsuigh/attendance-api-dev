# Use a imagem oficial do Python como base
FROM python:3.9

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código do projeto para o diretório de trabalho no contêiner
COPY . .

# Expõe a porta que o Django usará
EXPOSE 8009

# Comando para rodar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8009"]
