# NSU 학식 크롤링 코드 #
import requests
from datetime import datetime

def getReplyMessage():
    strResult = ""
    if "남샤 학식" in message:
        strResult = messageNSUMeal()
        
def messageNSUMeal():
    try:
        strMessage = ""
        MealList0 = []
        MealList1 = []
        MealList2 = []

        day = datetime.date.today().weekday()
        if day == 0:
            pass
        elif day > 0 and day <= 4:
            day += 1
        else:
            raise
        
        strUrl = "https://nsu.ac.kr/api/user/board/getBoardContentSummaryList"
        bokji_data = "boardIdList=466&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4"
        cafe_data = "boardIdList=468&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4"

        bokji_response = requests.post(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=bokji_data).json()
        bokji_response = dict(bokji_response)
        mealDate = bokji_response["body"]["list"][0]["title"]
        bokji_list = bokji_response["body"]["list"][0]["properties"]["food_list"][0]
        for mealData in bokji_list.items():
            MealList0.append((f"{mealData[1]}\n"))

        cafe_response = requests.post(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=cafe_data).json()
        cafe_response = dict(cafe_response)
        cafe0_list = cafe_response["body"]["list"][0]["properties"]["food_list"][0]
        cafe1_list = cafe_response["body"]["list"][0]["properties"]["food_list"][1]
        for mealData in cafe0_list.items():
            MealList1.append((f"{mealData[1]}\n"))

        for mealData in cafe1_list.items():
            MealList2.append((f"{mealData[1]}\n"))

        strMessage = "남서울대학교 " + mealDate + " 식단표" + "\n" + ">> 천원의 아침밥 <<\n" + MealList1[day] + "\n>> 오늘의 메뉴 <<\n" + MealList0[day] + "\n>> 멀베리 <<\n" + MealList2[day]
    except:
        strMessage = "오늘은 학식을 운영하지 않습니다."
    return strMessage

getReplyMessage()
messageNSUMeal()