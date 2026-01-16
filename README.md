# CRUD básico com FastAPI

API Rest simples para gerenciamento de usuários, desenvolvida com FastAPI, PostegresSQL e Docker.
Desenvolvida para estudo simples de uma API Rest.

## Tecnologias

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker & Docker Compose

## Como rodar o projeto

Para rodar o projeto é necessário ter instalado o Docker e Docker Compose.

1. Clone o repositório:

git clone https://github.com/inacioiso/CRUD-basico.git
cd CRUD-basico

2.Crie o seu próprio arquivo .env:

cp .env.example .env

3.Suba os containers:

docker compose up --build

## Endpoints da API

| Método | Rota | Descrição |
|------|------|------|
| POST | `/users` | Criar usuário |
| GET | `/users` | Listar usuários |
| PUT | `/users/{id}` | Atualizar usuário |
| DELETE | `/users/{id}` | Remover usuário |

## Observações
- O banco de dados é inicializado via Docker Compose
- As tabelas são criadas via SQLAlchemy
- O volume do PostgreSQL garante persistência dos dados
