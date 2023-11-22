# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
# from rest_framework.filters import OrderingFilter

from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # filter_backends = (DjangoFilterBackend,OrderingFilter,)
    # filterset_fields = ('pay_course', 'pay_lesson', 'pay_method',)
    # ordring_fields = ('pay_date',)