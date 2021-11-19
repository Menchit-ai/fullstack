# Powered AI

```bash
docker compose up
```

Wait for the backend to start, kong is configured by the backend.

The first query will take approximately 40 seconds to be responded. This is because kong needs to write in the database.
The next query should not take that long. A weird comportement is that if you stop making request for too long, the next request
will take approximately 20 seconds.

3 minutes after the application started, the AI will connect to the db and check how many humans' texts are present. It will then complete
so there is exactly the same number of humans' texts and ai's texts. The ai is heavy and creating a single text could be pretty long.
This completion will occure every 10 minutes.

The application starts with 3 texts from human's hand and with 2 precreated account. The 3 texts will be associated with the two users.
This means that the ai should start to create 3 new texts and add them to the database.
