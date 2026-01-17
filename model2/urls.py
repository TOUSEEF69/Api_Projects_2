from django.urls import path # type: ignore
from .views import MobileNetView

urlpatterns = [
    path('predict/', MobileNetView.as_view()),
]
