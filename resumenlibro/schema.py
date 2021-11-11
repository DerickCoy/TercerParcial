import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from resumenlibro.models import Post
from graphql_relay.node.node import from_global_id
 
class PublicacionNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = ['autor', 'autor_del_libro','libro','resumen']
        interfaces = (relay.Node, )
 
class CreatePublicacion(graphene.relay.ClientIDMutation):
    Publicacion = graphene.Field(PublicacionNode)
    class Input:
        autor = graphene.String()
        autor_del_libro = graphene.String()
        libro = graphene.String()
        resumen = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        Publicacion = Post(
            autor=input.get('autor'),
            autor_del_libro=input.get('autor_del_libro'),
            libro=input.get('libro'),
            resumen=input.get('resumen'),
        )
        Publicacion.save()
        return CreatePublicacion(Publicacion=Publicacion)
 
 
class UpdatePublicacion(graphene.relay.ClientIDMutation):
    Publicacion = graphene.Field(PublicacionNode)
    class Input:
        id = graphene.String()
        autor = graphene.String()
        autor_del_libro = graphene.String()
        descripcion = graphene.String()
        libro = graphene.String()
        resumen = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        Publicacion = Post.objects.get(pk=from_global_id(input.get('id'))[1])
        Publicacion.autor = input.get('autor')
        Publicacion.autor_del_libro = input.get('autor_del_libro')
        Publicacion.libro = input.get('libro')
        Publicacion.resumen = input.get('resumen')
        Publicacion.save()
        return UpdatePublicacion(Publicacion=Publicacion)
 
 
class DeletePublicacion(graphene.relay.ClientIDMutation):
    Publicacion = graphene.Field(PublicacionNode)
 
    class Input:
        id = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        Publicacion = Post.objects.get(pk=from_global_id(input.get('id'))[1])
        Publicacion.delete()
        return DeletePublicacion(Publicacion=Publicacion)
 
class Query(graphene.ObjectType):
    Publicacion = relay.Node.Field(PublicacionNode)
    all_Publicaciones = DjangoFilterConnectionField(PublicacionNode)
 
class Mutation(graphene.AbstractType):
    create_Publicacion = CreatePublicacion.Field()
    update_Publicacion= UpdatePublicacion.Field()
    delete_Publicacion= DeletePublicacion.Field()
