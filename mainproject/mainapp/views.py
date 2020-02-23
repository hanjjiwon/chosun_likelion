from django.shortcuts import render,redirect
from .models import Subject_range,Subject_code,Subject

# Create your views here.
def index(request):
    return render(request, 'index.html')

def searchlist(request):
    searchtext=request.GET.get('searchtext',' ')
    subject=Subject.objects.all()

    if not searchtext == '':
        subject=subject.filter(subject_name__icontains=searchtext)
        return render(request, 'searchlist.html', {'subject':subject})
    else:
        return redirect('index')
