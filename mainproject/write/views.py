from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse


from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User

from django.core.paginator import Paginator

from .models import Account
from .models import Subject_range
from .models import Subject_code    
from .models import Subject    
from .models import Evaluation
from .models import Write_index
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from hitcount.views import HitCountDetailView


#class형 뷰의 generic view를 이용하여 구현

#main page = index.html을 보여줄것임
class BoardList(ListView) : 
    model = Subject_code, Subject
    template_name = 'board/index.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        global page
        context = super(BoardDetail, self).get_context_data(**kwargs)
        paginator = context['paginator']

        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


#강의상세page = detail.html
class BoardDetail(ListView) :
    model = Subject_code, Subject
    template_name_suffix = '_detail'
    success_url = ('/write/detail/' + str(id))
    paginate_by = 3

    def get_context_data(self, **kwargs):
        global page
        context = super(BoardDetail, self).get_context_data(**kwargs)
        paginator = context['paginator']

        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


#강의평 등록
class BoardCreate(CreateView) : 
    model = Evaluation, Subject, Write_index
    fields = ['homework_large','homework_medium','homework_small',' homework_best','team_yes','team_no','team_best','grade_good','grade_bad','grade_f',' grade_best','attendance_speak','attendance_elec','attendance_none','attendance_best','test_3','test_2','test_1','test_0','test_best']
    template_name_suffix = '_create'
    success_url =('/write/detail/' + str(id))

    #id확인
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.autor_id = self.request.user.id
        if form.is_valid() :
            #올바르다면
            form.instance.save()
            return redirect('/write/detail/' + str(id))
        else : 
            #올바르지 않다면
            return self.render_to_response({'form' : form})
    

#강의평 삭제
class BoardDelete(DeleteView) : 
    model = Evaluation, Subject, Write_index
    template_name_suffix = '_delete'
    success_url = ('/write/detail/' + str(id))

    #로그인 정보 일치할때
    def dispatch(self, request, *args, **kwargs) : 
        object = self.get_object()
        if object.author != request.user :
            messages.warning(request, '삭제할 권한 없음')
            return HttpResponseRedirect('/write/detail/' + str(id))
        else : 
            return super(BoardDelete, self).dispatch(request, *args, **kwargs)

#cnt증가
class PostCountHitDetailView(BoardDetail, HitCountDetailView):
    count_hit = True




