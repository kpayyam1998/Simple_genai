FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt  --default-timeout=100 future

COPY . .

EXPOSE 8501

CMD ["steramlit","run","simple_bot.py"]


