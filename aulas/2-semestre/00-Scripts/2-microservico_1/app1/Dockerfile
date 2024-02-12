FROM node:latest

RUN npm install -g json-server

RUN echo '{"carros":[{"id":1,"marca":"gm","modelo":"corsa"},{"id":2,"marca":"ford","modelo":"fiesta"}]}' > /tmp/base.json

ENTRYPOINT ["json-server", "--port", "8080", "--host", "0.0.0.0"]

CMD ["/tmp/base.json"]