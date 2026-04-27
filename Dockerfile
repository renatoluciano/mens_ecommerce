# Usa uma imagem oficial do Python mais enxuta
FROM python:3.10-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Evita que o Python grave arquivos .pyc e garante que os logs saiam em tempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copia o arquivo de dependências e instala as bibliotecas
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do seu computador para dentro do container
COPY . /app/

# Expõe a porta que o Django usa
EXPOSE 8000
