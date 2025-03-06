from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

URL = "https://www.kleague.com/record/team.do"

driver = webdriver.Chrome()

driver.get(URL)

driver.implicitly_wait(3)

season = driver.find_element(By.ID,"year").click()
time.sleep(1)
team_2024 = driver.find_element(By.XPATH, "//*[@id='year']/option[2]").click()

def get_score():
    no_name1 = []
    no_name2 = []
    name_list1 =[]
    name_list2 =[]
    for num in range(1,7):
        name_ts1 = driver.find_element(By.XPATH, f"//*[@id='ts1']/tbody/tr[{num}]/td[2]/a/ta")
        name_ts2 = driver.find_element(By.XPATH, f"//*[@id='ts2']/tbody/tr[{num}]/td[2]/a/ta")
        name_list1.append(name_ts1.text)
        name_list2.append(name_ts2.text)
        for i in range(4,11):
            no_name_ts1 = driver.find_element(By.XPATH, f"//*[@id='ts1']/tbody/tr[{num}]/td[{i}]")
            no_name_ts2 = driver.find_element(By.XPATH, f"//*[@id='ts2']/tbody/tr[{num}]/td[{i}]")
            no_name1.append(no_name_ts1.text)
            no_name2.append(no_name_ts2.text)
    every_name = name_list1 + name_list2
    every_no_name= no_name1+ no_name2
    every_list = [] 
    # 이거는 4개 단위로 나누어 주는 코드
    def split_list(lst, n=7):
        return [lst[i:i + n] for i in range(0, len(lst), n)]

    split_result = split_list(every_no_name, 7)

    for i_2 in range(12):  # 팀 개수
        every_list.append({
            "name": every_name[i_2],
            "points": split_result[i_2][0],
            "win": split_result[i_2][1],
            "draw": split_result[i_2][2],
            "loss": split_result[i_2][3],
            "goals": split_result[i_2][4],
            "loss_goal": split_result[i_2][5]
        })
    return every_list

time.sleep(3)

def save_to_csv():
    data = get_score()  # get_score 함수 실행하여 데이터 가져오기
    df = pd.DataFrame(data)  # 데이터프레임으로 변환
    df.to_csv("2024_team_data/2024_score_data.csv", index=False, encoding="utf-8-sig")  # CSV 파일로 저장

save_to_csv()


driver.close()




