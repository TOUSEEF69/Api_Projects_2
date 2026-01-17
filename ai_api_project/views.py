from django.http import JsonResponse # type: ignore

def home(request):
    return JsonResponse({
        "message": "AI API is running",
        "endpoints": {
            "OpenCV Pencil Sketch": "/model1/predict/",
            "MobileNetV2": "/model2/predict/"
        }
    })
