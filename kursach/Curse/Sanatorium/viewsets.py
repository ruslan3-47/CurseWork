
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permission import *
from rest_framework.pagination import PageNumberPagination
from .serializers import *

class APIPagination(PageNumberPagination):
    page_size = 3
    page_query_param = "page_size"
    max_page_size = 5

class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission )
    pagination_class = APIPagination
    queryset = Users.objects.all()
    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        return UserSerializer

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer

    def get_queryset(self):
        type = self.request.GET.get('type', '')
        if type:
            return Room.objects.filter(type=type)
        else:
            return Room.objects.all()

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

