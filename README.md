# OptimizedOfficeAI

## 목차

1. [프로젝트 소개](#프로젝트-소개)
2. [프로젝트 배경](#프로젝트-배경)
3. [프로젝트 목표](#프로젝트-목표)
4. [문제 인식](#문제-인식)
5. [프로젝트 진행 과정](#프로젝트-진행-과정)
6. [프로젝트 기능 구현](#프로젝트-기능-구현)
7. [결과 정리](#결과-정리)
8. [프로젝트 회고](#프로젝트-회고)

### 프로젝트 소개
```
AI 모델을 활용한 사무용품 리뷰 사이트인 Ol'reviews 개발

- 프로젝트 기간: 2023.06.07 ~ 2023.06.30
- Skills: Tensorflow, Django, YOLOv8
- 출처: 코드스테이츠 AIB 부트캠프
```

### 프로젝트 배경

기업들을 대상으로 사무 용품을 판매하는 O사는 제품 구매자의 사진 리뷰를 통해 더 많은 서비스 이용자를 확보하는 것 이 목표입니다. 하지만 O 사의 경우 지금까지 이미지 데이터를 무분별하게 쌓고만 있었던 상황이며, 대부분 사내 제품 홍보 용으로 사용되는 이미지가 주로 쌓였습니다.

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/d4049ce7-977a-4aca-9871-0a55be266d2a)


이러한 상황에서 O 사는 추후 수집 될 이미지 데이터 분류를 위해 3가지 도메인에 대한 분류, 31가지 오브젝트에 대한 분류 AI Model 을 구현해 놓았습니다.

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/c89a8f02-7d50-4a56-b347-df0a3d37ca50)


하지만 사전에 구현된 AI 소프트웨어는 사내 직원 평가에서 ‘AI Model 성능’ 과 ‘AI 소프트웨어 사용 방법’ 에 대하여 부정적 VOC 가 누적된 상황입니다.

---

### 프로젝트 목표

**주 목표**

기존 사무 용품 분류 AI 소프트웨어의 떨어지는 성능과 AI 소프트웨어 사용 방법에 대한 부정적 VOC를 개선함으로써 더 많은 사용자를 확보하는 것

**세부 목표**

-   이미지 데이터의 탐색적 데이터 분석
-   AI 모델 성능 향상
-   UI/UX 개선

---

### 문제 인식

**모델**

-   기존 모델의 구조
    -   입력 계층 정보 - 입력 벡터 차원 수 : 30,000( ※ 100 \* 100 \* 3 )
    -   첫 번째 은닉 계층 정보 - Node: 64, Activation Function: ReLU
    -   두 번째 은닉 계층 정보 - Node: 32, Activation Function: ReLU
    -   세 번째 은닉 계층 정보 - Node: 10, Activation Function: ReLU
    -   출력 계층 정보 - 출력 벡터 차원 수: 3 (도메인), 31 (오브젝트) , Activation Function: Softmax
      
-   기존 모델의 성능
    -   도메인 정확도: 약 0.85
    -   오브젝트 정확도: 약 0.2
      
-   기존 모델의 단점
    -   파이썬과 넘파이 만으로 구현되어 있어 성능 향상을 위한 여러 기법을 테스트하는데 어려움이 존재  
         → tensorflow 등의 라이브러리를 활용
    -   오브젝트를 분류에 관한 성능이 너무 낮음  
        → 기존 단일 모델을 사용한 것에 비해 도메인과 오브젝트 분류를 위한 두 가지 모델을 선정
    -   ipynb 파일을 활용해서 실행해야하는 번거로움이 존재  
        → 사용자가 편하게 서비스를 이용할 수 있도록 웹 페이지를 구현

**데이터 셋** 

-   기존 데이터 셋
    -   도메인: 오피스(2,800개) / 스마트폰(500개) / 웹캠(800개)
    -   오브젝트:
      
-   기존 데이터 셋 단점
    -   오피스(사내 제품 홍보용) 이미지가 많이 수집되어 불균형한 데이터 분포를 보임  
        →  스마트폰과 웹캠의 데이터를 합쳐서 실사용 사진으로 라벨링을 묶을 경우, 불균형을 어느 정도 완화할 수 있을 것이라 예상  
        → 부족한 부분의 데이터만 추가로 수집
    -   오브젝트 별 이미지가 불균형한 데이터 분포를 보임  
        → 부족한 오브젝트에 대한 데이터 추가 수집
    -   추가로 수집된 이미지 중 전혀 상관없는 이미지들이 수집  
        → 데이터 전처리 필요
    -   YOLO 모델을 사용하기 위한 바운딩 박스 처리 필요  
        → Robowflow를 통해 바운딩 박스를 작업하며 관련없는 데이터 삭제

---

### 프로젝트 진행 과정

**팀 구성 및 역할**

| 이름 | 담당 업무 |
| --- | --- |
| 팀원 1 | \- YOLOv8  모델 제작   \- 데이터 수집 및 전처리 |
| 팀원 2 | \- CNN 모델 제작   \- 데이터 수집 및 전처리 |
| 팀원 3 | \- 웹 페이지 개발   \- 데이터 수집 및 전처리 |
| 팀원 4(본인) | \- 웹 페이지 개발   \- 데이터 수집 및 전처리   \- 웹 페이지 배포 |

**프로젝트 일정**

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/f7ba7a6e-6fe7-4f4d-9759-97e525c2e426)

---

### 프로젝트 기능 구현

> 왜 Django인가?  
>   
> - 파이썬을 활용하여 웹 페이지를 구현하는 것이 가능  
> - 회원가입, 로그인 등 기본적으로 Django 자체에 구현된 기능들이 많아 쉽게 구현 가능  
> - CSRF와 같은 보안 기능이 기본적으로 제공  
> - 상속 기능을 지원해서 효율적인 코드 작성이 가능

**Django 프로젝트 구조**

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/aaa93b5b-f231-43d7-9856-2f6e3aa52964)


**Ol'reviews 소개** 

> 모든 리뷰를 담는다는 의미인 all + reviews가 합쳐진 뜻으로 건강한 리뷰 문화를 지향하는 서비스를 의미한다. 사용자들은 사무용품 리뷰 텍스트와 사진을 업로드하고 다양한 사용자들과 리뷰를 공유할 수 있다. AI 모델을 통해 사용자들이 업로드한 이미지를 분류하고 그 결과를 활용해서 사용자가 원하는 조건의 리뷰만을 조회하는 것이 가능하다.

**회원 가입 및 로그인**

- Django에서 제공하는 `django.contrib.auth.models.User` 사용

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/cf388461-44e2-4d87-81e4-6274b743e58a)


**리뷰 작성**

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/7b70feda-0a31-4a01-879a-6f31e045de9c)


- 제목과 내용의 경우 입력할 수 있는 최대 길이를 제한
- 별점은 1점에서 5점까지 선택 가능
- 이미지의 경우, validator를 통해 3가지 확장자만 업로드 가능

  ```
  imgvalidator = FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'], 
                 message='다음과 같은 형식의 확장자만 사용 가능합니다(jpg, png, jpeg)')
  ```

- 한글 이름의 파일을 업로드 시, media 폴더에 저장된 이미지를 불러오는 과정에서 오류 발생 -> uuid4를 활용하여 랜덤한 값으로 이름을 변경해주는 함수 추가
  
  ```
  # instance : Feed 모델에서 __str__로 반환해주는 값 현재는 title로 지정, filename : 원본 파일명
  def rename_imagefile_to_uuid(instance, filename): 	
      # 파일 저장 위치 설정
      upload_to = f'review_images/'
      
      # 원본 파일명 text.jpg->[text, jpg]로 나누어주고 -1 번째 값만 ext에 담아주기
      ext = filename.split('.')[-1] 
      
      # 50da5daca34d4802a771047ee463c234 이런 형식에 임의에 이름 생성
      uuid = uuid4().hex 
      
      # '{uuid}.{ext}' -> 50da5daca34d4802a771047ee463c234.jpg
      filename = '{}.{}'.format(uuid, ext) 
  
      # DB에 저장할 값을 리턴
      return os.path.join(upload_to, filename
  ```

- Django form을 통해 데이터를 입력받고, 유효성 검증 후 DB에 반영
- 사용자로부터 데이터를 입력 받았을 때, 미리 학습해 둔 두 가지 모델(YOLO, CNN)을 호출하여 이미지 분류 실행 및 DB에 반영

**리뷰 상세보기**

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/4ff070c8-f506-436b-be4e-8297655d4c7d)


- 리뷰 제목, 작성자, 별점, 작성일, 내용 화면에 출력
- yolo 모델을 통해 예측한 오브젝트 분류 결과를 함께 출력
    - 여러 개의 오브젝트가 인식된 경우 모두 출력
    - 중복된 물체가 여러 개 있을 경우 하나만 출력
    - YOLO가 오브젝트를 찾지 못할 경우 출력하지 않음
- User 모델과 Review 모델의 ID 값을 확인하여 자신이 작성한 글에서만 수정, 삭제 버튼 활성화

**리뷰 수정**

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/fb8db00f-d332-4d10-a7d5-7d6deeb3a671)


