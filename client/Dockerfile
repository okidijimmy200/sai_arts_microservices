FROM node:14-alpine3.10

WORKDIR /app
COPY package.json .
RUN npm i
COPY . .

# CMD ["sh","-c","npm run build && http-server"]
CMD ["sh","-c","npm run serve"]
