from uuid import uuid4

from django.db.models import (
    Model,
    UUIDField,
    TextField,
    BooleanField,
    FileField,
    EmailField
)

# Create your models here.
class Post(Model):
    """
    A model that represents a post
    """
    id = UUIDField(unique=True, primary_key=True, default=uuid4())
    content = TextField(null=False)
    title = TextField(null=False)
    published = BooleanField(null=False, default=False)

    def __repr__(self):
        return f'<Post id={self.id}>'

    def __str__(self):
        return f'<Post id={self.id}>'


class Subscriber(Model):
    """
    A model that represents a post
    """
    id = UUIDField(unique=True, primary_key=True, default=uuid4())
    email = EmailField(null=False)

    def __repr__(self):
        return f'<Subscriber id={self.id}>'

    def __str__(self):
        return f'<Subscriber id={self.id}>'
