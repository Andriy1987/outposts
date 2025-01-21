FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git config --global --add safe.directory /log
RUN git config --global user.email "alavrinok@gmail.com" && \
    git config --global user.name "andriy1987"

WORKDIR /log

COPY parse_nginx_logs_new.py /log/

COPY nginx.log /log/nginx.log

ENTRYPOINT ["python", "parse_nginx_logs_new.py"]


# CMD ["python", "script.py", "--sort", "--filter"]

