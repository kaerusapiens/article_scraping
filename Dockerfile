# Build stage
FROM python:3.9-slim

WORKDIR /app

# Layer cachingのため、 requirements.txtを先にコピーしてパッケージをインストールする
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/bash"]