from django.test import TestCase, override_settings, Client
from django.shortcuts import reverse

from users.models import User


@override_settings(
    STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage"
)
class UsersVewsTests(TestCase):
    fixtures = ["favorite.json", "product.json", "user.json", "category.json"]

    def setUp(self):
        self.client = Client(HTTP_REFERER="http://www.qwant.fr")
        self.user = User.objects.all().first()

    def test_user_is_redirect_with_correct_info(self):
        self.user = User.objects.create_user(
            "test@test.com",
            "testeur",
            last_name="",
            password="i-am-a-strong-very-strong-password-5",
        )
        data = {
            "username": self.user.email,
            "password": "i-am-a-strong-very-strong-password-5",
        }

        url = reverse("users:login")
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 302)

    def test_user_is_redirect_with_invalid_email(self):
        self.user = User.objects.create_user(
            "test@test.com",
            "testeur",
            last_name="",
            password="i-am-a-strong-very-strong-password-5",
        )
        data = {
            "username": "wrong@test.fr",
            "password": "i-am-a-strong-very-strong-password-5",
        }

        url = reverse("users:login")
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 302)

    def test_user_is_redirect_with_invalid_password(self):
        self.user = User.objects.create_user(
            "test@test.com",
            "testeur",
            last_name="",
            password="i-am-a-strong-very-strong-password-5",
        )
        data = {
            "username": self.user.email,
            "password": "i-am-a-wrong-password",
        }

        url = reverse("users:login")
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 302)

    def test_login_view_is_loading_by_accessing_with_get(self):
        url = reverse("users:login")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_logout_redirect(self):
        self.client.force_login(self.user)

        url = reverse("users:logout")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_account_access(self):
        self.client.force_login(self.user)

        url = reverse("users:account")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
