# para desenvolvimento use o Dockerfile-dev
FROM --platform=linux/amd64 python:3.10-slim AS build

WORKDIR /home/project
ENV PYTHONPATH=/home/project

# instalar pacotes do sistema, incluindo locales e cron; então gerar pt_BR.UTF-8
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    tzdata \
    cron \
    locales \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    libssl-dev \
    pkg-config \
    libffi-dev \
 && sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen \
 && locale-gen pt_BR.UTF-8 \
 && update-locale LANG=pt_BR.UTF-8 \
 && rm -rf /var/lib/apt/lists/*

# copiar requirements antes para aproveitar cache
COPY requirements.txt requirements.txt

# definir timezone (usado em runtime)
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
 && echo "America/Sao_Paulo" > /etc/timezone

# atualizar pip e instalar dependências Python
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# copiar resto do projeto
COPY . .

# criar diretório temporário e copiar assets para lá (entrypoint irá mover se necessário)
RUN mkdir -p /temp
COPY assets /temp

# configurar locale de runtime - pt_BR gerado no build
ENV LANG=pt_BR.UTF-8
ENV LC_ALL=pt_BR.UTF-8
ENV LC_COLLATE=pt_BR.UTF-8

# criar um arquivo de cron em /etc/cron.d (padrão para containers)
RUN printf "0 12 * * * root cd /home/project && /usr/local/bin/python3 /home/project/src/Main.py >> /proc/1/fd/1 2>&1\n0 16-22/2 * * * root cd /home/project && /usr/local/bin/python3 /home/project/src/Main.py >> /proc/1/fd/1 2>&1\n" \
    > /etc/cron.d/bot-notif \
 && chmod 0644 /etc/cron.d/bot-notif

# garantir entrypoint executável (presume scripts/docker-entrypoint.sh existir)
RUN chmod +x /home/project/scripts/docker-entrypoint.sh

ENTRYPOINT ["/home/project/scripts/docker-entrypoint.sh"]