from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from django.core.files.storage import default_storage # type: ignore
from django.http import FileResponse # type: ignore
import cv2 # type: ignore
import os
from .utils import pencil_sketch

class PencilSketchView(APIView):
    def post(self, request):
        if 'image' not in request.FILES:
            return Response(
                {"error": "Image file is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        image = request.FILES['image']
        path = default_storage.save(image.name, image)
        full_path = default_storage.path(path)

        sketch = pencil_sketch(full_path)

        output_path = full_path.replace(".jpg", "_sketch.jpg")
        cv2.imwrite(output_path, sketch)

        return FileResponse(open(output_path, 'rb'), content_type='image/jpeg')
