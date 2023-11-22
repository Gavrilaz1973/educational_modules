from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    # lesson_count = SerializerMethodField()

    # def get_lesson_count(self, obj):
    #     return Lesson.objects.filter(course=obj.pk).count()

    class Meta:
        model = Review
        fields = '__all__'