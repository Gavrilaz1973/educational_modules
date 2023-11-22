from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from modules.models import Module
from reviews.models import Review


class ModuleSerializer(serializers.ModelSerializer):
    reviews_count = SerializerMethodField()
    average_rating = SerializerMethodField()

    def get_reviews_count(self, obj):
        return Review.objects.filter(module=obj.pk).count()

    def get_average_rating(self, obj):
        sum_rating = 0
        for rev in Review.objects.filter(module=obj.pk):
            sum_rating += int(rev.rating)
        avg_rating = sum_rating / Review.objects.filter(module=obj.pk).count()
        return avg_rating

    class Meta:
        model = Module
        fields = '__all__'