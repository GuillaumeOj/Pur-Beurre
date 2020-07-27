from tests.custom import CustomTestCase
from users.models import User


class UserModelsTests(CustomTestCase):
    def get_user(self):
        return User.objects.all().first()

    def create_user(self, email, first_name, last_name, password):
        return User.objects.create_user(
            email=email, first_name=first_name, last_name=last_name, password=password
        )

    def create_superuser(self, email, first_name, last_name, password):
        return User.objects.create_superuser(
            email=email, first_name=first_name, last_name=last_name, password=password
        )

    def test_user_printing_name(self):
        user = self.get_user()

        self.assertIsInstance(user, User)
        self.assertEqual(user.__str__(), user.email)

    def test_user_is_created_with_all_fields(self):
        user = self.create_user(
            "test@test.com", "testeur", "testeur", "i-am-a-strong-password-5"
        )

        self.assertIsInstance(user, User)

    def test_user_is_created_with_all_required_fields_only(self):
        user = self.create_user(
            "test@test.com", "testeur", "", "i-am-a-strong-password-5"
        )

        self.assertIsInstance(user, User)

    def test_user_is_not_created_with_email_missing(self):
        with self.assertRaises(ValueError):
            self.create_user("", "testeur", "testeur", "i-am-a-strong-password-5")

    def test_user_is_not_created_with_first_name_missing(self):
        with self.assertRaises(ValueError):
            self.create_user("test@test,com", "", "testeur", "i-am-a-strong-password-5")

    def test_user_is_not_created_with_password_missing(self):
        with self.assertRaises(ValueError):
            self.create_user("test@test,com", "testeur", "testeur", "")

    def test_superuser_is_created(self):
        superuser = self.create_superuser(
            "test@test.com", "testeur", "testeur", "i-am-a-strong-password-5"
        )

        self.assertIsInstance(superuser, User)
