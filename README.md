# GLP-Group-1-21
Group 1 GLP hackathon project 2021

## Backend Management
The backend is exposed through a flask applicaiton that can be built from a docker file. 
To build the image, from the home directory run
```
make build
```
Once the docker image is built, a container can be run using
```
make run
```
To stop a running container use
```
make stop
```
If rebuilding an image, errors can sometime occur when trying to run a new container, since the old container still points to the image. If this happens, simply run
```
make clear
```
and from there rerun the container.
