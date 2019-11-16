from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notice
from .forms import NoticeForm
from django.contrib.auth.models import User


# Create your views here.

##메인페이지
def home(request):
        return render(request, 'mainapp/home.html')

#공지 리스트
def notice_list(request):
    notices = Notice.objects               
    return render(request, 'mainapp/notice_list.html', {'notices' : notices})

#공지 상세페이지 (R)
def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'mainapp/notice_detail.html',{'notice': notice})

#공지 등록 (C)
@login_required
def notice_register(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            return redirect('mainapp:notice_list')
    else : 
        form=NoticeForm()
        return render(request, 'mainapp/notice_register.html', {'form':form})


#공지 수정(U)
@login_required
def notice_update(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    if request.method=='POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            return redirect('mainapp:notice_detail', notice_id=notice.pk)    
    else:
        form = NoticeForm(instance=notice)
        return render(request, 'mainapp/notice_update.html', {'form':form})


#공지 삭제(D)
@login_required
def notice_delete(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    notice.delete()
    return redirect('mainapp:notice_list')


    return render(request, 'mainapp/notice_list.html')

