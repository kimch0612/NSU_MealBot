# NSU 학식 크롤링 코드 #
import requests
import json

def NSU_MEAL():
    if NSU_MSG == "1층":
        location = 465
    elif NSU_MSG == "2층":
        location = 466
    elif NSU_MSG == "3층":
        location = 467
    elif NSU_MSG == "채움":
        location = 468

    strUrl = "https://nsu.ac.kr/api/user/board/getBoardContentSummaryList"
    mealResponse = requests.post(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data="boardIdList=%d&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4" % location).json()
    mealResponse = dict(mealResponse)

    mealList = mealResponse["body"]["list"][0]["properties"]["food_list"][0]

    mealList['//월요일//'] = mealList['field1']
    mealList['//화요일//'] = mealList['field2']
    mealList['//수요일//'] = mealList['field3']
    mealList['//목요일//'] = mealList['field4']
    mealList['//금요일//'] = mealList['field5']
    del(mealList['corner'])
    del(mealList['field1'])
    del(mealList['field2'])
    del(mealList['field3'])
    del(mealList['field4'])
    del(mealList['field5'])

    for mealData in mealList.items():
        print(f"{mealData[0]}\n{mealData[1]}")
    
    file_path = "tmp1.json"
    with open(file_path, 'w') as outfile:
        json.dump(mealList, outfile, indent=4)

NSU_MSG = input("위치를 입력하세요: ")
NSU_MEAL()