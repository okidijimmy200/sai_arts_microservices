import datetime
import uuid
from django.utils import timezone
from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from . import models
from django.urls import reverse
from .serializers import ArtPieceSerializer

from rest_framework import serializers, status
from rest_framework.test import APIClient

ARTPIECE_URL = reverse('artpiece:artpiece-list')

def sample_user(email='test@test.com', password='test123'):
    '''create a sample user'''
    return get_user_model().objects.create_user(email, password)
 
def image_upload_url(artpiece_id):
    '''return URL for artpiece'''
    return reverse('artpiece:artpiece-upload-image', args=[artpiece_id])

def detail_url(artpiece_id):
    '''return artpiece detail url'''
    return reverse('artpiece: artpiece-detail', args=[artpiece_id])

def sample_artpiece(user, **params):
    '''create and return a sample artpiece'''
    defaults = {
            'name':'testman',
            'publish_date': datetime.datetime.now(tz=timezone.utc),
            'timestamp':datetime.datetime.now(tz=timezone.utc),
            'slug': 'testman',
            'body' :'this is a powerful picture',
            'status' :'created'
    }
    defaults.update(params)

    return models.ArtPiece.objects.create(user=user, **defaults)

class ModelTests(TestCase):

    def test_artpiece_str(self):
        '''test the artpiece string representation'''
        artpiece = models.ArtPiece.objects.create(
            user=sample_user(),
            name='testman',
            publish_date= datetime.datetime.now(tz=timezone.utc),
            timestamp=datetime.datetime.now(tz=timezone.utc),
            slug = 'testman',
            body='this is a powerful picture',
            status='created'

        )
        self.assertEqual(str(artpiece), artpiece.name)

    @patch('uuid.uuid4')
    def test_picture_upload(self, mock_uuid):
        '''test that image is saved in the correct location'''
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        # call function to call file path
        file_path = models.art_image_path(None, 'myimage.jpg')

        exp_path = f'upload/art/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)

class PublicArtpieceApiTests(TestCase):
    '''test unauthenticated artpiece API access'''
    def  setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        '''test tht authentication is required'''
        res = self.client.get(ARTPIECE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateArtPieceTests(TestCase):
    '''test unauthenticated artpiece API access'''
    def setUp(self):
        self.client = APIClient()

        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'testpass'
        )

        self.client.force_authenticate(self.user)

    def test_retrieve_artpiece(self):
        '''test retrieving a list of artpieces'''
        sample_artpiece(user=self.user)
        # sample_artpiece(user=self.user)

        res = self.client.get(ARTPIECE_URL)

        artpiece = models.ArtPiece.objects.all().order_by('-id')
        serializer = ArtPieceSerializer(artpiece, many=True)
        self.assertEqual(res.data, serializer.data)




