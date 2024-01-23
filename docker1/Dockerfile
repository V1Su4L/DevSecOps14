FROM python:3.10.13-alpine3.19
WORKDIR app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python3","main.py" ]