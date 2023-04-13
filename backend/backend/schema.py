import graphene
import graphql_jwt
from backend.users.schema import Mutation as UserMutations, Query as UserQuery


class Query(UserQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(UserMutations, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
