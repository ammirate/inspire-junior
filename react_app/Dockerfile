FROM node:7.8.0

ENV NPM_CONFIG_LOGLEVEL warn

COPY . .

RUN npm run build

RUN npm install -g serve

CMD yarn start

EXPOSE 3000
