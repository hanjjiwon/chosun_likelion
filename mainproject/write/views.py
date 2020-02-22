from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User

from django.core.paginator import Paginator

from .models import Account
from .models import Subject_range
from .models import Subject_code    
from .models import Subject    
from .models import Evaluation
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from hitcount.views import HitCountDetailView


#class형 뷰의 generic view를 이용하여 구현

#main page = index.html을 보여줄것임
class BoardList(ListView) : 
    model = Subject_code, Subject
    template_name = 'board/index.html'


#강의상세page = detail.html
class BoardDetail(ListView) :
    model = Subject_code, Subject
    template_name = 'write/detail + <int:pk>.html'


#cnt증가
class PostCountHitDetailView(BoardDetail, HitCountDetailView):
    count_hit = True




#강의평쓰기 _ 존나수정해야함
@login_required
def write_add(request ) : #과목 번호
    if request.method == "POST" :
         #양식
         return redirect('/photo/detail/' + str(photo_id))
    else : 
        return HttpResponse('잘못된 접근')


#강의평 삭제
def write_delete(request, writer_id ) :
    write = get_object_or_404(Write, pk = writer_id )
    if request.user == write.user:
        if request.method == "POST": 
            write.delete()
            return redirect('/write/detail/' +str(write.post.id ))
    return HttpResponse('잘못된 접근')