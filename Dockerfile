FROM python:3.11-slim

# Instalar dependencias del sistema necesarias para Calibre
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
    && rm -rf /var/lib/apt/lists/*

# Instalar Calibre (CLI)
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

# Copiar requerimientos de Python
COPY requirements.txt /app/requirements.txt

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar todo el proyecto
COPY . /app
WORKDIR /app

# Comando por defecto
CMD ["python", "main.py"]
