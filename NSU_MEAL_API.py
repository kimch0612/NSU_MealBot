# NSU 학식 크롤링 코드 #
import requests

def getReplyMessage():
    strResult = ""
    global NSU_BAP
    if "남샤" in message:
        if "1층" in message:
            NSU_BAP = 465
        elif "2층" in message:
            NSU_BAP = 466
        elif "3층" in message:
            NSU_BAP = 467
        elif "채움" in message:
            NSU_BAP = 468

def NSU_MEAL():
    strUrl = "https://nsu.ac.kr/api/user/board/getBoardContentSummaryList"
    mealResponse = requests.post(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data="boardIdList=%d&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4" % int(NSU_BAP)).json()
    mealResponse = dict(mealResponse)
    mealList = mealResponse["body"]["list"][0]["properties"]["food_list"][0]

    mealList['//월요일//'] = mealList['field1']
    mealList['//화요일//'] = mealList['field2']
    mealList['//수요일//'] = mealList['field3']
    mealList['//목요일//'] = mealList['field4']
    mealList['//금요일//'] = mealList['field5']
    del(mealList['corner'], mealList['field1'], mealList['field2'], mealList['field3'], mealList['field4'], mealList['field5'])

    for mealData in mealList.items():
        print(f"{mealData[0]}\n{mealData[1]}\n")

message = input("위치를 입력하세요: ")
getReplyMessage()
NSU_MEAL()