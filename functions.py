import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#------------------------------------------
# 실질적으로 쓰는것
# make_percentage() == 특정년도의 데이터
# -> 요소 값 ==  이것도 팀의 요소 값
# every_team_make_percentage() ==  모든 팀을 퍼센트로  
# -> 입력 값 ==  팁의 요소 값
#----------------------------------------
# 거리를 퍼센트로 해서 그냥 일반 정수로 나오는 문제는 해결이 되었다.
def make_percentage(element):
    df = pd.read_csv("2024_team_data/2024_score_data.csv")
    
    min_val = df[element].min()# 여기서 퍼센트를 만들기 위해 최소와 최대를 지금 구해온것이다.
    max_val = df[element].max()

    percentages = []
    for value in df[element]:
        if max_val != min_val:# 최대와 최소가 같지 않다면  
            percentage = int((value - min_val) / (max_val - min_val) * 100)
            # 이거는 지금 뭐를 하는걸까?
            # 이거는 최대값과 최소값 사이에 내가 원하는 파일이 어느 정도의 거리에 있는지 확인하는 코드 그니까 이걸로 거리를 확인을 하는거지
        else: # 이런 경위의 수는 현재 전 시즌을 보는 과정에서는 필요가 없지만 있어도 나쁘지 않다.
            percentage = 0
        percentages.append(percentage)
    
    df[f"{element}"] = percentages
    
    df[["name", f"{element}"]].to_csv(f"2024_team_data/결과/{element}.csv", index=False, encoding="utf-8-sig")
    
team_list = ["강원","광주","김천","대구","대전","서울","수원FC","울산","인천","전북","제주","포항"]

# 이거 천의 자리를 넘어가면 문제가 생긴다. "," 이거를 없애주는것도 추가 해야한다.
# 이걸로 점을 제거하는 함수
def make_percentage_every_team_data(element):
    data_list = []
    for team in team_list:
        df = pd.read_csv(f"2024_team_data/raw_data/{team}.csv")
        index = df.index[df["label"] == element].tolist()
        data = str(df["data"][index[0]]).replace(",", "")
        result = int(data)
        data_list.append(result)
    return data_list

def every_team_make_percentage(element):
    df = pd.read_csv("2024_team_data/2024_score_data.csv")
    data = make_percentage_every_team_data(element)
    
    min_val = min(data)
    max_val = max(data)

    percentages = []
    for value in data:
        if max_val != min_val:
            percentage = int((value - min_val) / (max_val - min_val) * 100)
        else:
            percentage = 0
        percentages.append(percentage)
    
    df[f"{element}"] = percentages
    
    # 결과 저장
    df[["name", f"{element}"]].to_csv(f"2024_team_data/스텟/{element}.csv", index=False, encoding="utf-8-sig")



def make_graph(결과):
    df = pd.read_csv(f"2024_team_data/결과/{결과}.csv")
    data_list_결과 =[]
    df.set_index("name", inplace=True)
    for i in range(0,12):
        data_list_결과.append(df["points"].iloc[i])
    data_list_total=[]
    for i in range(len(labels)):
        df = pd.read_csv(f"2024_team_data/스텟/{labels[i]}.csv")
        df.set_index("name", inplace=True)
        for i_2 in range(0,12):
            data_list_total.append(df[labels[i]].iloc[i_2])
    for i in range(0,44):
        data = data_list_total[i:i+12]
        plt.scatter(data_list_결과, data , color=colors[i], s=30)
    plt.axis((0,100, 0, 100))
    plt.show()
    











colors = [
    'red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'black', 'gray',
    'brown', 'lime', 'navy', 'gold', 'teal', 'violet', 'pink', 'indigo', 'darkgreen', 'darkred',
    'silver', 'lightblue', 'lightgreen', 'darkblue', 'maroon', 'beige', 'coral', 'olive', 'chocolate', 'turquoise',
    'plum', 'orchid', 'slategray', 'crimson', 'peru', 'seagreen', 'sienna', 'darkorchid', 'deepskyblue', 'chartreuse',
    'hotpink', 'cadetblue', 'mediumvioletred', 'mediumslateblue', 'mediumseagreen'
]


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
team_list = ["강원", "광주", "김천", "대구", "대전", "서울", "수원FC", "울산", "인천", "전북", "제주", "포항"]