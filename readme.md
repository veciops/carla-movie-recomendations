# Smartphone Recommender
The project developed to hit a partial note on the discipline of Artificial Intelligence.

### Project structure
The project is organized of the following form:

### API
An API responsible by returning a list of recommendations and a list of filters to be used on 
the client application.

The API contains the following routes:

##### /recommendations
This route returns a list of recommendations based on a list of informed filters on query string
params. Below, an example of a query string is informed.

Method: GET
Params:

* cpu=Snapdragon 855
* storage-capacity=128 GB
* removable-storage=No
* ram=6 GB
* os=Android 8.1 "Oreo"
* battery=3500mAh
* display=6.41" 2340x1080 AMOLED
* camera=Dual 12 MP + 13 MP (rear camera) 24.8 MP (front camera)
* fingerprint-scanner=Under screen
* facial-recognition=Yes

##### /filters
This route returns the filters that the client application go show to allow that the user can select
yours preferences.

Method: GET
Params: No params is needed

### Recommender

### Client Application
# carla-movie-recomendations
