from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from modules.tasks import send_email
from modules.models import Module
from reviews.models import Review
from users.models import User


class ModuleSerializer(serializers.ModelSerializer):
    reviews_count = SerializerMethodField()
    average_rating = SerializerMethodField()

    def get_reviews_count(self, obj):
        return Review.objects.filter(module=obj.pk).count()

    def get_average_rating(self, obj):
        sum_rating = 0
        for rev in Review.objects.filter(module=obj.pk):
            sum_rating += int(rev.rating)
        if sum_rating == 0:
            avg_rating = 0
        else:
            avg_rating = sum_rating / Review.objects.filter(module=obj.pk).count()
        return avg_rating

    class Meta:
        model = Module
        fields = '__all__'


class ModuleCreateSerializer(serializers.ModelSerializer):
    users_for_mail = SerializerMethodField()

    def get_users_for_mail(self, obj):
        email_address = []
        for sub in User.objects.all():
            email_address.append(sub.email)
        send_email.delay(obj.name, email_address)
        return email_address

    class Meta:
        model = Module
        fields = '__all__'