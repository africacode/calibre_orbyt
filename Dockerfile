FROM python:3.11-slim

# Instalar todas las dependencias necesarias para Calibre CLI
RUN apt-get update && apt-get install -y \
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
    libpng16-16 \
    libjpeg62-turbo \
    libtiff5 \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Instalar Calibre (CLI)
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

# Copiar requerimientos de Python
COPY requirements.txt /app/requirements.txt

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar todo el código
COPY . /app
WORKDIR /app

# Comando por defecto
CMD ["python", "main.py"]
