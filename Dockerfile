FROM library/python:3.7-alpine

LABEL maintainer=""

# Set Time Zone for Docker Container
# https://serverfault.com/a/683651
# RUN apk add --no-cache tzdata
# ENV TZ Europe/Oslo

WORKDIR /app/

COPY app.py requirements.txt /app/

RUN pip3 install --requirement requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
