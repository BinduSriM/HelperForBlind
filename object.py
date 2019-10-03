import io
import os
import cv2
cap = cv2.VideoCapture(0)



while(True):

    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)



    cv2.imshow('frame', rgb)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        out = cv2.imwrite('capture_obj.jpg', frame)

        break

cap.release()

cv2.destroyAllWindows()
from google.cloud import vision
client = vision.ImageAnnotatorClient()
file_name=os.path.join(
    os.path.dirname(__file__),
    'capture_obj.jpg')
file1=open("C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\myfile1.txt","w")
with open(file_name, 'rb') as image_file:
    content = image_file.read()
image = vision.types.Image(content=content)

objects = client.object_localization(
        image=image).localized_object_annotations

file1.write('Number of objects found: {}'.format(len(objects)))
for object_ in objects:
        if (object_.score)>=0.600000001:
         #if '\n{} (confidence: {})'.format(object_.name, object_.score)>=0.60:
             #object_.score=0
             file1.write('\n{})'.format(object_.name,object_.score,'.2f'))
        #print('\n{} (confidence: {})'.format(object_.name, object_.score))
        #print('Normalized bounding polygon vertices: ')
        #for vertex in object_.bounding_poly.normalized_vertices:
         #   print(' - ({}, {})'.format(vertex.x, vertex.y))

        
