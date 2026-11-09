import factory

from django.contrib.auth.models import User
from django.utils.text import slugify

from blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Faker("safe_email")

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if extracted:
            self.set_password(extracted)
            if create:
                self.save()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f"Post {n}")
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
    content = factory.Faker("paragraph")
    author = factory.SubFactory(UserFactory)
    status = 0