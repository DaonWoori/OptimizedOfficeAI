from django.contrib import admin
from Reviews.models import Review_Models

# admin.py : 장고 관리자(admin) 사이트를 설정하는 데 사용됨. 관리자 사이트는 데이터베이스 모델을 관리하고 관리자용 인터페이스를 제공하는 Django의 기능

# Register your models here.
admin.site.register(Review_Models)