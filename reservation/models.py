from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE


class Table(models.Model):

    SHAPE_CHOICES = (
        (1, 'Rectangle'),
        (2, 'Ellipse'),
    )
    number = models.PositiveIntegerField(unique=True)
    sits = models.PositiveIntegerField(default=2)
    shape = models.IntegerField(choices=SHAPE_CHOICES)

    coordinateX = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    coordinateY = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    length = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    width = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return str(self.number)


class Order(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    table = models.ForeignKey(Table, CASCADE, related_name="orders")
    date = models.DateField()

    class Meta:
        unique_together = ('table', 'date',)

    def __str__(self):
        return str(self.date)
