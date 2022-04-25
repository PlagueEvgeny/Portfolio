import blogapp.views as blogapp
from django.urls import path
from blogapp.views import PostList, PostDetail

app_name = 'blogapp'

urlpatterns = [
	path('', PostList.as_view(), name='index'),
	path('<int:pk>/', PostDetail.as_view(), name='post')
]