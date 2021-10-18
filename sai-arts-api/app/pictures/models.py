from django.db import models
import uuid
import os
from django.conf import settings
from django.utils import timezone

def art_image_path(instance, filename):
    '''Generate file path for new art image'''
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    # join
    return os.path.join('upload/art/', filename)
# exhibited art pieces
class ExhibitedManager(models.Manager):
    def get_queryset(self):
        return super(ExhibitedManager,
                    self).get_queryset().filter(status='exhibited')

# latest artpieces
class LatestPiecesManager(models.Manager):
    def get_queryset(self):
        return super(LatestPiecesManager,
                    self).get_queryset().filter(status='created')

class ArtPiece(models.Model):
    '''art piece and the artist who created it'''
    STATUS_CHOICES = (
    ('created', 'Created'),
    ('exhibited','Exhibited')
    )
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    publish_date = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique=name)
    body = models.TextField()
    status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='created')

    class Meta:
        ordering = ('-timestamp',)
    
    def __str__(self):
        return self.name

    objects = models.Manager()

    exhibited = ExhibitedManager()

    created = LatestPiecesManager()

