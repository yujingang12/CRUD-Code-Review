# 장고에서 제공하는 forms기능을 사용하기 위해 import함
from django import forms
# models.py에서 Blog모델을 쓸 것이기 때문에 가져온다!
from .models import Blog

# postfor이라는 이름의 클래스 생성
class PostForm(forms.ModelForm):
    # 클래스 안의 클래스!
    class Meta:
        # Blog라는 모델을 참고하여form을 만들었음!
        model = Blog
        # Blog라는 모델의 값 중 제목, 작성자, 콘텐츠 항목을 입력받을 것임
        fields = ['title', 'writer', 'content']