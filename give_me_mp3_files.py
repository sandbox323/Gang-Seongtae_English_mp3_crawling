import requests
import os

# 변수 초기화 부분
path = 'C:/Users/user/Downloads/mp3_files/'  # mp3파일이 저장될 경로
s_d = 0     # s_d(시작 일자) = 0(책의 맨처음 일자)
l_d = 60    # l_d(끝 일자) = 60(책의 맨마지막 일자)

# 다운받을 범위를 입력받는 부분
ran = input("다운받을 mp3의 시작 일자와 끝 일자을 입력, (ex> 1 2, all을 입력하면 모두 다운로드) :")
if ran not in ['all', 'ALL', 'All']:
    s_d, l_d = map(int, ran.strip().split(' '))

# mp3파일이 저장될 폴더 생성 부분
try:
    os.makedirs(path)
except OSError:
    if os.path.isdir(path) is True:
        if input("<!> 이미 폴더가 존재합니다. 그곳에 저장할까요? (y/n또는 아무키) : ") not in ['y', 'Y']:
            print("<!> 폴더를 생성하지 못했습니다. 다운로드 파일로 경로를 변경합니다...")
            path = 'C:/Users/user/Downloads/'

# 실제 다운로드(크롤링) 부분
for day in range(s_d, l_d+1):
    with open(path + f'Day_{day:02}.mp3', 'wb') as f:
        f.write(requests.get(f'http://mp3.englishbus.co.kr/KST_VOCA/MP3/1/Day_{day:02}.mp3').content)
        print(f'Day_{day:02}.mp3 다운로드 완료')
