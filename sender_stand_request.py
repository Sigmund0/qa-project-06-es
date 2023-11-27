import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_user(data.user_body);
token=response.json()["authToken"]
print(response.status_code)
print(response.json())
print(token)


def post_new_client_kit(kit_body, auth_token):
    headers=data.headers
    headers["Authorization"]="Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)



