from django.urls import path
from .views import BoardList, BoardDetail, BoardCreate, BoardDetail
from . import views
import write.views

app_name = "write"
urlpatterns = [

    path("",BoardList.as_view(), name = 'list'),
    path("detail/<int:pk>",BoardDetail.as_view(), name = 'detail'),   #해당과목번수
    path('create', views.write_add, name='create'),  
    path('delete/<int:pk>' , views.write_delete, name='delete'),  #해당과목의평가번호
]