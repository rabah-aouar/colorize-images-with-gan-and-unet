import uuid
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image
import os
from .colorization.demo_release import colorize
import matplotlib.pyplot as plt 
import numpy as np 

@api_view(['POST'])
def grayscale_image(request):
    image_file = request.FILES['image']
    # Open the uploaded image
    image = Image.open(image_file)
    filename = str(uuid.uuid4()) + '.jpg'
    path = os.path.join(settings.MEDIA_ROOT, 'images', filename)
    image.save(path)
    
    # Convert to grayscale
    colorized_image= colorize(path)

    plt.imsave(os.path.join(settings.MEDIA_ROOT, 'col-images', filename), colorized_image)
    # Construct the full URL of the saved image
    url = request.build_absolute_uri(settings.MEDIA_URL + 'col-images/' + filename)
    # Return the URL in the response
    return Response({'url': url}, status=status.HTTP_201_CREATED)