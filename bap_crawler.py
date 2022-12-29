# NSU 학식 크롤링 코드 #

import requests

def NSU_MEAL():
    strUrl = "https://nsu.ac.kr/api/user/board/getBoardContentSummaryList"

    mealResponse = requests.post(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data="boardIdList=468&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4").json()
    mealResponse = dict(mealResponse)

    mealList = mealResponse["body"]["list"][0]["properties"]["food_list"][0]

    for mealData in mealList.items():
        print(f"Field : {mealData[0]}\n{mealData[1]}")

NSU_MEAL()