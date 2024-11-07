## PARA RODAR O TESTE

na raiz do projeto com o docker instalado em sua maquina rode o comando:

Liberando o network public:
````
docker network create traefik-public
````

Subindo a aplicação.
````
docker-compose up 
````

## ACESSE O LINK DA APLICACAO COM A URL ABAIXO PARA TER ACESSO A TODAS AS REQUESTS DA APLICACAO.
````
http://localhost:8000/docs#/
````


## Crie o usuario do tipo não admin pelo endpoint:

````
curl -X 'POST' \
  'http://localhost:8000/api/v1/users/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "user@tivit.com",
  "password": "123Mudar",
  "full_name": "user"
}'
````

## Mudando o usuário para para o perfil admin.
Acesse a base de dados e dentro dela deixe como verdadeiro a coluna do banco de nome is_superuser para
que o usuario criado na request vire do tipo admim.

## LIBERANDO O ACESSO AS REQUESTS ( AUTHORIZE ) APENAS USUÁRIOS DO TIPO ADMIN PODEM!

Com o usurio e senha ja criados, va ate o cadeado do swagger da aplicacao do lado direito superior e preencha os campos 
usuario e senha, caso tudo de ceto algo como os dados abaixo serao apresentados:

OAuth2PasswordBearer (OAuth2, password)
Authorized
Token URL: /api/v1/login/access-token

Flow: password

username: user@example.com
password: ******
Client credentials location: basic
client_secret: ******

( AGORA VOCE TEM ACESSO A TODAS AS REQUISICOES DA APLICACAO QUE ANTES NAO ESTAVAM PERMITIDAS )