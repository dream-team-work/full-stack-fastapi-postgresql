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

# Criar o ambiente virtual
RUN python -m venv /opt/venv

# Ativar o ambiente virtual
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Instalar as dependências dentro do ambiente virtual
RUN pip install --no-cache-dir -r /app/requirements.txt

# Instalar o Uvicorn (servidor ASGI recomendado para FastAPI)
RUN pip install uvicorn

# Expor a porta 8000
EXPOSE 8000

# O comando de inicialização do FastAPI com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
