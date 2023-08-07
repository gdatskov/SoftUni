from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import views as rest_views

"""
Authentication in pure django (web):
    = Session cookie
User sends session cookie to the Django app

Authentication for API:
    = Token
Client sends 'token' to the Django app
"""

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    # Now the problem here is that the password is not a) hashed and b) returned in the html response as plain text

    # This hashes the password
    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user

    # This removes (whatever we want) from response
    def to_representation(self, instance):
        to_repr = super().to_representation(instance)
        to_repr.pop('password')  # pop to remove whatever is needed
        return to_repr
        # return {} # to return nothing


class RegisterAPIView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


# copy/pasta from https://www.django-rest-framework.org/api-guide/authentication/
class LoginAPIView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            # 'email': user.email   # Or whatever is needed
        })

    # permission_classes = (
    #     permissions.IsAuthenticated
    # )


class LogoutAPIView(rest_views.APIView):
    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)

    @staticmethod
    def __perform_logout(request):
        request.user.auth_token.delete()
        return Response(
            {'message': 'User Logged Out', }
        )
