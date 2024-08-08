FROM python:3.12.5-slim-bullseye

WORKDIR /app

RUN apt-get update -q && \
  apt-get install -y --no-install-recommends \
    python3-pip \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libpangoft2-1.0-0 && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app .

CMD ["fastapi", "run", "main.py", "--port", "8080"]
