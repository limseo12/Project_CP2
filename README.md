# 안면인식 프로젝트 입니다
Project_CP2 기업협업 프로젝트 (후케어스)

기간 : 2022.07.18 ~ 2022.08.05 총 17일 (주말포함x)

데이터 : 테스트를 할 때 배우 구인구직 사이트 https://www.filmmakers.co.kr/\
배우들의 프로필 사진을 가져와 테스트를 하였고 몇 개의 연예인 사진들도 사용하였습니다.\
연예인들의 사진의 경우 고퀄리티 사진이 많아 배우들의 구인구직 사이트에 있는 프로필사진을 우선순위로\
그 중 고퀄리티 사진과 휴대폰 셀카사진들을 적절히 섞어 사용하였습니다.

Part : 프로젝트에서 모델 서치,테스트 데이터 수집, 모델 테스트 역할을 맡았습니다.

내용 : 기업측에서 시니어를 위한 데이팅 프로그램을 만들었으며, 챗봇팀과 안면인식팀 중 안면인식팀 에서\
로그인시 등록된 프로필 사진을 바탕으로 현재 나의 사진과 동일인물인지 아닌지를 판단하여 로그인 하는방식으로 만들어져 있는 기존 안면인식 모델을 교체, 성능을 개선하여\
정확도 향상과 인식시간 단축을 하는 방향으로 프로젝트가 진행되었습니다.\
여러가지 모델들을 비교 하였으며 (VGG-Face, Open-Face, Facenet512, dlib, ArcFace, DeepFace, DeepID)\
최종적으로 기존에 있는 이미지를 자르고 회전시키는 부분은 같은 모델을 사용하고(cv2)\
인식하는 부분의 모델만 교체를 해주었더니(face_recognition) 정확도 향상과 함께 인식시간이 단축되었습니다.


모델 : 얼굴을 정렬하는부분은 cv2를 사용하였습니다.\
       얼굴을 추출하는 부분에서 파이썬 패키지 중 face_recognition 이라는 것으로 교체하였습니다. 모델이 가볍고 빠르게 작동합니다.
      

PPT : 

![image](https://user-images.githubusercontent.com/93918673/214771178-761d434c-5eb7-4374-9ae6-6d163231d894.png)
![image](https://user-images.githubusercontent.com/93918673/214771206-c9d5effa-4820-4ce8-9c6a-658600d303bb.png)
![image](https://user-images.githubusercontent.com/93918673/214771217-ccc5de37-d311-462e-a731-779090d44104.png)
![image](https://user-images.githubusercontent.com/93918673/214771226-f33f2bbd-ae19-4032-a0b6-e1b60df81c39.png)
![image](https://user-images.githubusercontent.com/93918673/214771242-e25dbfac-7027-40c6-89b7-c8dfc4c5d1aa.png)
![image](https://user-images.githubusercontent.com/93918673/214771255-2085fa68-73a6-4fc2-be5a-6f59e9901fa9.png)
![image](https://user-images.githubusercontent.com/93918673/214771266-f96a22c2-fb1c-4f14-b3e1-68464bf4d304.png)
![image](https://user-images.githubusercontent.com/93918673/214771276-99ae2d39-bc9d-4454-8d64-dd769bf01dce.png)
![image](https://user-images.githubusercontent.com/93918673/214771285-6e39c573-bc04-435f-b6b0-e755dfb2a82a.png)
![image](https://user-images.githubusercontent.com/93918673/214771298-c68e3477-fd9e-4d08-b5eb-490ff5059d98.png)


프로젝트에서 사용한 라이브러리와 코드들을 리뷰하였습니다. : https://lim123.tistory.com/65

face_rec\
#단계적 실행 순서
1. crop_gray.py
2. comparaion.py
3. 리셋 reset_file.py\
#main.py 모두 실행
