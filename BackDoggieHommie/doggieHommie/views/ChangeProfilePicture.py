from django.db import Error
from ast import Try
from time import time_ns
from warnings import catch_warnings
from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import UserSerializer
from doggieHommie.serializers import UserDjangoSerializer
from doggieHommie.models import User
from django.contrib.auth.models import User as DjangoUser
from rest_framework.status import *

from rest_framework.response import Response
from doggieHommie.services.FirebaseService import firebase
import base64


class ChangeProfilePictureView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request, pk):
        data = request.data
        print(data)
        user = User.objects.get(id=pk)

        if user != None:
            image = data["data"]

            try:
                appUser = DjangoUser.objects.get(id = user.user_id)

                extesion = data["imgName"].split(".")[-1]
                file = base64.b64decode(image)
                storage = firebase.storage()
                path = "user/" + str(time_ns()) + extesion
                fileInfo = storage.child(path).put(file)
                data["profile_picture"] = storage.child(
                    path).get_url(fileInfo["downloadTokens"])

                appUser.profile_picture = data["profile_picture"]
                appUser.save()
                
                response = super().patch(request)

            except Error as e:
                return Response(data={"exitoso": False, "error": e.args[0], }, status=HTTP_400_BAD_REQUEST)


            return Response(data={"exitoso": True, "mensaje": "Se ha cambiado la foto de perfil", }, status=HTTP_200_OK)
