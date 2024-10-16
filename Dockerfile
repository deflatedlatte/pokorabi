FROM python:3.11.10-bookworm

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY src /app/src/
WORKDIR /app/src

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
