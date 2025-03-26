FROM python:3.13-slim
FROM mcr.microsoft.com/vs/visualstudio/2019/preview/win10-amd64

ENV PYTHONUNBUFFERED=1

COPY src/requirements.txt ./

RUN msbuild /p:Configuration=Release /p:Platform=x64 MyApplication.sln
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src/ /app
WORKDIR /app

EXPOSE 11434

#CMD [ "python", "./main.py" ]
