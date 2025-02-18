FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

# 暴露端口
EXPOSE 11434

#CMD [ "python", "./main.py" ]
