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
![image](https://user-images.githubusercontent.com/93918673/232786364-8ee7ca6e-7528-4089-85ff-ba48ff8938e7.png)
![image](https://user-images.githubusercontent.com/93918673/232786434-a44a6284-c94c-4054-aacf-c93e8b069e53.png)
![image](https://user-images.githubusercontent.com/93918673/232786464-19da7aa0-a636-4ac7-a5d2-1a39b157c2cc.png)
![image](https://user-images.githubusercontent.com/93918673/232786515-d93013d7-5156-419c-9901-dc8effbd07c1.png)
![image](https://user-images.githubusercontent.com/93918673/232786545-e078f7bc-b207-49b3-ad90-cee4820460b1.png)
![image](https://user-images.githubusercontent.com/93918673/232786570-6d30313d-716c-4562-a819-6f8b88140b61.png)
![image](https://user-images.githubusercontent.com/93918673/232786588-a67862fc-91af-414a-bbb0-0f18c0958136.png)
![image](https://user-images.githubusercontent.com/93918673/232786604-50e8d9b4-0944-4562-870f-7c0f3dbdcb5c.png)
![image](https://user-images.githubusercontent.com/93918673/232786630-c9cee821-4ec2-4124-a1c1-2cdeaa400954.png)
![image](https://user-images.githubusercontent.com/93918673/232786657-eb42dbae-6302-4f67-b86c-3036c037310c.png)
![image](https://user-images.githubusercontent.com/93918673/232786688-b539fb1a-baf0-4752-8db3-d3d5efc7cf1e.png)
![image](https://user-images.githubusercontent.com/93918673/232786721-e7cd51f7-e044-40ff-975a-2717688ffbdf.png)
![image](https://user-images.githubusercontent.com/93918673/214771242-e25dbfac-7027-40c6-89b7-c8dfc4c5d1aa.png)
![image](https://user-images.githubusercontent.com/93918673/232786768-2fada88b-b66a-4d12-8853-996273d27d3d.png)
![image](https://user-images.githubusercontent.com/93918673/232786798-9ab0944b-c7e8-41f1-8b98-18fb4ee6d9a8.png)
![image](https://user-images.githubusercontent.com/93918673/232786845-2af6e653-5d67-4748-bcd1-605887138adf.png)
![image](https://user-images.githubusercontent.com/93918673/232786863-f8e1a893-bb72-41bf-96b5-a69e98d45cd8.png)
![image](https://user-images.githubusercontent.com/93918673/232786879-f5cae888-9003-403a-a0ee-be7e1c7f53c2.png)
![image](https://user-images.githubusercontent.com/93918673/232786899-2086445d-4eef-4038-a72c-5207950b540b.png)
![image](https://user-images.githubusercontent.com/93918673/232786936-37096a90-9186-4225-8016-44bd64d3a49c.png)
![image](https://user-images.githubusercontent.com/93918673/232786961-7adc7515-8f08-4adb-8313-0490a2879597.png)


프로젝트에서 사용한 라이브러리와 코드들을 리뷰하였습니다. : https://lim123.tistory.com/65

face_rec\
#단계적 실행 순서
1. crop_gray.py
2. comparaion.py
3. 리셋 reset_file.py\
#main.py 모두 실행