- 작성한 내용을 instance 파라미터를 활용해 form에 그대로 출력

**리뷰 삭제**

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/4a4c017c-540f-4d59-a58c-d8c8742ff580)


- 삭제 버튼 클릭 시 부트스트랩 모달 기능을 통해 팝업창 활성화

**리뷰 조회**

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/87ff3c7a-ac66-49a0-b660-228f449ec6b7)


- 드롭다운을 통해 선택한 조건이 GET 방식으로 전달

---

### 결과 정리

**도메인 분류 모델**

- 구현 모델

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/f751d945-600e-4cc0-b989-4515fa7f81af)


- 이미지 증강
    - 사용 데이터 수: 총 6,000장
    - 좌우 반전

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/4ea9e028-e7e3-47ea-aa8d-9aa698dcdef8)


- 모델 성능 개선

| 기존 모델 정확도 | 개선 모델 정확도 |
| --- | --- |
| 0.850 | 0.986 |

**오브젝트 분류 모델**

- 사용 모델: YOLO v8

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/bf78e647-8dc9-4a38-9582-1944f5a4f784)


- 이미지 증강
    - 사용 데이터 수: 총 7,867장
    - 좌우 반전, 90도 회전

![image](https://github.com/DaonWoori/OptimizedOfficeAI/assets/88466357/cc93e73e-050a-416e-932d-32ed16756afd)


- 모델 성능 개선

| 기존 모델 정확도 | 개선 모델 Precision |
| --- | --- |
| 0.2 | 0.913 |

**UI/UX 개선**

- 리뷰를 업로드하고 리뷰를 조회할 수 있는 리뷰 사이트 구현
- AI 모델의 분류 결과를 바탕으로 원하는 조건의 리뷰만 빠르게 조회 가능
- ngrok을 활용해 배포된 환경에서 동작 확인

**시연 영상**

[<iframe src="https://play-tv.kakao.com/embed/player/cliplink/439899838?service=daum_tistory" width="860" height="484" frameborder="0" allowfullscreen="true"></iframe>](https://tv.kakao.com/v/439899838)

---

### 프로젝트 회고

**향후 개선 사항**

- 리뷰 작성 시 포인트 기능 추가
- 마이 페이지 구현
- 댓글 기능 구현 및 댓글 추천 기능 구현
