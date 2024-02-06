FROM node:current-alpine3.19
WORKDIR app
COPY . .
RUN npm i
EXPOSE 3000
ENTRYPOINT [ "npm", "start" ]