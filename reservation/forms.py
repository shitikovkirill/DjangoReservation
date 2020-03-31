from django.forms import ModelForm
from reservation.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'table', 'date',)
