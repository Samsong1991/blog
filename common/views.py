from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework import viewsets, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from common.models import User
from common.serializers import UserSerializer, UserLoginSerializer, UserPasswordSerializer


def get_random_password():
    import random
    import string
    return ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 8))


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginViewSet(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=200)
        else:
            ret = {'detail': 'Username or password is wrong'}
            return Response(ret, status=403)

    def put(self, request, *args, **kwargs):
        """
        Parameter: username->user's username who forget old password
        """
        username = request.data.get('username', '')
        users = User.objects.filter(username=username)
        user: User = users[0] if users else None

        if user is not None and user.is_active:
            password = get_random_password()

            try:
                send_mail(subject="New password for Library System",
                          message="Hi: Your new password is: \n{}".format(password),
                          from_email=django.conf.settings.EMAIL_HOST_USER,
                          recipient_list=[user.email],
                          fail_silently=False)
                user.password = make_password(password)
                user.save()
                return Response({
                    'detail': 'New password will send to your email!'
                })
            except Exception as e:
                print(e)
                return Response({
                    'detail': 'Send New email failed, Please check your email address!'
                })
        else:
            ret = {'detail': 'User does not exist(Account is incorrect !'}
            return Response(ret, status=403)


class UserLogoutViewSet(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserLoginSerializer

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail': 'logout successful !'})


class PasswordUpdateViewSet(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserPasswordSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        password = request.data.get('password', '')
        new_password = request.data.get('new_password', '')
        user = User.objects.get(id=user_id)
        if not user.check_password(password):
            ret = {'detail': 'old password is wrong !'}
            return Response(ret, status=403)

        user.set_password(new_password)
        user.save()
        return Response({
            'detail': 'password changed successful !'
        })
