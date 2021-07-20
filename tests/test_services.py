import requests

PING_URL = "http://localhost:8080/api/v1/ping"
RECEIVER_URL = "http://ReceiverService:8080/api/v1/info"
HEALTH_URL = "http://localhost:8080/health"
RECEIVER_URL_OUTSIDE = "http://localhost:8081/api/v1/info"

def test_integrated_output():

    response = requests.post(PING_URL, json={
        'url':RECEIVER_URL
    })
    assert response.json() == {"Receiver": "Cisco is the best!"}

def test_status_code_ping():
    response = requests.post(PING_URL, json={
        'url':RECEIVER_URL
    })
    assert response.status_code == 200

def test_health():
    response = requests.get(HEALTH_URL)
    assert response.json()['status'] == 'healthy'

def test_receiver():
    response = requests.get(RECEIVER_URL_OUTSIDE)
    assert response.json() == {"Receiver": "Cisco is the best!"}



