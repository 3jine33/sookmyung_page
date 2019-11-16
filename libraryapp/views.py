from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

#책 리스트
def book_list(request):
    return render(request, 'libraryapp/book_list.html')

#책 상세페이지 (R)
def book_detail(request):
    return render(request, 'libraryapp/book_detail.html')

#책 등록 (C)
def book_register(request):
    return render(request, 'libraryapp/book_register.html')

#책 수정(U)
def book_update(request):
    return render(request, 'libraryapp/book_update.html')

#책 삭제(D)
def book_delete(request):
    return render(request, 'libraryapp/book_list.html')

#책 필터링
def book_result(request):
    return render(request, 'libraryapp/book_result.html')