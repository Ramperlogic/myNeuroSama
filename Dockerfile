FROM python:3.13-slim
FROM mcr.microsoft.com/vs/visualstudio/2019/preview/win10-amd64

ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./

RUN msbuild /p:Configuration=Release /p:Platform=x64 MyApplication.sln
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

# 暴露端口
EXPOSE 11434

#CMD [ "python", "./main.py" ]
