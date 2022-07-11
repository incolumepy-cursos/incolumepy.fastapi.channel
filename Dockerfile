FROM python:3.10.5-slim-bullseye

WORKDIR /app

COPY .requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app/

CMD ["uvicorn", 'main:app', '--host', '0.0.0.0', '--port', '80']
