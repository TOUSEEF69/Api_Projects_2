from django.urls import path # type: ignore
from .views import PencilSketchView

urlpatterns = [
    path('predict/', PencilSketchView.as_view()),
]
