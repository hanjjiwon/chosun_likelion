from django.shortcuts import render,redirect
from .models import Subject_range,Subject_code,Subject

# Create your views here.
def index(request):
    return render(request, 'index.html')

def searchlist(request):
    searchtext=request.GET.get('searchtext','')
    subject=Subject.objects.all()

    if not searchtext == '':
        subject=subject.filter(subject_name=searchtext)
        # subjectrange=subject.filter(subject_range=searchtext)
        # if not subject == '':
        #     return render(request, 'searchlist.html', {'subject':subject, 'searchtext':searchtext})
        # elif not subjectrange =='':
        #     return render(request, 'searchlist.html', {'subjectrange':subjectrange})
        # # else:
        #     return redirect('index')
        return render(request, 'searchlist.html', {'subject':subject, 'searchtext':searchtext})
    else:
        return redirect('index')
