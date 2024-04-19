import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from users.models import Profile
from posts.models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post


# TODO: Add tag type


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    # TODO: Add post by tag resolver

    def resolve_all_posts(root, info):
        return Post.objects.all()


class PostMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, text):
        post = Post.objects.create(text=text)
        return PostMutation(post=post)


class Mutation(graphene.ObjectType):
    create_post = PostMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
