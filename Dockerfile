FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

# 安装编译工具链和依赖库
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libopenblas-dev \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

COPY src/requirements.txt ./

# 升级pip并安装依赖
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY src/ /app
WORKDIR /app

EXPOSE 11434

#CMD [ "python", "./main.py" ]
