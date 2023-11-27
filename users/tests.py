from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User
from users.serializers import UserSerializer


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """ Тестирование создания пользователя """
        data = {
            "email": "test@tast.com",
            "username": "test_name",
            "password": "123qwe456rty"
        }
        response = self.client.post('/users/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.all().exists())

    def test_list_user(self):
        """ Тестирование вывода списка пользователя """
        User.objects.create(
            email="test@tast.com",
            username="test_name",
            password="123qwe456rty"
        )
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_user(self):
        """ Тестирование удаления пользователя """
        User.objects.create(
            email="test@tast.com",
            username="test_name",
            password="123qwe456rty"
        )
        response = self.client.delete('/users/15/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_module(self):
        """ Тестирование изменения пользователя """
        User.objects.create(
            email="test@tast.com",
            username="test_name",
            password="123qwe456rty"
        )
        response = self.client.patch('/users/19/', {"username": "name_test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_user(self):
        data = {
            "email": "test@tast.com",
            "username": "test_name",
            "password": "123qwe456rty"
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def tearDown(self):
        pass