

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


labels = [
    "득점", "도움", "슈팅", "유효슈팅", "블락된 슈팅", "벗어난 슈팅", "PA내 슈팅", "PA외 슈팅", "오프사이드",
    "프리킥 유효슈팅", "프리킥 크로스", "코너킥", "스로인", "드리블", "패스", "키패스", "수비진영 패스", "롱패스",
    "단거리패스", "전방패스", "중거리패스", "횡패스", "후방패스", "크로스", "공격진영 패스", "중앙지역 패스", 
    "태클", "경합(공중)", "경합(지상)", "인터셉트", "클리어링", "차단", "획득", "블락", "볼미스", "파울", 
    "피파울", "경고", "퇴장", "실점", "캐칭", "펀칭", "골킥", "공중 클리어링"
]

data_list_강원 = []
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




URL = 'https://data.kleague.com'

driver = webdriver.Chrome()

driver.get(URL)

driver.implicitly_wait(3)

driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "html > frameset > frame:nth-child(2)"))
#어떻게   html > frameset > frame:nth-child(2)   이것을 가져왔는지 

elements = driver.find_element(By.CSS_SELECTOR, "body > div.wrap > div.header > div > div.headerLeft > div.main-menu > ul > li:nth-child(1) > a").click()

time.sleep(3)

elements = driver.find_element(By.CSS_SELECTOR, "body > div.wrap > div.sub-menu > div > ul > li:nth-child(2) > a").click()

time.sleep(3)

elements = driver.find_element(By.ID, "selectTeamEmble_K21").click()

time.sleep(3)
data_list=driver.find_elements(By.CLASS_NAME, "total-search-chart-datalabel")

for i in range(44):
    data_list_강원.append({'label':labels[i], 'data':(data_list[i]).text })
    
df_광원=pd.DataFrame(data_list_강원)

df_광원.to_csv('data_광원.csv',index=False,encoding='utf-8-sig')








time.sleep(1)


driver.close()
