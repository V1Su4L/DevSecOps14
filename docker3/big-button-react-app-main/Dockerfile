FROM node:current-alpine3.19
WORKDIR /app
COPY . .
WORKDIR /run/movie-land
RUN npm install
EXPOSE 3000
CMD [ "npm","start" ]