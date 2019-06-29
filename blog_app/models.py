from uuid import uuid4

from django.db.models import (
    Model,
    UUIDField,
    TextField,
    BooleanField,
    FileField,
    EmailField,
    DateField
)

# Create your models here.
class Post(Model):
    """
    A model that represents a post
    """
    id = UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    content = TextField(null=False)
    title = TextField(null=False)
    published = BooleanField(null=False, default=False)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    def __repr__(self):
        return f'<Post id={self.id}>'

    def __str__(self):
        return f'<Post id={self.id}>'


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
