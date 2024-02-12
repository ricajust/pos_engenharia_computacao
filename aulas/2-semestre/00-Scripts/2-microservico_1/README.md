## Disciplina Microsserviços - Aula 01 - Simulação de REST APIs

### Pasta raíz de todos os códigos: app1

Digitar no terminal

```bash

# verificar se o cUrl está disponível, senão faça a instalação
curl --version

# verificar se o docker foi devidamente instalado, senão faça a instalação
docker

# descompactar arquivo app1.zip (verifique se seu sistema operacional possui o aplicativo ZIP instalado, normalmente)
unzip app1.zip

# acessar pasta app1
cd app1

# criar a imagem do container
docker build -t jsonserver .

# executar o container
# -d    Roda o container em background e exibe o ID do container
# –rm	Remove o container quando ele é encerrado
# -it   Inicia o modo interativo, acessa o terminal docker container via linha de comando
docker run -d --rm -it --name jsonserver-container -p 8080:8080 jsonserver

# acessar JSON-server, via navegador de sua preferência para acompanhar resultados
# Via navegador, acessar o endereço http://localhost:8080/

# testar chamada GET via linha de comando LINUX/MacOS
# utilize 127.0.0.1, caso localhost ou 0.0.0.0 não funcione
curl -X GET http://0.0.0.0:8080/carros

#ou
curl http://0.0.0.0:8080/carros

#ou Windows (cmd)
curl http://localhost:8080/carros 

#ou
curl -X GET http://localhost:8080/carros



# carregar mais dados através do arquivo carros.json
# Na pasta app1, verificar se o arquivo carros.json está disponível (LINUX/MacOS)
ls -l carros.json

# ou Windows (cmd)
dir carros.json

# copiar o arquivo carros.json para o container na pasta temp com o nome base.json 
docker cp carros.json jsonserver-container:tmp/base.json

# listar o container ativo e anotar o container ID
docker ps

# reiniciar o container, adicionando o container ID
docker restart `ID_DO_CONTAINER`

# ou reiniciar via nome do container
docker restart jsonserver-container

# Testar chamada POST via linha de comando LINUX/MacOS
curl -i -H "Accept: application/json" -H "Content-type: application/json" -X POST http://0.0.0.0:8080/carros -d '{"id":"9","marca":"audi","modelo":"q7"}'

# ou Windows (cmd)
curl -i -H "Accept: application/json" -H "Content-type: application/json" -X POST http://localhost:8080/carros -d '{\"id\":\"9\",\"marca\":\"audi\",\"modelo\":\"q7\"}'

# Testar chamada PUT via linha de comando LINUX/MacOS
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X PUT http://0.0.0.0:8080/carros/9 -d '{"id":"9","marca":"bmw","modelo":"x1"}'

# ou Windows (cmd)
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X PUT http://localhost:8080/carros/9 -d '{\"id\":\"9\",\"marca\":\"bmw\",\"modelo\":\"x1\"}'

# Testar chamada PATCH via linha de comando LINUX/MacOS
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X PATCH http://0.0.0.0:8080/carros/9 -d '{"id":"9","modelo":"x2"}'

# ou Windows (cmd)
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X PATCH http://localhost:8080/carros/9 -d '{\"id\":\"9\",\"marca\":\"bmw\",\"modelo\":\"x2\"}'

# Testar chamada DELETE via linha de comando LINUX/MacOS
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X DELETE http://0.0.0.0:8080/carros/9

# ou Windows (cmd)
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X DELETE http://localhost:8080/carros/9
