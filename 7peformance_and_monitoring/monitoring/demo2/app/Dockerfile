FROM python:3.11-slim


#install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# creating working dirctory in docker container
WORKDIR /app




COPY app/main.py .
COPY requirements.txt .

RUN uv pip install --system -r requirements.txt

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
