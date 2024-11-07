#!/bin/bash

# Depuração: Verificar se o ambiente virtual foi criado corretamente
echo "Ativando o ambiente virtual..."

# Verificar se o ambiente virtual existe
if [ ! -d "/app/.venv" ]; then
    echo "Erro: ambiente virtual não encontrado."
    exit 1
fi

# Ativar o ambiente virtual
source /app/.venv/bin/activate

# Verificar se o SQLAlchemy está instalado no ambiente virtual
echo "Verificando se o SQLAlchemy está instalado..."
/app/.venv/bin/pip show sqlalchemy

# Executar o script de pré-inicialização
echo "Executando o script backend_pre_start.py..."
python /app/app/backend_pre_start.py
