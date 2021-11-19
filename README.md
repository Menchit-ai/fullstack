# FullStack Project : Powered AI

## Project presentation

The main idea of the project is to make a quiz site based on artificial intelligence, where users will have to guess if a text was written by a human or an AI. The principle of the site is collaborative, users can therefore connect to write their text and submit it to the site, text which will be offered to other users in the quiz section.

## Installation

To run this project you will just need to have docker installed and to clone this project. Then up the application with docker and go to the url of the frontend :

```bash
git clone https://github.com/Menchit-ai/fullstack
docker compose up
start http://localhost:8085
```

Wait for the backend to start, kong is configured by the backend.When all is prepared you should see the line **Uvicorn running on http://0.0.0.0:8005 (Press CTRL+C to quit)**.

## Generalities

The first query will take approximately 40 seconds to be responded. This is because kong needs to write in the database. The next query should not take that long. A weird comportement is that if you stop making request for too long, the next requestwill take approximately 20 seconds.

3 minutes after the application started, the AI will connect to the db and check how many humans' texts are present. It will then completeso there is exactly the same number of humans' texts and ai's texts. The ai is heavy and creating a single text could be pretty long. This completion will occure every 10 minutes. Due to pc limitation, kong could be long when the ai is computing new texts, if a query does not resolveor result with a 404 not found, maybe it is juste the computer that is strugling. If this is a problem you can shutdown the container with the aiby typing :

```bash
docker compose rm -s -v gpt2
```

The application starts with 3 texts from human's hand and with 2 precreated account. The 3 texts will be associated with the two users.This means that the ai should start to create 3 new texts and add them to the database.

## Technology

This project make use of several technologies list below :

- Docker
- PostgreSQL
- Fastapi
- Vuejs
- Kong
- Keycloak
- GPT-2

### Docker

Docker is used to launch all the necessary resources of the project : the backend made with FastAPI, the frontend made with Vue, the database PostgreSQL, Kong the API Gateway and GPT-2 which is the text AI used for the quiz.

### FastAPI



## Limits

Normally, the frontend should be accessible pathing by kong. But due to compilations and project organisations' infos that I don't have, I didn't success to load the Vue components in browser. So the frontend is only accessible through itself. This mean that when the front access the back and if the oidc plugin is used, he is blocked by cors policy. I didn't find a workaround so I decided to not use keycloak. Keycloak works, it's database is update if a user is created but the users are just not redirected on it (because I have comment the line that put the oidc plugin in kong).
