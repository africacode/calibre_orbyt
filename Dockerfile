FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget curl xz-utils \
    libegl1 libopengl0 libxcb-cursor0 libxrender1 libxi6 libxcomposite1 libxrandr2 \
    libxdamage1 libxfixes3 libxkbcommon0 libxkbcommon-x11-0 libglib2.0-0 libfreetype6 \
    libfontconfig1 libharfbuzz0b libfribidi0 libjpeg62-turbo libnss3 libnspr4 \
    libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libasound2 libpng16-16 libx11-6 \
    libxext6 libxau6 libxdmcp6 zlib1g libbz2-1.0 libexpat1 libuuid1 \
    && rm -rf /var/lib/apt/lists/*

RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

WORKDIR /app

# Copia todo el código
COPY . /app

# Copia las recetas a la carpeta por defecto de calibre para recetas
RUN mkdir -p /root/.config/calibre/recipes/
COPY recipes/*.recipe /root/.config/calibre/recipes/

# Crea carpeta output (donde guardar los pdf/epub)
RUN mkdir -p /app/output

CMD ["python", "run_calibre.py"]
