'''
find face and crop, grayscale

실행 시간 : 0.5425937175750732
'''
import os
import cv2
import numpy as np
import face_recognition
import dlib
import shutil
import time
import re
import random
import string
from pathlib import Path
# start = time.time()
# print("time :", time.time() - start)


def make_path_list(path): # 경로 만들기
    base_path = path
    path_file = os.listdir(path)
    path_list = [base_path + file for file in path_file]
    return path_list


def crop_gray(color_img_path, gray_img_save_path):
    
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # 얼굴 탐지모델
    
    img_name = color_img_path.split('/')[-1] # 이미지 이름 ex) ian.jpg
    img_src = cv2.imread(color_img_path) # 이미지 불러오기

    # 회색으로 바꿈
    # gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    # face = face_detector.detectMultiScale(gray, 1.3, 5)
    face = face_detector.detectMultiScale(img_src)
    
    source = color_img_path # 현재 경로
    destination = 'images/unrecognized/' + img_name # unrecognized 폴더 경로
    
    if len(face) < 1:
        # 탐지 안된 사진은 unrecognized 폴더로 이동
        if img_name not in os.listdir(gray_img_save_path):
            print(img_name.split('.')[-2], '가 아닌 다른 사진을 넣어주세요')
            shutil.move(source, destination) # 파일 이동
    else:
        x, y, w, h = face[0]
        cv2.rectangle(face, (x,y), (x+w,y+h), (255,0,0), 2)
        # cv2.imwrite(gray_img_save_path + img_name, gray[y:y+h,x:x+w])
        cv2.imwrite(gray_img_save_path + img_name, img_src[y:y+h,x:x+w])
        
        # 방금 저장한 이미지 불러오기
        try:
            saved_img = face_detector.detectMultiScale(cv2.imread(gray_img_save_path + img_name))
            # 귀나 눈 사진을 저장하면 삭제 후 원본 사진은 unrecognized 폴더로 이동
            if len(saved_img) < 1:
                shutil.move(source, destination)
                os.remove(gray_img_save_path + img_name)
            cv2.destroyAllWindows()
        except:
            print('FileNotFoundError : saved_img')
            return
        
        
    return

def crop_run():
    try:
        color_img_path = 'images/color_faces/'
        gray_img_path = 'images/crop_gray_faces/'
        color_now_img_path = 'images/color_now_face/'
        gray_now_img_path = 'images/crop_gray_now_face/'

        for c in make_path_list(color_img_path):
            name = Path(c).stem
            extension = os.path.splitext(c)
            
            Korean = re.findall('[가-힣]', name) # 한글 찾기
            # 한글 찾아서 랜덤 영문자로 파일 이름 바꾸기 
            if Korean:
                for i in Korean:
                    name = name.replace(i, f'{random.choice(string.ascii_letters)}')
                file_oldname = c
                file_newname_newfile = color_img_path + name + '.' + extension
                
                os.rename(file_oldname, file_newname_newfile)
            else:
                pass
            if extension == 'png' or 'jpg': # 확장자 확인
                crop_gray(c, gray_img_path)
            else:
                print('Allow png, jpg extensions only')
            
            
        for c in make_path_list(color_now_img_path):
            name = Path(c).stem
            extension = os.path.splitext(c)
            
            Korean = re.findall('[가-힣]', name) # 한글 찾기
            # 한글 찾아서 랜덤 영문자로 파일 이름 바꾸기 
            if Korean:
                for i in Korean:
                    name = name.replace(i, f'{random.choice(string.ascii_letters)}')
                file_oldname = c
                file_newname_newfile = color_img_path + name + '.' + extension
                
                os.rename(file_oldname, file_newname_newfile)
            else:
                pass
            if extension == 'png' or 'jpg': # 확장자 확인
                crop_gray(c, gray_now_img_path)
            else:
                print('Allow png, jpg extensions only')
        
    except:
        print('FileNotFoundError : img')
        return

'''각자 실행할 때'''  
if __name__ == '__main__':
    crop_run()