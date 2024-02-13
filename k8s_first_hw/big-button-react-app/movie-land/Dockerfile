FROM node:16.20.2-alpine3.18

WORKDIR /app

COPY package*.json ./
RUN npm i

COPY public public
COPY src src

EXPOSE 3000

USER root

CMD [ "npm","start" ]