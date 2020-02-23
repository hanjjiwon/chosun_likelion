from django.shortcuts import render, redirect, get_object_or_404, HttpResponse #404예외처리
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
# from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Lec, Subject_range, Subject_code, Subject, Evaluation, Write_index#모델(클래스 불러오기)
from .forms import BlogForm
#데이터 처리-> 함수 정의 나중에 템플릿에서 이 함수들을 사용하면 됨.

def home(request):
    lecs = Lec.objects#모델로 부터 lec 클래스의 객체(객체목록=쿼리셋)를 전달받아서 변수에 저장.
    #쿼리셋을 메소드를 사용해서 정렬이나 기능을 처리

    #페이지네이션
    lec_list = Lec.objects.all()
    paginator = Paginator(lec_list, 3) #객체 list를 3개씩 구분
    page = request.GET.get('page') #req한 페이지를 get방식으로 얻어와 page라는 변수에 넣고
    posts = paginator.get_page(page)#페이지 번호(page)에 해당하는 페이지를 가져옴. 
    return render(request, 'home.html', {'lecs' : lecs, 'posts':posts})

    #모델이름.쿼리셋(objects).메소드

def detail(request, lec_id):
    lecs_fb = get_object_or_404(Lec, pk=lec_id)#(사용할클래스이름,pk값) 특정 강의id(int형)의 객체를 가져옴
    return render(request, 'lec-feedback.html', {'lecs_feedback' : lecs_fb})

def write(request):#글쓰기페이지 보여주는 함수
    if request.user.is_authenticated:
        return render(request, 'write.html')

#@login_required
def create(request):#입력받은 내용을 디비에 넣어주는 함수
    lec = Lec()#lec객체 생성
    # lec.author = request.user#작성한 사람
    lec.title = request.GET['title']#write에서 입력한 제목을 가져와 생성한 lec객체에 담아줌
    lec.body = request.GET['body']
    lec.pub_date = timezone.datetime.now()#현재시간
    lec.save()#객체를 디비에 저장. lec.delete() 객체를 디비에서 삭제
    return redirect('/강의/'+str(lec.id))#위의 작업들을 다 하고 이 url로 넘기기. id는 정수니까 문자열로 형변환.


# blog = Blog()
#     blog.author = request.user
#     blog.title = request.POST['title']
#     blog.body = request.POST['body']
#     blog.pub_date = timezone.datetime.now()
#     blog.save()
#     return redirect('/blog/'+str(blog.id)) 


def fb_create(request):
    if request.method == 'POST':
#입력받은 내용을 디비에 넣어주는 함수
        clec = Evaluation()#lec객체 생성
        #form = BlogForm(request.POST)#POST방식으로 들어온 data를 form에 넣어줌.
        if form.is_valid():
        # lec.writer_id = 
                # lec.author = request.user#작성한 사람
            clec.evaluation_text = request.POST['text']
            clec.pub_date = timezone.datetime.now()#현재시간
            clec.save()#객체를 디비에 저장. lec.delete() 객체를 디비에서 삭제
        return redirect('/강의/'+str(clec.id))
    else:
        return render(request, 'write.html')




#평가글 삭제
# @login_required
def feedback_delete(request, writer_id):
    texts = get_object_or_404(Evaluation, pk=writer_id)
    if request.user == texts.user:
        if request.method == 'POST':
            subject_id = texts.subject.id
            texts.delete()
            return redirect('/강의/' + str(subject_id))
    return HttpResponse('잘못된 접근') 

#검색후, 선택한 과목의 수강평가 정보 보여주기.
# def search_subject_detail(request, subject_id):
#     search_subject = get_object_or_404(Subject, pk=subject_id)
#     #(사용할클래스이름,pk값) 특정 강의id(int형)의 객체를 가져옴
#     return render(request, 'lec-feedback.html', {'search_subject' : search_subject})




#강의평쓰기에서 선택한 옵션을 강의에 적용하게하기

# class LecView(ListView):
#     model = Evaluation

