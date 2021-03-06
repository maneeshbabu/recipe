from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTestCase(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = "test@example.com"
        password = "test123"
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test creating a new user with email is normalized"""
        email = "test@EXAMPLE.com"
        user = get_user_model().objects.create_user(email=email,
                                                    password='test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a new user with invalid email raise exception"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None,
                                                 password='test123')

    def test_new_user_is_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            email="test@example.com", password="test123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
