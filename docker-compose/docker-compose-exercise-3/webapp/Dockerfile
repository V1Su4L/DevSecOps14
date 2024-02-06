FROM python:3.9.18-alpine3.19
WORKDIR /app
COPY requirements.txt .
RUN apk add py3-pip
RUN apk add mariadb-dev build-base
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
ENV YSQL_ROOT_PASSWORD=movie123
ENV MYSQL_HOME=mysql://root:movie123@database:3306/movies
COPY . .
EXPOSE 80
CMD [ "python3","server.py" ]
