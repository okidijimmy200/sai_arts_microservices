from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

def sample_user(email='test@test.com', password='test123'):
    '''create a sample user'''
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):
    # create a new test class
    def test_create_user_with_email_successful(self):
        '''test creating a new user with an email successful'''
        email = 'test@test.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        # run assertion to make sure user was created correctly
        self.assertEqual(user.email, email) #make sure email is the same
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''test the email for new user is normalized'''
        email = 'test@TEST.com'
        user = get_user_model().objects.create_user(email, 'test123') #password test123

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # incase we pass a blank string in email
        with self.assertRaises(ValueError):
            # this shd raise a valueError else the test fails
            get_user_model().objects.create_user(None, 'test123')

    # test to check if the superuser is created and is assigned is_staff and is_superuser
    def test_create_new_superuser(self):
        '''test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@admin.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

# ----------------------------------------------------
'''test admin'''
class AdminSiteTests(TestCase):
    '''setup function that needs to be run b4 any other tests'''
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@admin.com',
            password = 'password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@admin.com',
            password = 'password123',
            name = 'Test user full name'
        )
    def test_users_listed(self):
        '''test that user are listed on the user page'''
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        '''test tht the user edit page works'''
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        # test the page renders ok
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        '''test tht the create user page works'''
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
