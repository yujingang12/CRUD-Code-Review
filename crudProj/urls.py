from django.contrib import admin
from django.urls import path
# crudApp안에 view를 임포트 해준다.
import crudApp.views

urlpatterns = [
     # 주소창 끝에 /admin을 쳐서 접속할 수 있음. 
    path('admin/', admin.site.urls),
    #페이지 열자마자 바로 실행됨, crudApp폴더 안에 view.py안에 main이라는 함수를 적용시킨다. 이름은 main으로 할 것임
    path('', crudApp.views.main, name='main'),
    #주소창 끝에 /detail를 쳐서 접속할 수 있음, 특정 게시물을 가져오는 것이기 때문에 id를 지정해줌, crudApp폴더 안에 view.py안에 create이라는 함수를 적용시킨다. 이름은 detail으로 할 것임.
    path('detail/<str:id>/', crudApp.views.detail, name='detail'),
    #주소창 끝에 /read를 쳐서 접속할 수 있음, crudApp폴더 안에 view.py안에 read이라는 함수를 적용시킨다. 이름은 read로 할것임.
    path('read/', crudApp.views.read, name = 'read'),
    #주소창 끝에 /new/create를 쳐서 접속할 수 있음, crudApp폴더 안에 view.py안에 create이라는 함수를 적용시킨다. 이름은 create로 할 것임
    path('new/create/', crudApp.views.create, name='create'),
     #주소창 끝에 /edit를 쳐서 접속할 수 있음, 특정 게시물을 가져오는 것이기 때문에 id를 지정해줌,crudApp폴더 안에 view.py안에 edit이라는 함수를 적용시킨다. 이름은 edit으로 할 것임.
    path('edit/<str:id>/', crudApp.views.edit, name='edit'),
    #특정 게시물을 가져오는 것이기 때문에 id를 지정해줌,crudApp폴더 안에 view.py안에 delete이라는 함수를 적용시킨다. 이름은 delete으로 할 것임.
    path('delete/<str:id>/', crudApp.views.delete, name='delete'),
]
