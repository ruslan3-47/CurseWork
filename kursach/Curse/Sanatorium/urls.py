
from django.urls import path,include
from .views import *
from .viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',UsersViewSet,basename='users')
router.register(r'rooms',RoomViewSet,basename='rooms')
router.register(r'programs',ProgramViewSet,basename='programs')
router.register(r'types',TypeViewSet,basename='types')

urlpatterns = [
    path('mainpage/', Homepage.as_view(), name="mainpage"),
    path('rooms/', Rooms.as_view(), name="rooms"),
    path('program/', Program_html.as_view(), name="programs"),
    path('program/<slug:program_slug>',Show_program.as_view(), name = "program"),
    path('about/', About.as_view(), name="about"),
    path('rooms/<slug:room_slug>', ShowRoom.as_view(), name="room"),
    path('food/', Food.as_view(), name = 'food'),
    path('register/',RegisteUsers.as_view() , name = 'register'),
    path('login/',LoginUsers.as_view(),name = 'login'),
    path ('logout/', logout_user, name = 'logout'),
    path ('user/editprofile/',UserInfoAdd.as_view(),name = 'addinfo'),
    path ('user/',UsersHome.as_view(),name = 'usershome'),
    path('order/', OrderingProgram.as_view(),name = 'ordering'),
    path ('adminviews/',AdminViews.as_view(), name = 'admin'),
    path ('EditUser/<int:pk>/',EditUser.as_view(),name = "edituser"),
    path ('EditProgram/<int:pk>/',EditProgram.as_view(),name = "editprogram"),
    path ('EditRoom/<int:pk>/',EditRoom.as_view(),name = "editroom"),
    path ('EditType/<int:pk>/',EditType.as_view(),name = "edittype"),
    path ('adminviews/CreateUser/', CreateUser.as_view(), name= "createuser"),
    path('adminviews/CreateProgram/', CreateProgram.as_view(), name="createprogram"),
    path('adminviews/CreateRoom/', CreateRoom.as_view(), name="createroom"),
    path('adminviews/CreateType/', CreateType.as_view(), name="createtype"),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('rest_framework.urls')),

    #homepage user
]
