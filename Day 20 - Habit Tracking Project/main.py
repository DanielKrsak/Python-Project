import requests
import datetime as dt

today = dt.datetime.now()


USERNAME = "kikina"
TOKEN = "aoiuhfaoinQr0fqih!"
GRAPH_ID = "graph1"
ADJUSTED_DATE = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{ADJUSTED_DATE}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Kikina Gym",
    "unit": "minute",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN

}

post_pixela_graph_params = {
    "date": ADJUSTED_DATE,
    "quantity": "10"
}

put_pixela_params = {
    "quantity": "5",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# graph_response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
# post_pixela_response = requests.post(url=post_pixel_endpoint, json=post_pixela_graph_params, headers=headers)

adjusted_response = requests.put(url=put_pixel_endpoint, json=put_pixela_params, headers=headers)


