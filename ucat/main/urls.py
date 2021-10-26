from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path('c/<str:short>/',views.redirector, name = 'redirect'),
	path('',views.index , name = 'index'),
	path('add/',views.add,name='add'),
	path('register/',views.register,name = 'register'),
	path('signin/',views.signin,name = 'signin'),
	path('logout/',views.logout,name = 'logout'),
	path('delete/<str:short>',views.delete,name = 'delete'),
]