import os

import io

import re

#import espeak

# [START vision_face_detection]



"""Detects faces in an image."""

from google.cloud import vision
client = vision.ImageAnnotatorClient()



    # [START vision_python_migration_face_detection]

    # [START vision_python_migration_image_file]
file_name=os.path.join(
    os.path.dirname(__file__),
    'girl.jpg')
    
with io.open(file_name, 'rb') as image_file:

    content = image_file.read()



image = vision.types.Image(content=content)

    # [END vision_python_migration_image_file]



response = client.face_detection(image=image)

faces = response.face_annotations



    # Names of likelihood from google.cloud.vision.enums

likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',

                       'LIKELY', 'VERY_LIKELY')

print('Faces:')



for face in faces:
    
    if((likelihood_name[face.anger_likelihood]=='VERY_LIKELY')|(likelihood_name[face.anger_likelihood]=='LIKELY')):
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))

    
    elif((likelihood_name[face.joy_likelihood]=='VERY_LIKELY')|(likelihood_name[face.joy_likelihood]=='LIKELY')):
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))

    
    elif((likelihood_name[face.surprise_likelihood]=='VERY_LIKELY')|(likelihood_name[face.surprise_likelihood]=='LIKELY')):
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))


    
    #print('anger: {}'.format(likelihood_name[face.anger_likelihood]))

    #print('joy: {}'.format(likelihood_name[face.joy_likelihood]))

    #print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))


    vertices = (['({},{})'.format(vertex.x, vertex.y)

for vertex in face.bounding_poly.vertices])

    print('face bounds: {}'.format(','.join(vertices)))


if((likelihood_name=='VERY_LIKELY')|(likelihood_name=='LIKELY')):
    print('anger: {}'.format(likelihood_name[face.anger_likelihood]))

    # [END vision_python_migration_face_detection]

# [END vision_face_detection]


