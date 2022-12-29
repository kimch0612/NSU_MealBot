# NSU 학식 크롤링 코드 #
from bs4 import BeautifulSoup
from urllib import parse
import requests, json

def NSU_Meal():
    timeout = 5
    url = parse.urlparse('https://nsu.ac.kr/api/user/board/getBoardContentSummaryList')
    headers = {'Content-Type' : 'application/x-www-form-urlencoded;'}
    data = {'boardIdList=468&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4'}
    #465 1층, 466 2층, 467 3층, 468 채움
    res = requests.post(url, data=data, headers=headers, timeout=timeout)
    print(res)

NSU_Meal()