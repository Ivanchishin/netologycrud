from django.urls import path
from .views import DetailedView, SensorView, SensorupdateView,MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorupdateView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('details/<int:pk>', DetailedView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
