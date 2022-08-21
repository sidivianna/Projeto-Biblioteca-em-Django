# Projeto-Biblioteca-em-Django
Projeto de um site para gestão de uma biblioteca.


## Aula 2:

### Modelar o banco de dados:

- Criar a url base nas urls.py do projeto;
- Criar uma url.py no app livro
- Criar a função na pasta views.py;
- Criação do banco de dados na pasta models;

- Nos settings adicionar o aplicativo livro;
Na pasta models:
Criar as variáveis de classe: (colunas no banco de dados(nome, autor, etc)

Comando: 
python .\manage.py makemigrations
python .\manage.py migrate

criar conta para a area administrativa:
user: admin
senha: 01234	

Registrando a model Livro na area administrativa.
Criando as entradas de registros das informações do livros na área administrativa. (nome, autor, data, etc.) 
