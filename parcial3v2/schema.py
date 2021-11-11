import graphene
import resumenlibro.schema


class Query(resumenlibro.schema.Query, graphene.ObjectType):
   
    pass
class Mutation(resumenlibro.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)