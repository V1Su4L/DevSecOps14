FROM python:3-alpine3.12

WORKDIR /app

COPY *.txt .
RUN pip3 install -r requirments.txt

COPY movies.py .

EXPOSE 80

CMD python3 movies.py