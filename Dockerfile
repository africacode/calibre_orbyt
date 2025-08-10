FROM python:3.11-slim

# Instalamos dependencias necesarias para calibre
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    libegl1 \
    libopengl0 \
    libxcb-cursor0 \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

# Instalamos calibre
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
