FROM python:3.11-slim

# Instalar dependencias necesarias para Calibre y Python
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget curl xz-utils \
        libegl1 libopengl0 libxcb-cursor0 libxrender1 libxi6 libxcomposite1 libxrandr2 \
        libxdamage1 libxfixes3 libxkbcommon0 libxkbcommon-x11-0 libglib2.0-0 libfreetype6 \
        libfontconfig1 libharfbuzz0b libfribidi0 libjpeg62-turbo libnss3 libnspr4 \
        libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libasound2 libpng16-16 libx11-6 \
        libxext6 libxau6 libxdmcp6 zlib1g libbz2-1.0 libexpat1 libuuid1 libgl1 \
    && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin \
    && apt-get purge -y wget curl xz-utils \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Instalar Calibre
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

# Crear carpeta de trabajo
WORKDIR /app

# Copiar código del repositorio
COPY . .

# Crear carpeta para salidas
RUN mkdir -p /app/output

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Usar start.sh si existe, si no, ejecutar main.py
CMD ["bash", "-c", "if [ -f start.sh ]; then bash start.sh; else python main.py; fi"]

