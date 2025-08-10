FROM python:3.10-slim

# Instalamos dependencias necesarias para calibre
RUN apt-get update && apt-get install -y \
    wget \
    libegl1 \
    libopengl0 \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

# Instalamos calibre
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

# Copiamos tu script y recetas
WORKDIR /app
COPY . /app

# Instalamos dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]

