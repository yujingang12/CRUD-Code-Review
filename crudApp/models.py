# 장고 데이터베이스에서 모델(여기!)로 가져온다. 
from django.db import models
# 프로젝트에서 사용하는 user를 import하기 위해 settings를 가져온다!
from django.conf import settings

# Create your models here.

# 모델은 모다? 데이터를 저장할 수 있게 해주는 곳! 아래 Post라는 클래스를 만들어 title, pub_date, writer, content속성을 갖도록 한다.
# 이것은 각각 제목, 날짜, 작성자, 콘텐츠(내용)을 뜻합니다.
# writer에 null을 방지하기위해 디폴트를 "닉네임을 입력하시오"로 설정해둠
#  모델을 변경한 뒤에는 makemigrations!
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    writer = models.CharField(max_length=15, default="닉네임을 입력해주세요")
    body = models.TextField()
# def로 함수를 선언하고~ 모델 클래스의 객체를 그대로(self) 문자열(str)로 반환한다. 
# 만약 __str__(self) 이하가 없다면 글쓴대로 제목이 나오지 않음. Blog object라고 뜸.
    def __str__(self):
        return self.title