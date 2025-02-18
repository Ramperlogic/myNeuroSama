FROM python:3.13-slim

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app
COPY . /app

# 暴露端口
EXPOSE 8000

CMD [ "python", "./main.py" ]
