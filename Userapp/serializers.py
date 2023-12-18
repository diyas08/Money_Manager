from rest_framework.serializers import ModelSerializer
from .models import User, AllMoney




class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class AllMoneySerializer(ModelSerializer):
    class Meta:
        model = AllMoney
        fields = "__all__"
class ChiqimSerializer(ModelSerializer):
    class Meta:
        model = AllMoney
        fields = ("user_n","type_of_money",)
