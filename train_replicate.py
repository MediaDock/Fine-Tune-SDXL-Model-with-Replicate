#Pip install the replicate library before you start
import replicate
import os

#You need to create and name a API token on your Replicate account. This will generate a unique ID number/string.

os.environ["REPLICATE_API_TOKEN"]="<TOKEN NUMBER>" #ID number/string of the generated Replicate token

training = replicate.trainings.create(
    model="stability-ai/sdxl",
    version="39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
    input={
      "input_images": "<https://server.com/dataset.zip>", #Link to your dataset (.zip file on a server)
      "token_string": "<TOKEN>", #Name of token
      "caption_prefix": "a photo of <TOKEN>", #Default description of image
      "max_train_steps": 1000,
      "use_face_detection_instead": False #Toggle face recocnition on (True) if working with images of faces
    },
    #You need to create a model on your Replicate account that will be the destination for the trained version.
    destination="<username/modelname>" #"Path", name of user and model
)
