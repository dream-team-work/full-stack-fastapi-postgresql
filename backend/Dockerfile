# Use Python 3.10 como base
FROM python:3.10

# Defina o diretório de trabalho
WORKDIR /app

# Copiar o código da aplicação para o container
COPY app /app

# Copiar o arquivo de requisitos
COPY requirements.txt /app/

# Copiar os scripts para /app/scripts
COPY scripts /app/scripts

# Criar um ambiente virtual e instalar dependências
RUN pip install --no-cache-dir -r /app/requirements.txt

# Instalar o Uvicorn (servidor ASGI recomendado para FastAPI)
RUN pip install uvicorn

# Expor a porta 8000
EXPOSE 8000

# O comando de inicialização do FastAPI com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
