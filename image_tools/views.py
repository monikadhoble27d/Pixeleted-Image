# views.py

from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .util import *

def process_image_api(request):
    if request.method == 'POST' and request.FILES['image']:
        print('Processing image...')
        uploaded_image = request.FILES['image']
        image_path = default_storage.save('uploaded_image.png', ContentFile(uploaded_image.read()))
        image = Image.open(default_storage.open(image_path))

        # sobel_result = sobel_edge_detection(image)
        # sobel_result_path = default_storage.save('sobel_result.png', ContentFile(sobel_result))
        # frequency_result = frequency_analysis(image)
        lbp_result = local_binary_pattern(image)
        wiener_result = wiener_filter(image)

        context = {
            'uploaded_image': image_path,
            # 'sobel_result': sobel_result_path,
            # 'frequency_result': frequency_result_path,
            'lbp_result': lbp_result,
            'wiener_result': wiener_result,
        }

        return render(request, 'process_result.html', context)

    return render(request, 'upload_image.html')
