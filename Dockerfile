FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

COPY src/requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src/ /app
WORKDIR /app

EXPOSE 11434

#CMD [ "python", "./main.py" ]
