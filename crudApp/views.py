from django.shortcuts import render, redirect, get_object_or_404
# models.py에서 Post모델을 쓸 것이기 때문에 가져온다!
from .models import Post
#forms.py에서 PostForm를 가져온다.
from .forms import PostForm
# 장고에서 제공하는 시간기능을 사용하기 위함!
from django.utils import timezone

# Create your views here.

# def로 함수선언~ main이란 이름의 함수는 요청받았을 때 
# 반환한다(return), 불러옴으로써(render) 요청받았을 때 (request), crud파일에 main.html이란 html파일을 띄운다!
#메인페이지
def main(request):
    return render(request, 'crudApp/main.html')

# def로 함수선언~ new이란 이름의 함수는 요청받았을 때 
# 반환한다(return), 불러옴으로써(render) 요청받았을 때 (request), crud파일에 new.html이란 html파일을 띄운다!
#글쓰기페이지
def new(request):
    return render(request, 'crudApp/new.html')

#글쓰기 함수
# def로 함수선언~ create이란 이름의 함수는 요청받았을 때 
def create(request):
    #view에서 다시 한번 method를 확인 한뒤
    if request.method == 'POST':
        # form의 입력값 유효성 검증을 시작
        form = PostForm(request.POST)
        #우리가 post형식으로 요청받은 form이 forms.py에서 작성받기로 한 정보를 다 받았는 지 유효성검사!
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            #form이 잘 입력되었다면 read으로 이동!
            return redirect('read')
            
    #그렇지 않는다면 폼을 다시 입력받음
    else:
        form = PostForm
        return render(request, 'crudApp/new.html', {'form':form})

#읽기페이지
def read(request):
    posts = Post.objects
    return render(request, 'crudApp/read.html', {'posts':posts})

#디테일페이지
# def로 함수선언~ detail이란 이름의 함수는 특정한 값(id)를 요청받았을 때 
def detail(request, id):
    #blog모델에서 id값을 Post라는 변수에 담아 가져오려 하는데, id값을 제대로 가져오지 못하면 404에러를 일으킬 것.
    post = get_object_or_404(Post, id=id)
      #post의 객체가 담겨있는 post라는 변수를 html에서는 post라는 변수로 표현하겠다!
    return render(request, 'crudApp/detail.html', {'post':post})

#수정페이지
# def로 함수선언~ edit이란 이름의 함수는 특정한 값(id)를 요청받았을 때 
def edit(request, id):
    #post모델에서 id값을 Post라는 변수에 담아 가져오려 하는데, id값을 제대로 가져오지 못하면 404에러를 일으킬 것.
    post = get_object_or_404(Post, id=id)
    #view에서 다시 한번 method를 확인 한뒤
    if request.method == 'POST':
        #form의 입력값 유효성 검증을 시작, 이때 instance는 수정할 글이 어떤 글인지 글의 id를 함수에게 설명
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            #form이 잘 입력되었다면 read로 이동!
            return redirect('read')

    #그렇지 않는다면 폼을 다시 입력받음
    else:
        form = PostForm(instance=post)
        return render(request, 'crudApp/edit.html', {'form':form})

#삭제 함수
#def로 함수선언~ delete이란 이름의 함수는 특정한 값(id)를 요청받았을 때 
def delete(request, id):
    #post모델에서 id값을 Post라는 변수에 담아 가져오려 하는데, id값을 제대로 가져오지 못하면 404에러를 일으킬 것.
    post = get_object_or_404(Post, id=id)
    #특정 id값을 가진 데이터를 삭제해주는 함수.
    post.delete()
    #삭제를 한 다음에 다시 read페이지를 띄운다.
    return redirect('read')