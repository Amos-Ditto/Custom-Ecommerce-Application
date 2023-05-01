import graphene
import graphql_jwt
from backend.users.schema import Mutation as UserMutations, Query as UserQuery
from backend.products.schema import Query as ProductQuery
from backend.orders.schema import Query as OrderQuery


class Query(UserQuery, ProductQuery, OrderQuery, graphene.ObjectType):
    pass


class Mutation(UserMutations, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
