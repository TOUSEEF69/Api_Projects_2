from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from django.core.files.storage import default_storage # type: ignore
from .utils import predict_image

class MobileNetView(APIView):
    def post(self, request):
        if 'image' not in request.FILES:
            return Response(
                {"error": "Image file is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        image = request.FILES['image']
        path = default_storage.save(image.name, image)
        full_path = default_storage.path(path)

        result = predict_image(full_path)
        return Response(result)
