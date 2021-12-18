FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY /Kollec /app

CMD ["gunicorn", "--bind", "0.0.0.0", "-p", "8000", "kollec.wsgi"]