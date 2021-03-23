from django.http import HttpResponse
from django.shortcuts import render
import os
import cv2
import numpy as np
import matplotlib.image as mpimg

ROOT_DIR = os.path.abspath("../")

def submit_image(request):
    
    if request.method=="POST":
        img= request.FILES['chesk_img']
        XML= request.FILES['xml_file']
        print(img)
        print(XML)
        img_name = img.name
        XML_name = XML.name
        
        with open(os.path.join(ROOT_DIR,'Dimensionless_Tech_Task/TASK/static',img_name), 'wb+') as destination:
            for chunk in img.chunks():
                    destination.write(chunk)
        with open(os.path.join(ROOT_DIR,'Dimensionless_Tech_Task/TASK/static',XML_name), 'wb+') as destination:
            for chunk in XML.chunks():
                    destination.write(chunk)
            img_path = '../static/{}'.format(img_name)
            XML_path = '../static/{}'.format(XML_name)
            predicted_class = prediction(img_path)
            return render(request,"index.html",{'predicted_class':predicted_class,"img_path":img_path,"XML_path":XML_path})
    return render(request,"index.html")
    
def prediction(img_name):
    
    image_path = os.path.join(ROOT_DIR,'Dimensionless_Tech_Task/TASK/static',img_name)
    
    bag_cascade = cv2.CascadeClassifier('P00X000-2019092701422.xml')
    
    return image_path


        
        






