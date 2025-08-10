FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias necesarias para Calibre
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget curl \
    libegl1 \
    libopengl0 \
    libxcb-cursor0 \
    libxrender1 \
    libxi6 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxkbcommon-x11-0 \
    libglib2.0-0 \
    libfreetype6 \
    libfontconfig1 \
    libharfbuzz0b \
    libfribidi0 \
    libjpeg62-turbo \
    libtiff5 \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libasound2 \
    libpng16-16 || apt-get install -y libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar Calibre CLI
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

# Copiar requerimientos
COPY requirements.txt /app/requirements.txt

# Instalar dependencias Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar todo el código
COPY . /app
WORKDIR /app

CMD ["python", "main.py"]
