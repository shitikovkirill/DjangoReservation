import graphene

from reservation.schema.mutation import ReservationMutation
from reservation.schema.query import ReservationQuery


class Query(
    ReservationQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    ReservationMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
