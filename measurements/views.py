from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from measurements.models import Sensor, Measurement
from measurements.serializers import SensorDetailSerializer, SensorsSerializer, MeasurementsSerializer


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorView(ListCreateAPIView):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer


class SensorupdateView(RetrieveUpdateAPIView):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class DetailedView(RetrieveAPIView):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
