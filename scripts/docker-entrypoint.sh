#!/bin/sh
set -eu

# Paths (ajuste se seu Dockerfile copia assets para outro lugar)
TEMP_DIR="/temp"                 # onde o Dockerfile provavelmente colocou os assets
TARGET_ASSETS_DIR="/home/project/assets"

# 1) Inicia cron / crond de maneira compatível
# tenta service, então cron (Debian), então crond (Alpine)
if command -v service >/dev/null 2>&1 && service cron start >/dev/null 2>&1; then
    echo "cron iniciado via service"
elif command -v cron >/dev/null 2>&1; then
    # 'cron' em Debian normalmente inicia em background
    cron
    echo "cron iniciado via cron"
elif command -v crond >/dev/null 2>&1; then
    # 'crond' em Alpine/Debian pode aceitar -b para background; aqui usamos daemon mode (sem -f)
    crond
    echo "cron iniciado via crond"
else
    echo "Aviso: nenhum comando de cron encontrado"
fi

# 2) Corrige assets: copia só se target estiver ausente ou vazio
if [ ! -d "$TARGET_ASSETS_DIR" ] || [ -z "$(ls -A "$TARGET_ASSETS_DIR" 2>/dev/null || true)" ]; then
    echo "Assets target vazio ou inexistente. Tentando copiar de $TEMP_DIR/assets..."
    if [ -d "$TEMP_DIR/assets" ]; then
        mkdir -p "$TARGET_ASSETS_DIR"
        cp -r "$TEMP_DIR/assets/." "$TARGET_ASSETS_DIR/" || true
        echo "Assets copiados."
    else
        echo "Fonte de assets $TEMP_DIR/assets não encontrada. Pulando cópia."
    fi
else
    echo "Assets já existem em $TARGET_ASSETS_DIR, não copiando."
fi

# 3) Remove diretório temporário se existir
if [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
    echo "Diretório temporário $TEMP_DIR removido."
fi

# 4) Executa o processo principal com exec para receber sinais corretamente
echo "Executando bot endpoint..."
exec python3 /home/project/src/endpoint/bot_endpoint.py
