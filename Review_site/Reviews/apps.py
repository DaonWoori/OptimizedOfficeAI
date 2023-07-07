from django.apps import AppConfig

# apps.py : 각 애플리케이션(App)에 대한 구성을 정의하는 파일


class UploadConfig(AppConfig):
    # default_auto_field: 장고에서 사용하는 기본 자동 생성 필드 설정
    default_auto_field = 'django.db.models.BigAutoField' 
     
    # name: 앱의 이름
    name = 'Reviews'
