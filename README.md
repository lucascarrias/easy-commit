# Easy Commit

Script criado para facilitar a vida de quem é novato no Git e automatizar o processo de commits simples.

### Disclaimer:
> Este projeto não tem o propósito de substituir as fucionalidades dos comandos do git 
> e tampouco deve ser utilizado em projetos de maior complexidade ou que precisam do uso de branches.

Use este projeto para se familiarizar com as vantagens do Git e agilizar os commits/pushes em projetos simples.

## O que o script faz:
* Verifica se o git já foi iniciado no diretório e inicia ele;
* Verifica a existência do .gitignore e adiciona o arquivo do script nele;
* Adiciona os arquivos/diretórios e faz o commit de acordo com a mensagem do usuário;
* Verifica a existência de um reposítório remoto e cria ele de acordo com o link fornecido;
* Faz o commit na master e salva as credenciais do usuário em cache por 2 horas;


## Como utilizar:
Mova o script para o diretório do seu projeto, abra o terminal no mesmo diretório e digite o comando:
> python easy_commit.py


### Requisitos:
* Sistema operacional Linux;
* Python 3;
* Git instalado;

## Melhoras possíveis:
Além das inúmeras e evidentes implementações que este projeto pode ter, algumas estão mais em vista:
* Deixar compatível com outros sistemas operacionais;
* Melhor tratamento de exceções e validação dos dados;
* Fazer o commit e push com apenas uma linha de comando;
* Melhorar a interface do menu;
* Adicionar e melhorar as mensagens ao usuário;
* Adicionar funcionalidade de gerar o README.md automaticamente com um template;
* Verificar se houve modificações no reposítório remoto antes de fazer um commit;



#### Sinta-se à vontade para deixar o seu feedback ou sugerir mudanças! ^^
