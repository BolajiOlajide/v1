from uuid import uuid4

from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    EmailField,
    FileField,
    Model,
    SlugField,
    TextField,
    UUIDField,
)
from django.utils.text import slugify

# Create your models here.
class Post(Model):
    """
    A model that represents a post
    """
    id = UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    content = TextField(null=False)
    title = CharField(null=False, max_length=255)
    slug = SlugField(unique=True, max_length=255)
    published = BooleanField(default=False)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __repr__(self):
        return f'<Post slug={self.slug}>'

    def __str__(self):
        return f'<Post slug={self.slug}>'


class Subscriber(Model):
    """
    A model that represents a post
    """
    id = UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    email = EmailField(null=False)
    is_active = BooleanField(default=True)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    def __repr__(self):
        return f'<Subscriber id={self.id}>'

    def __str__(self):
        return f'<Subscriber id={self.id}>'
