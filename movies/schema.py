import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from movies.models import Category, Pelicula, Cine, Sala

# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'peliculas']
        interfaces = (relay.Node, )

class CineNode(DjangoObjectType):
    class Meta:
        model = Cine
        filter_fields = ['name', 'salas']
        interfaces = (relay.Node, )

# Se hace lo mismo con el modelo Ingredient
class PeliculaNode(DjangoObjectType):
    class Meta:
        model = Pelicula
        # Permite un filtrado mas avanzado
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )

# Se hace lo mismo con el modelo Ingredient
class SalaNode(DjangoObjectType):
    class Meta:
        model = Sala
        # Permite un filtrado mas avanzado
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'cine': ['exact'],
            'cine__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    movies = relay.Node.Field(PeliculaNode)
    all_movies = DjangoFilterConnectionField(PeliculaNode)

    cine = relay.Node.Field(CineNode)
    all_cines = DjangoFilterConnectionField(CineNode)

    salas = relay.Node.Field(SalaNode)
    all_salas = DjangoFilterConnectionField(SalaNode)