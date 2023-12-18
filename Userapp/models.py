from django.db import models


# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20, unique=True)
    user_password = models.CharField(max_length=16)

    def __str__(self):
        return self.user_name

#
class AllMoney(models.Model):
    user_n = models.ForeignKey(User, on_delete=models.CASCADE)
    total_money = models.IntegerField(default=0)
    CHOISES = (
        ("Kirim", "Kirim"),
        ("Chiqim", "Chiqim"),
    )
    type_of_money = models.CharField(max_length=6, choices=CHOISES)
    date = models.DateField(auto_now_add=True)
    CHOISE2 = (
        ("Oziq-ovqat", "Oziq-ovqat"),
        ("Transport", "Transport"),
        ("Kiyim-kechak", "Kiyim-kechak"),
        ("Komunal", "Komunal"),
        ("Axborot-vositalari", "Axborot-vositalari"),
        ("Kafe-restoran", "Kafe-restoran"),
        ("Taksi", "Taksi"),
        ("Xizmatlar", "Xizmatlar"),

    )
    category_money = models.CharField(max_length=30, choices=CHOISE2)
    comment = models.TextField(blank=True)
class UserMoney(models.Model):
    card_holder = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.IntegerField(default=8600)
    expired_date = models.DateField()
    money = models.IntegerField()

    def __str__(self):
        return str(self.card_holder)