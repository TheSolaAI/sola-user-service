FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libmagic-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv python-magic

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --ignore-pipfile

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
