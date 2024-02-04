FROM python:alpine3.19
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV PORT=5000
EXPOSE 4999
EXPOSE 8989
CMD [ "python3","main.py" ]