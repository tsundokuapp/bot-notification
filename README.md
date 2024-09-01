# Bot de notificações no Discord
branch developer

# Instruções Para Dev
A versão do Python utilizada é: python:3.10

* Para criar o ambiente, utilize: 
    python3 -m venv venv
    source venv/bin/activate

* Para instalar as dependencias do projeto:
    pip install -r requirements.txt

* Para executar os testes:
    pytest

# Para buildar a imagem com docker
A imagem utiliza volume, então é necessário criar um:
* docker volume create <nome-do-volume> 

Após isso, para criar a imagem:
* docker build -t bot-notif:<versao-do-bot> .

E por fim, para executar o container:
* docker run -d -v <nome-do-volume>:/home/project/assets bot-notif:<versao-do-bot>

Caso queira acompanhar a saida do bot, pode usar:
* docker attach <id-do-container>
Pode encontrar o id do container a partir do comando: docker ps