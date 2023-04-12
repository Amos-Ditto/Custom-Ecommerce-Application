import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
from .models import AppUser
from .forms import UserCreationForm


class AppUserType(DjangoObjectType):
    class Meta:
        model = AppUser


class AppUserMutation(DjangoModelFormMutation):
    user = graphene.Field(AppUserType)

    class Meta:
        form_class = UserCreationForm


class Mutation(graphene.ObjectType):
    register_user = AppUserMutation.Field()
