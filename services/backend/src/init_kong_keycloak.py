import os

import requests
from keycloak import KeycloakAdmin

KONG_HOST_IP = os.environ["KONG_HOST_IP"]
KONG_PORT = os.environ["KONG_PORT"]



KEYCLOAK_HOST_IP = os.environ["KEYCLOAK_HOST"]
KEYCLOAK_PORT = os.environ["KEYCLOAK_PORT"]

KEYCLOAK_URL = os.environ["KEYCLOAK_URL"]
USERNAME = "admin"
PASSWORD = 'Pa55w0rd'
MASTER_REALM_NAME = "master"
REALM_NAME = "master"


keycloak_admin = KeycloakAdmin(
    server_url="http://keycloak:8080/auth/",
    username=USERNAME,
    password=PASSWORD,
    verify=True
)

# check if kong is already in keycloak's clients
kong_created = False
for client in keycloak_admin.get_clients():
    if client["name"] == "kong": kong_created = True

# adding kong to keycloak's clients
if not kong_created:
    keycloak_admin.create_client({
        "clientId":"kong",
        "name":"kong",
        "enabled": True,
        "redirectUris":[ "/front/*", "/api/*" ]
    })

# saving the id of kong
for client in keycloak_admin.get_clients():
    if client["name"] == "kong": kong_id = client["id"]

# storing kong's key as a client
kong_key = keycloak_admin.generate_client_secrets(kong_id)["value"]

introspection_url = f'http://{KEYCLOAK_HOST_IP}:{KEYCLOAK_PORT}/auth/realms/{REALM_NAME}/protocol/openid-connect/token/introspect'
discovery_url = f'http://{KEYCLOAK_HOST_IP}:{KEYCLOAK_PORT}/auth/realms/{REALM_NAME}/.well-known/openid-configuration'

# adding services for front and back with the OIDC plugin
services = [
    {
        'name': 'api_service',
        'url': 'http://backend:8005/',
        'path': "api"
    },
    {
        'name': "front_service",
        'url': f'http://frontend:8085/',
        'path': "front"
    }
]
print("Starting initialisation of kong")

for service in services:
    name = service["name"]
    if requests.get(f"http://{KONG_HOST_IP}:{KONG_PORT}/services/{name}").status_code == 404:
        response = requests.post(f"http://{KONG_HOST_IP}:{KONG_PORT}/services/",data = service)
        created_service_id = response.json()["id"]

        oidc_data = {
            'name': 'oidc',
            'config.client_id': f'{kong_id}',
            'config.client_secret': f'{kong_key}',
            'config.realm': f'{REALM_NAME}',
            'config.bearer_only': 'true',
            'config.introspection_endpoint':introspection_url,
            'config.discovery':discovery_url
        }
        requests.post(f'http://{KONG_HOST_IP}:{KONG_PORT}/services/{created_service_id}/plugins', data=oidc_data)

        print(name, "created !")

    else: print(name, "already exists !")

