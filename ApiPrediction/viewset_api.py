

from rest_framework.views import APIView

from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
import pickle


class testingyaa(APIView):
    def get(self,request):
        object_file = pickle.load(open('prediction_model.sav','rb'))
        testing = object_file.predict([[request.data['ac'],request.data['selimut'],request.data['bantal'],request.data['kursi_l'],request.data['kursi_xl'],request.data['kursi_xll'],request.data['non_stop'],request.data['sleeper'],request.data['toilet'],request.data['wifi'],request.data['makan'],request.data['minum'],request.data['charging_station'],request.data['smoking_room'],request.data['sandaran_kaki'],request.data['jarak'],request.data['harga_bbm']]])
        print(testing)
        return JsonResponse(testing[0],safe=False)
    