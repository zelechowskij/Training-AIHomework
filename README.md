# This is a second task for Collabera recruitment

We have two services:
## PingService
1. ```/api/v1/ping```
Accepts POST requests containing a url key. It then sends a GET request to that endpoint, and returns recieved payload
2. ```/health```
Accepts GET requests, and returns simple health check
## RecieverService
1. ```/api/v1/info```
Accepts GET requests, returns a hardcoded dictionary 
```{"Receiver": "Cisco is the best!"}```

## Requirements
- Docker
- Git
- Python >= 3.8

## Steps to run these services in a Docker enviroinment
1. Clone the repository <br />
```git clone https://github.com/zelechowskij/Training-AIHomework.git && cd Training-AIHomework```<br />
2. Install requirements for testing <br />
```pip install -r requirements.txt```
3. Build and run services <br />
```docker compose up```

From here you can open another terminal in ```Training-AIHomework``` directory
- Test services using pytest <br />
```pytest```
- Test services using curl command <br />
 ```curl -X POST http://localhost:8080/api/v1/ping -H "Content-Type:application/json" -d '{"url":"http://ReceiverService:8080/api/v1/info"}'```<br />
 NOTE <br />
 if curl is not working make sure to copy it from here instead of task pdf :)

Also you can check health of PingerService with ```docker ps``` and look into ```status``` column
