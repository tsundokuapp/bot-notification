#!/bin/sh

# Verifica se /home/project/assets está vazio
if [ -z "$(ls -A /home/project/assets)" ]; then
    # Copia os assets apenas se /home/project/assets estiver vazio
    cp -r /home/project/temp/assets/* /home/project/assets/
fi

# Removendo o diretório temporário /home/project/temp
rm -rf /home/project/temp

crond

python3 /home/project/src/endpoint/bot_endpoint.py