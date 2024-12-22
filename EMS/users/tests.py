from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

CustomUser = get_user_model()

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            phone_number="01234567890",
            password="Test@1234",
            user_type="regular"
        )
        self.login_url = reverse("login")
        self.signup_url = reverse("signup")
        self.logout_url = reverse("logout")
        self.update_url = reverse("update")

    def test_signup_success(self):
        response = self.client.post(self.signup_url, {
            "email": "newuser@example.com",
            "username": "newuser",
            "phone_number": "01122334455",
            "password": "NewPass@123",
            "confirm_password": "NewPass@123",
            "user_type": "admin"
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login after successful signup
        self.assertTrue(CustomUser.objects.filter(username="newuser").exists())

    def test_signup_invalid_email(self):
        response = self.client.post(self.signup_url, {
            "email": "invalidemail",
            "username": "newuser",
            "phone_number": "01122334455",
            "password": "NewPass@123",
            "confirm_password": "NewPass@123",
            "user_type": "admin"
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid email format!")

    def test_signup_existing_username(self):
        response = self.client.post(self.signup_url, {
            "email": "newuser@example.com",
            "username": "testuser",
            "phone_number": "01122334455",
            "password": "NewPass@123",
            "confirm_password": "NewPass@123",
            "user_type": "admin"
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username already exists!")

    def test_login_success(self):
        response = self.client.post(self.login_url, {
            "username": "testuser",
            "password": "Test@1234",
        })
        self.assertEqual(response.status_code, 302)  # Redirect to index after login
        self.assertIn('_auth_user_id', self.client.session)  # User is logged in

    def test_login_failure(self):
        response = self.client.post(self.login_url, {
            "username": "testuser",
            "password": "WrongPass@123",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid email or password")

    def test_logout(self):
        self.client.login(username="testuser", password="Test@1234")
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertNotIn('_auth_user_id', self.client.session)  # User is logged out

    def test_update_phone_number_success(self):
        self.client.login(username="testuser", password="Test@1234")
        response = self.client.post(self.update_url, {
            "update_choice": "1",
            "new_phone": "01111222333"
        })
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.user.refresh_from_db()
        self.assertEqual(self.user.phone_number, "01111222333")

    def test_update_password_success(self):
        self.client.login(username="testuser", password="Test@1234")
        response = self.client.post(self.update_url, {
            "update_choice": "2",
            "new_password": "Updated@1234",
            "confirm_password": "Updated@1234"
        })
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("Updated@1234"))

    def test_update_failure_phone_number_exists(self):
        CustomUser.objects.create_user(
            username="otheruser",
            email="otheruser@example.com",
            phone_number="01111222333",
            password="OtherPass@123"
        )
        self.client.login(username="testuser", password="Test@1234")
        response = self.client.post(self.update_url, {
            "update_choice": "1",
            "new_phone": "01111222333"
        })
        self.assertEqual(response.status_code, 302)  # Redirect after failure
        self.assertContains(response, "Phone number already exists!")
