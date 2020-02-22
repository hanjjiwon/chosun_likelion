from django.urls import path
from .views import BoardList, BoardDetail
from . import views
import write.views

app_name = "board"
urlpatterns = [

    path("",BoardList.as_view(), name = 'list'),
    path("detail/<int:pk>",BoardDetail.as_view(), name = 'detail'),
    
    #평가
    path('write_add' , views.write_add, name='write_add'),
    path('write_delete/<int:id>' , views.write_delete, name='write_delete'),
]