from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from modules.models import Module
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from users.models import User


class ReviewTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=True, is_staff=True)
        self.module = Module.objects.create(name="test7", description="test7")
        self.client.force_authenticate(user=self.user)

    def test_create_module(self):
        """ Тестирование создания отзыва """
        data = {
            "rating": 5,
            "description": "test",
            "module": 6,
            "user": 7
        }

        response = self.client.post('/reviews/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {'id': 2,
             'rating': '5',
             'description': 'test',
             'module': 6,
             'user': 7}
        )
        self.assertTrue(
            Review.objects.all().exists()
        )

    def test_list_module(self):
        """ Тестирование вывода списка отзывов """
        Review.objects.create(
            rating=5,
            description="test3",
            module=self.module,
            user=self.user
        )
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         [{'id': 4,
                           'rating': '5',
                           'description': 'test3',
                           'module': 8,
                           'user': 9}]
                         )

    def test_destroy_review(self):
        """ Тестирование удаления отзыва """
        Review.objects.create(
            rating=5,
            description="test4",
            module=self.module,
            user=self.user
        )
        response = self.client.delete('/reviews/3/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_module(self):
        """ Тестирование изменения отзыва """
        Review.objects.create(
            rating=5,
            description="test5",
            module=self.module,
            user=self.user
        )
        response = self.client.patch('/reviews/5/', {"description": "5_test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                          {'id': 5,
                            'rating': '5',
                            'description': '5_test',
                            'module': 9,
                            'user': 10}
                         )

    def test_valid_review(self):
        data = {
            "rating": 5,
            "description": "test",
            "module": 6,
            "user": 7
        }
        serializer = ReviewSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def tearDown(self):
        pass