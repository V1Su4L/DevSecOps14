FROM python:3.10-alpine3.13
WORKDIR /app
COPY requirements.txt .
RUN apk add py3-pip
RUN apk add postgresql
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3","app.py" ]
