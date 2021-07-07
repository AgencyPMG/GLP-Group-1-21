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
make up
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

**Note:**
To load weights for the Language Model you must have the following file structure
```
src/
|_backend/
|__model/
|___label_encoder.pickle
|___tokenizer.pickle
|___language_model_weights.index
|___language_model_weights.data
```
To create the files for the model you can run 
```
python src/train/train_LM.py
```
