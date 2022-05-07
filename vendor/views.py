from rest_framework.generics import ListAPIView, UpdateAPIView
from adminn.models import Query, Service
from rest_framework.response import Response
from client.models import MidOrder
from .serializers import *
from adminn.serializer import QuerySerializer
from account.models import User
from rest_framework.permissions import IsAdminUser
from account.serializer import UserSerializer
from client.serializer import ServiceWithMoreDetails, MidOrderSerializer


class MyOrders(ListAPIView):
    queryset = MidOrder.objects.all()
    serializer_class = MidOrderVSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self, *args, **kwargs):
        return super(MyOrders, self).get_queryset(*args, **kwargs).filter(service__provider=self.request.user).order_by('-id')


class MyServices(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceWithMoreDetails
    permission_classes = [IsAdminUser]

    def get_queryset(self, *args, **kwargs):
        return super(MyServices, self).get_queryset(*args, **kwargs).filter(provider=self.request.user).order_by('-sid')


class UpdateStatus(UpdateAPIView):
    queryset = MidOrder.objects.all()
    serializer_class = MidOrderSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, pk):
        instance = self.get_object()
        if request.user != instance.service.provider:
            return Response(401)
        status = request.GET.get('status', None)
        if not status:
            return Response(404)
        instance.status = status
        instance.save()
        return Response({"success": True})


class Users(ListAPIView):
    queryset = MidOrder.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(service__provider=request.user)
        users = []
        for mid in instance:
            if mid.order.user not in users:
                users.append(mid.order.user)
        return Response({"success": True, "data": self.serializer_class(users, many=True).data})


class QueryVendor(ListAPIView):

    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self, *args, **kwargs):
        return super(QueryVendor, self).get_queryset(*args, **kwargs).filter(service__provider=self.request.user).order_by('-id')


class SendQueryToAdmin(UpdateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    permission_classes = [IsAdminUser]

    def update(self, request):
        instance = self.get_object()
        instance.is_at_admin = True
        return Response({"success": True, "data": self.serializer_class(instance).data})