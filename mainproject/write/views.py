from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Subject_code, Subject, Write_index
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse
# Create your views here.

def write(request):
    return render(request, 'write.html')


class CommenttList(ListView):
    model = Subject_code, Subject
    template_name_suffix = '_list'

class CommentCreate(CreateView):
    model = Subject_code, Subject, Write_index
    fields = ['subject_name', 'professor', 'homework','team','grade','attendance','test',]
    template_name_suffix = '_create'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class CommentUpdate(UpdateView):
    model = Subject_code, Subject, Write_index
    fields = ['subject_name', 'professor', 'homework','team','grade','attendance','test',]
    template_name_suffix = '_update'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PhotoUpdate, self).dispatch(request, *args, **kwargs)


class CommentDelete(DeleteView):
    model = Subject_code, Subject, Write_index
    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PhotoDelete, self).dispatch(request, *args, **kwargs)


class CommentDetail(DetailView):
    model = Subject_code, Subject, Write_index
    template_name_suffix = '_detail'


class CommentMyList(ListView):
    model = Subject_code, Subject, Write_index
    template_name = 'photo/photo_mylist.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(PhotoMyList, self).dispatch(request, *args, **kwargs)


def index(request):
    sort = request.GET.get('sort', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

    if sort == 'likes':
        memos = Memos.objects.annotate(like_count=Count(
            'likes')).order_by('-like_count', '-update_date')
        return render(request, 'memo_app/index.html', {'memos': memos})
    elif sort == 'mypost':
        user = request.user
        memos = Memos.objects.filter(name_id=user).order_by(
            '-update_date')  # 복수를 가져올수 있음
        return render(request, 'memo_app/index.html', {'memos': memos})
    else:
        memos = Memos.objects.order_by('-update_date')
        return render(request, 'memo_app/index.html', {'memos': memos})