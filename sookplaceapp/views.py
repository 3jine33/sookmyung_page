from django.shortcuts import render

# Create your views here.
#게시물 리스트
def sookplace_list(request):
    return render(request, 'sookplaceapp/sookplace_list.html')

#게시물 상세페이지 (R)
def sookplace_detail(request):
    return render(request, 'sookplaceapp/sookplace_detail.html')

#게시물 등록 (C)
def sookplace_register(request):
    return render(request, 'sookplaceapp/sookplace_register.html')

#게시물 수정(U)
def sookplace_update(request):
    return render(request, 'sookplaceapp/sookplace_update.html')


#게시물 삭제(D)
def sookplace_delete(request):
    return render(request, 'sookplaceapp/sookplace_list.html')
