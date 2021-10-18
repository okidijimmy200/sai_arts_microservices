from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

TOKEN_USER_URL = reverse('user:token')
CREATE_USER_URL = reverse('user:create')
ME_URL = reverse('user:me')

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
    
    # test to check if the user  exists
    def test_user_exists(self):
        payload = {'email': 'test@test.com','password': 'test123'}
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        '''test tht the password must be more than 5 characters'''
        payload = {'email': 'test@test.com', 'password': 'pw'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        '''test tht a token is generated for user'''
        payload= {'email': 'test@test.com', 'password': 'password123'}
        create_user(**payload)
        res = self.client.post(TOKEN_USER_URL, payload)

        self.assertIn('token', res.data) #check if there is a key in token sent
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_no_user(self):
        '''test tht token is not created if user doesnot exist'''
        payload = {'email': 'test@test.com', 'password': 'password123'}
        res =  self.client.post(TOKEN_USER_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_fields(self):
        '''test tht email and password are required'''
        res = self.client.post(TOKEN_USER_URL, {'email': 'one', 'password': ''})
        self.assertNotEqual('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

class PrivateUserApiTest(TestCase):
    '''test API request tht requires authentication'''

    def setUp(self):
        self.user = create_user(
            email = 'test@test.com',
            password='test123',
            name='name'
        )
        # setup our client
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        'test retrieving profile for logged in user'
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'name': self.user.name,
            'email': self.user.email
        })