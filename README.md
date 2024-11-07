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

## Ou crie os usuarios rodando manualmente usando os SQL Abaixo:
````
INSERT INTO public."user" (id, email, is_active, is_superuser, hashed_password) VALUES
    ('f9a7bfa6-0b58-4a72-9a2e-e4ecce7b7b6a', 'admin@tivit.com', TRUE, TRUE, '$2b$12$0Qt/56.z1HdbGV7O0dzZneI3rVsn0q.V8ny5.q0VduzD5FGh9Tz7u'),
    ('bb1f3f9a-11b8-40e3-8adf-51dffaf81d1d', 'user@tivit.com', TRUE, FALSE, '$2b$12$kCm0s6F5kD54l1EJl55d3uEZcNdkjwUnTY9mF5r8Yh.c.WP0ll3AW');
````




