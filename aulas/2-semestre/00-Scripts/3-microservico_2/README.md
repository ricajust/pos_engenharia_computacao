## Disciplina Microsserviços - Aula 02

Digitar no terminal

```bash

# Pré-requisitos instalação do LocalStack
# 1. LocalStack CLI
# 2. LocalStack Web Application account e Auth Token
# 3. Docker
# 4. Python 3.9+ e pip
# 5. AWS CLI e awslocal wrapper
# 6. jq, zip e curl

# 1. LocalStack CLI (fonte https://docs.localstack.cloud/getting-started/installation/#localstack-cli)

# Windows
# Executar o Powershell em modo Administrador

# Baixar o arquivo do localstack
Invoke-WebRequest -Uri "https://github.com/localstack/localstack-cli/releases/download/v3.1.0/localstack-cli-3.1.0-windows-amd64-onefile.zip" -OutFile "$env:TEMP\localstack-cli.zip"

# Extrair o arquivo ZIP
Expand-Archive -Path "$env:TEMP\localstack-cli.zip" -DestinationPath "$env:TEMP" -Force

# Mover o arquivo para o destino final
Move-Item -Path "$env:TEMP\localstack.exe" -Destination C:\Windows\System32\localstack.exe -Force

# Limpar os arquivos temporários
Remove-Item -Path "$env:TEMP\localstack-cli.zip" -Force

# Verificar se o LocalStack CLI foi instalado corretamente
localstack --version

# Resposta do comando
3.1.0

# Extrair o arquivo ZIP e executar via Powershell
# Verificar se o LocalStack CLI foi instalado corretamente
localstack --version

# Resposta do comando
3.1.0

# Linux
curl -Lo localstack-cli-3.1.0-linux-amd64-onefile.tar.gz \
    https://github.com/localstack/localstack-cli/releases/download/v3.1.0/localstack-cli-3.1.0-linux-amd64-onefile.tar.gz

# Extrair o LocalStack CLI
sudo tar xvzf localstack-cli-3.1.0-linux-*-onefile.tar.gz -C /usr/local/bin

# ou alternativa via Brew
brew install localstack/tap/localstack-cli

# MacOS
brew install localstack/tap/localstack-cli

# ou alternativa Binary Download
curl -Lo localstack-cli-3.1.0-darwin-amd64-onefile.tar.gz \
    https://github.com/localstack/localstack-cli/releases/download/v3.1.0/localstack-cli-3.1.0-darwin-amd64-onefile.tar.gz

# Extrair o LocalStack CLI
sudo tar xvzf localstack-cli-3.1.0-darwin-*-onefile.tar.gz -C /usr/local/bin

# Verificar se o LocalStack CLI foi instalado corretamente
localstack --version

# Resposta do comando
3.1.0

# 2. LocalStack Web Application account e Auth Token

# Acessar o endereço https://app.localstack.cloud/sign-up
# Efetuar o cadastro
# Acessar o menu Subscription, selecionar a opção ADD NEW PLAN, no canto superior direito da tela
# Selecionar o plano FREE TRIAL
# Acessar o menu AUTH TOKEN e copiar o valor
# Voltar a linha de comando (CLI) do seu sistema operacional e definir a variável de ambiente

# Windows
$env:LOCALSTACK_AUTH_TOKEN=<auth-token-copiado> # Antes
$env:<auth-token-copiado> #Depois

# Linux/MacOS
export LOCALSTACK_AUTH_TOKEN=<auth-token-copiado>
export ACTIVATE_PRO=0

# 3. Docker

# Acessar o endereço https://docs.docker.com/get-docker/ e seguir os passos de instalação para seu sistema operacional

# 4. Python 3.9+ e pip

# Acessar o endereço https://www.python.org/downloads/ e seguir os passos de instalação para seu sistema operacional 

# 5. AWS CLI e awslocal wrapper

# AWS CLI: Acessar o endereço https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html e seguir os passos de instalação para seu sistema operacional 

# awslocal wrapper: Acessar o endereço https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal e seguir os passos de instalação. O comando é o mesmo para todos os sistemas operacionais
pip install awscli-local[ver1]

# Instalar via sudo no Linux:
sudo pip3 install awscli-local[ver1]

# 6. jq, zip e curl

# jq
# jq Windows
# run this curl in your gitbash as ADMIN
curl -L -o /usr/bin/jq.exe https://github.com/stedolan/jq/releases/latest/download/jq-win64.exe

# or manually save the jq-win64.exe in link above as jq.exe to your /usr/bin (which is in your git bash installation folder)

# Linux ou MacOS via Brew
brew install jq

# Linux Debian-based (por exemplo Ubuntu)
sudo apt-get install jq

# Linux RPM-based (por exemplo CentOS)
sudo yum install jq

# Verificar se o jq foi instalado corretamente
jq --version

# verificar se o cUrl está disponível, senão faça a instalação
curl --version

# verificar se o ZIP está disponível, senão faça a instalação
zip

# Exercício 01
# https://docs.localstack.cloud/getting-started/quickstart/

# A aplicação faz o redimensionamento de imagens através de tecnologias Serverless (sem Servidor), usando os serviços da AWS S3 (armazenamento de objetos), AWS SSM (Systems Manager para armazenamento de configurações), Lambda (funções executadas na nuvem sem servidor), SNS e SES. A aplicação possui uma função Lambda que cria URLs pré-assinadas para uplodas diretos e a funcionalidade S3 bucket notifications dispara a função de redimensionamento de imagem. Outra função Lambda lista e entrega URLs pré-assinadas para exibição no navegador. A aplicação também gerencia falhas nas funções Lambda através do serviço SNS e notificações via e-mail através do serviço SES.

# Clonar a aplicação de exemplo do repositório no Github
git clone https://github.com/localstack-samples/sample-serverless-image-resizer-s3-lambda.git

# Acessar a pasta
cd sample-serverless-image-resizer-s3-lambda

# Criar um ambiente virtual Python. Verifique a versão, talvez seja necessário mudar o comando python para python3

# Windows
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt

# macOS/Linux
python -m venv .venv

# Nota 2: Caso encontre algum problema na criação do ambiente virtual Python, instale o python3.10-venv e tente novamente
sudo apt install python3.10-venv

source .venv/bin/activate
pip install -r requirements-dev.txt

# Nota: Caso encontrar problemas com a instalação dos pacotes (por exemplo Pillow), garantir o uso da mesma versão para Python Lambdas (3.9) e pacote Pillow. Caso use pyenv, instalar e ativar o Python 3.9 com o seguintes comandos:
pyenv install 3.9.0
pyenv global 3.9.0



# Iniciar a infraestrutura local
localstack start

# Abrir um novo Terminal
cd sample-serverless-image-resizer-s3-lambda

# Configurar e executar a aplicação serverless image resizer
bin/deploy.sh

# Recuperar e anotar as URLs das funções Lambda
awslocal lambda list-function-url-configs --function-name presign | jq -r '.FunctionUrlConfigs[0].FunctionUrl'
awslocal lambda list-function-url-configs --function-name list | jq -r '.FunctionUrlConfigs[0].FunctionUrl'

# Executar a aplicação no navegador
https://webapp.s3-website.localhost.localstack.cloud:4566

# Colar as funções Lambda de pré-assinatura e listagem de URLs nos respectivos campos da aplicação e clique no botão Apply. Alternativamente, clique no botão Load from API para carregar automaticamente as URLs 

# Fazer o upload de uma imagem para testes e clique no botão Upload

# Se tudo funcionar, a aplicação retornará uma mensagem de sucesso

# Remover a infraestrutura local
localstack stop
