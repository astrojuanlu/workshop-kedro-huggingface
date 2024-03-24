FROM gitpod/workspace-python-3.11:2024-03-20-07-19-19

RUN pyenv global 3.11.8 && pip install uv

RUN wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20231120224007.0.0_amd64.deb -O minio.deb \
    && sudo dpkg -i minio.deb

RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc \
    && chmod +x mc \
    && sudo mv mc /usr/local/bin/mc

RUN curl -fsSL https://ollama.com/install.sh | sh
