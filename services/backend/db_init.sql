CREATE DATABASE backend;
CREATE DATABASE keycloakdb;

CREATE USER keycloak WITH PASSWORD 'keycloak';
CREATE USER usr_backend WITH PASSWORD 'pwd_backend';

GRANT ALL PRIVILEGES ON DATABASE backend TO usr_backend;
GRANT ALL PRIVILEGES ON DATABASE keycloakdb TO keycloak;

\c keycloakdb;
CREATE SCHEMA keycloak_schema;
GRANT ALL PRIVILEGES ON SCHEMA keycloak_schema TO keycloak;