from django.shortcuts import render
from .serializers import RegisterSerializer, AllMoneySerializer, User, AllMoney, ChiqimSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class UserRegisterView(APIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def post(self, request):
        username = request.data.get('user_name')
        password = request.data.get('user_password')
        user = User.objects.create(user_name=username, user_password=password)
        user.save()
        return Response({"status": "User created"})


from .models import UserMoney


class AddMoneyView(APIView):
    serializer_class = AllMoneySerializer
    queryset = AllMoney.objects.all()

    def post(self, request):
        user_n = int(request.data.get("user_n"))
        total_money = request.data.get('total_money')
        pul = UserMoney.objects.all().filter(card_holder=user_n)

        for i in pul:
            user_puli = i.money

        if user_puli >= int(total_money):
            qolgan_pul = user_puli - int(total_money)
            print(qolgan_pul)
            serializer = AllMoneySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print("Save")
            try:
                updater = UserMoney.objects.all().filter(card_holder=user_n).update(money=qolgan_pul)
            except:
                return Response("Sizning Kartangiz yo'q")
            return Response({"MSG": "succses"})
        else:
            return Response({"MSG": "Sizning Pulingiz yetmaydi"})


class FilterMoney(APIView):
    serializer_class = ChiqimSerializer
    queryset = AllMoney.objects.all()

    def post(self, request):
        user_n = request.data.get("user_n")
        type_of_money = request.data.get("type_of_money")
        chiqim = AllMoney.objects.all().filter(
            user_n=user_n, type_of_money=type_of_money)
        money = 0
        for i in chiqim:
            money += i.total_money

        serializer = AllMoneySerializer(chiqim, many=True)
        return Response({"Data": serializer.data,
                         f"Barcha {type_of_money} lar": money
                         })


class Top3User(APIView):
    def get(self, request):
        users_list = []
        #################################
        data_user = User.objects.all()
        for i in data_user:
            users_list.append(i.id)
        print(users_list)
        ##################################

        dict_kirim = {

        }
        dict_chiqim = {

        }

        for k in users_list:
            pul_odam = 0
            pul = AllMoney.objects.all().filter(user_n_id=k, type_of_money="Kirim")

            for d in pul:
                pul_odam += d.total_money
            dict_kirim[k] = pul_odam
        print("kirim", dict_kirim)
        ####################################################################################
        for k in users_list:
            pul_odam = 0
            pul = AllMoney.objects.all().filter(user_n_id=k, type_of_money="Chiqim")

            for d in pul:
                pul_odam += d.total_money
            dict_chiqim[k] = pul_odam
        print('chiqim ', dict_chiqim)
        asosiy_hisob_kitob = {}
        kirimlar = list(dict_kirim.values())
        chiqimlar = list(dict_chiqim.values())

        for t in range(len(kirimlar)):
            total_month = kirimlar[t] - chiqimlar[t]
            asosiy_hisob_kitob[t + 1] = total_month

        print(asosiy_hisob_kitob)

        sorted_asosiy_hisob_kitob = dict(
            sorted(asosiy_hisob_kitob.items(), key=lambda item: item[1], reverse=True))

        top3_users = dict(list(sorted_asosiy_hisob_kitob.items())[:3])

        return Response(top3_users)


