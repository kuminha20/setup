import pytest

from blog.factories import PostFactory
from blog.models import Post


@pytest.mark.django_db
def test_create_post():
    """Garante que um Post pode ser criado corretamente usando a Factory."""
    post = PostFactory(title="Meu Primeiro Post no Blog", status=1)

    assert post.title == "Meu Primeiro Post no Blog"
    assert post.slug == "meu-primeiro-post-no-blog"
    assert post.status == 1
    assert str(post) == "Meu Primeiro Post no Blog"
    assert post.author is not None


@pytest.mark.django_db
def test_default_status_is_draft():
    post = PostFactory()

    assert post.status == 0


@pytest.mark.django_db
def test_posts_ordered_by_newest_first():
    first = PostFactory()
    second = PostFactory()

    assert list(Post.objects.all()) == [second, first]