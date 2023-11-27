from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from modules.models import Module
from modules.serializers import ModuleSerializer
from reviews.models import Review
from users.models import User


class ModuleTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_create_module(self):
        """ Тестирование создания модуля """
        # print(self.user.id)
        data = {
            "name": "test",
            "description": "test",
            "user": 3
        }

        response = self.client.post('/modules/create/', data=data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'users_for_mail': ['test@sky.pro'],
                'name': 'test',
                'preview': None,
                'description': 'test',
                'link_to_materials': None,
                'user': [3]
            }
        )
        self.assertTrue(
            Module.objects.all().exists()
        )

    def test_list_module(self):
        """ Тестирование вывода списка модулей """
        Module.objects.create(
            name="test2",
            description="test2"
        )
        response = self.client.get('/modules/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         [{'id': 4,
                           'reviews_count': 0,
                           'average_rating': 0,
                           'name': 'test2',
                           'preview': None,
                           'description': 'test2',
                           'link_to_materials': None,
                           'user': []}]
                         )

    def test_destroy_module(self):
        """ Тестирование удаления модуля """
        Module.objects.create(
            name="test3",
            description="test3"
        )
        response = self.client.delete('/modules/destroy/3/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_module(self):
        """ Тестирование изменения модуля """
        Module.objects.create(
            name="test4",
            description="test4"
        )
        response = self.client.patch('/modules/update/5/', {"name": "4_test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                          {'id': 5,
                           'reviews_count': 0,
                           'average_rating': 0,
                           'name': '4_test',
                           'preview': None,
                           'description': 'test4',
                           'link_to_materials': None,
                           'user': []}
                         )

    def tearDown(self):
        pass


class ModuleSerializerTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_valid_module(self):
        data = {
            "name": "test5",
            "description": "test5",
            "user": 1
        }
        serializer = ModuleSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_get_reviews_count(self):
        module = Module.objects.create(
            name="test6",
            description="test6"
        )
        Review.objects.create(
            rating=5,
            module=module
        )
        response = self.client.get('/modules/')
        # print(response.json())
        self.assertEqual(response.json(),
                         [{'id': 1,
                          'reviews_count': 1,
                          'average_rating': 5.0,
                          'name': 'test6',
                          'preview': None,
                          'description': 'test6',
                          'link_to_materials': None,
                          'user': []}])

    def tearDown(self):
        pass