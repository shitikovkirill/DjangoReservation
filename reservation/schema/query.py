from graphene import Field, Boolean, Date, ObjectType, List
from graphene_django import DjangoObjectType

from reservation.models import (
    Table as TableModel,
    Order as OrderModel
)


class TableType(DjangoObjectType):
    class Meta:
        model = TableModel

    reserved = Field(Boolean, date=Date())

    def resolve_reserved(self, info, date):
        return OrderModel.objects.filter(
            id=self.id,
            date=date
        ).exists()


class OrderType(DjangoObjectType):
    class Meta:
        model = OrderModel


class ReservationQuery(object):
    tables = List(TableType)

    def resolve_tables(self, info):
        return TableModel.objects.all()
