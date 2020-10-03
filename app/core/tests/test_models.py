from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        # Test creating a new user with an email is successfull
        email = "parthrr510@gmail.com"
        password = "Testpass1234"
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        # Test the email for the new user is normalized
        email = "parthrr510@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test creating with no email raises error"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_user(self):
        # Test creating a new user email
        user = get_user_model().objects.create_superuser('test@gmail.com',
                                                         'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
