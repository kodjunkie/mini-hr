from django.test import TestCase
from django.urls import reverse

from .models import User


def create_user():
    """
    Create a new user
    :return: New User Object
    """
    return User.objects.create_user(username='tester', password='P@ssw0rD')


# Test for authentication
class UserAuthTests(TestCase):
    def test_login(self):
        """
        Make sure the user logs in successfully
        """
        self.user = create_user()
        response = self.client.login(username='tester', password='P@ssw0rD')
        self.assertIs(response, True)

    def test_login_with_xmlhttp_request(self):
        """
            Only accept auth credentials via Ajax request with POST method,
            Make sure the request was successful,
            Make sure you get the successful message with no errors in json
        """
        self.user = create_user()
        response = self.client.post(
            reverse('users:login'),
            {'username': 'tester', 'password': 'P@ssw0rD'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'msg': 'Login successful.',
                'error': False
            }
        )

    def test_logout(self):
        """
        Make sure users logout successfully
        """
        self.user = create_user()
        self.client.login(username='tester', password='P@ssw0rD')
        response = self.client.logout()
        self.assertIs(response, None)


# Test the views to make sure unwanted request methods are not permitted
class UserViewTests(TestCase):
    def test_login(self):
        """
            Make sure the login form view displays
        """
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """
            Do not allow unwanted request methods
        """
        response = self.client.post(reverse('users:login'))
        self.assertEqual(response.status_code, 403)
