FROM node:14.16.0-alpine3.13
WORKDIR /app
COPY package* .
RUN npm i
# RUN chown -R node:node /app
COPY . .
EXPOSE 3000
RUN chmod o-r package*.json
USER node:node
CMD [ "npm","start" ]
