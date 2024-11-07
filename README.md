## PARA RODAR O TESTE

na raiz do projeto com o docker instalado em sua maquina rode o comando:
````
docker-compose up 
````

## ACESSE O LINK DA APLICACAO COM A URL ABAIXO PARA TER ACESSO A TODAS AS REQUESTS DA APLICACAO.
````
http://localhost:8000/docs#/
````


## Crie o usuario no endpoint:

````
curl -X 'POST' \
  'http://localhost:8000/api/v1/users/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "administrador@tivit.com",
  "password": "123Mudar",
  "full_name": "administrador"
}'
````

## LIBERANDO O ACESSO AS REQUESTS ( AUTHORIZE )

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