from graphene import AbstractType, Field, String, Date, ID
from graphene_django.forms.mutation import DjangoModelFormMutation
from reservation.forms import OrderForm
from reservation.models import Order
from reservation.schema.query import OrderType
from graphql import GraphQLError


class CreateOrderMutation(DjangoModelFormMutation):
    name = String()
    email = String()
    date = Date()
    table = ID()

    order = Field(OrderType)

    class Meta:
        form_class = OrderForm


class ReservationMutation(AbstractType):
    create_order = CreateOrderMutation.Field()
