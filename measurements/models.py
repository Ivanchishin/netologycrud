from django.db import models


class Sensor(models.Model):
    """Объект на котором проводят измерения."""

    name = models.TextField(blank=True)
    description = models.TextField(blank=True)


class Measurement(models.Model):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
