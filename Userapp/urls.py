from django.urls import path
from .views import UserRegisterView,AddMoneyView,FilterMoney,Top3User
urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("money/",AddMoneyView.as_view()),
    path("chiqim/",FilterMoney.as_view()),
    path("top3/",Top3User.as_view()),
]
