# GLP-Group-1-21
Group 1 GLP hackathon project 2021

## Backend Docker Image
Build from the container
```
docker build -t semfeed-flask:latest .
```
Then run the container and bind to port 
```
docker run -d -p <port>:<port> semfeed-flask
```

To interact inside the container
```
docker exec -it semfeed-latest
```