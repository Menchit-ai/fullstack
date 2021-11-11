CREATE DATABASE backend;
CREATE DATABASE keycloakdb;
CREATE DATABASE kongdb;

CREATE USER keycloak WITH PASSWORD 'keycloak';
CREATE USER usr_backend WITH PASSWORD 'pwd_backend';
CREATE USER usr_kong WITH PASSWORD 'pwd_kong';

GRANT ALL PRIVILEGES ON DATABASE backend TO usr_backend;
GRANT ALL PRIVILEGES ON DATABASE keycloakdb TO keycloak;
GRANT ALL PRIVILEGES ON DATABASE kongdb TO usr_kong;

\c keycloakdb;
CREATE SCHEMA keycloak_schema;
GRANT ALL PRIVILEGES ON SCHEMA keycloak_schema TO keycloak;