
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "src/saludtech/api/notificador.py", "run", "--host=0.0.0.0"]