from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserTests(TestCase):
    '''test the user api public'''
    def setUp(self):
        self.client = APIClient()

    # test to validate the user is created successfully
    def test_create_valid_user_successful(self):
        # sample load
        payload = {
            'email': 'test@test.com',
            'password': 'test123',
            'name': 'test name'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data) # take the dic res and pass it as response
        self.assertTrue(user.check_password(payload['password']))
        # to make sure the password is not returned in req body
        self.assertNotIn('password', res.data)
