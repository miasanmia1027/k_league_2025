from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import json

labels = [
    "득점",
    "도움",
    "슈팅",
    "유효슈팅",
    "블락된 슈팅",
    "벗어난 슈팅",
    "PA내 슈팅",
    "PA외 슈팅",
    "오프사이드",
    "프리킥 유효슈팅",
    "프리킥 크로스",
    "코너킥",
    "스로인",
    "드리블",
    "패스",
    "키패스",
    "수비진영 패스",
    "롱패스",
    "단거리패스",
    "전방패스",
    "중거리패스",
    "횡패스",
    "후방패스",
    "크로스",
    "공격진영 패스",
    "중앙지역 패스",
    "태클",
    "경합(공중)",
    "경합(지상)",
    "인터셉트",
    "클리어링",
    "차단",
    "획득",
    "블락",
    "볼미스",
    "파울",
    "피파울",
    "경고",
    "퇴장",
    "실점",
    "캐칭",
    "펀칭",
    "골킥",
    "공중 클리어링",
]

data_list_광원 = []
data_list_광주 = []
data_list_김천 = []
data_list_대구 = []
data_list_대전 = []
data_list_서울 = []
data_list_수원FC = []
data_list_울산 = []
data_list_인천 = []
data_list_전북 = []
data_list_제주 = []
data_list_포항 = []


URL = "https://data.kleague.com"

driver = webdriver.Chrome()

driver.get(URL)

driver.implicitly_wait(3)

driver.switch_to.frame(
    driver.find_element(By.CSS_SELECTOR, "html > frameset > frame:nth-child(2)")
)
# 어떻게   html > frameset > frame:nth-child(2)   이것을 가져왔는지

elements = driver.find_element(
    By.CSS_SELECTOR,
    "body > div.wrap > div.header > div > div.headerLeft > div.main-menu > ul > li:nth-child(1) > a",
).click()

time.sleep(3)

elements = driver.find_element(
    By.CSS_SELECTOR, "body > div.wrap > div.sub-menu > div > ul > li:nth-child(2) > a"
).click()

time.sleep(3)


def fetch_team_data(team_name, team_number):
    # 팀 선택 요소 클릭
    elements = driver.find_element(By.ID, f"selectTeamEmble_K{team_number}").click()

    # 데이터 로드 시간 대기
    time.sleep(3)

    # 데이터 수집
    data_list = driver.find_elements(By.CLASS_NAME, "total-search-chart-datalabel")

    # 라벨 목록 (필요한 라벨 리스트를 미리 정의)
    labels = [
        "득점",
        "도움",
        "슈팅",
        "유효슈팅",
        "블락된 슈팅",
        "벗어난 슈팅",
        "PA내 슈팅",
        "PA외 슈팅",
        "오프사이드",
        "프리킥 유효슈팅",
        "프리킥 크로스",
        "코너킥",
        "스로인",
        "드리블",
        "패스",
        "키패스",
        "수비진영 패스",
        "롱패스",
        "단거리패스",
        "전방패스",
        "중거리패스",
        "횡패스",
        "후방패스",
        "크로스",
        "공격진영 패스",
        "중앙지역 패스",
        "태클",
        "경합(공중)",
        "경합(지상)",
        "인터셉트",
        "클리어링",
        "차단",
        "획득",
        "블락",
        "볼미스",
        "파울",
        "피파울",
        "경고",
        "퇴장",
        "실점",
        "캐칭",
        "펀칭",
        "골킥",
        "공중 클리어링",
    ]

    # 데이터 저장할 리스트
    data_list_team = []

    # 수집한 데이터를 라벨과 함께 저장
    for i in range(44):
        data_list_team.append({"label": labels[i], "data": (data_list[i]).text})

    # 데이터프레임으로 변환
    df_team = pd.DataFrame(data_list_team)

    # CSV 파일로 저장
    df_team.to_csv(f"data_{team_name}.txt", index=False, encoding="utf-8-sig")

    print(f"{team_name} 팀 데이터 저장 완료!")


fetch_team_data("광원", "21")
fetch_team_data("광주", "22")
fetch_team_data("김천", "35")
fetch_team_data("대구", "17")
fetch_team_data("대전", "10")
fetch_team_data("서울", "09")
fetch_team_data("수원FC", "29")
fetch_team_data("울산", "01")
fetch_team_data("인천", "18")
fetch_team_data("전북", "05")
fetch_team_data("제주", "04")
fetch_team_data("포항", "03")


time.sleep(3)


driver.close()
