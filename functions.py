import pandas as pd

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
    
    min_val = df[element].min()
    max_val = df[element].max()

    percentages = []
    for value in df[element]:
        if max_val != min_val:
            percentage = int((value - min_val) / (max_val - min_val) * 100)
        else:
            percentage = 0
        percentages.append(percentage)
    
    df[f"{element}_percentage"] = percentages
    
    # 결과 저장
    df[["name", f"{element}_percentage"]].to_csv(f"2024_team_data/scores/mp_{element}.csv", index=False, encoding="utf-8-sig")

# 현재 개별 요소를 가져오는 코들 짰다. 팀 이름 그리고 원한는 요소 이거를 또 하나의 한수를 써서 간단하게 하자
# 이거 천의 자리를 넘어가면 문제가 생긴다. "," 이거를 없애주는것도 추가 해야한다.
team_list = ["강원","광주","김천","대구","대전","서울","수원FC","울산","인천","전북","제주","포항"]

def make_percentage_team_data(team_name,element):
    df = pd.read_csv(f"2024_team_data/raw_data/{team_name}.csv")
    index = df.index[df["label"] == f"{element}"].tolist()
    data = str(df["data"][index[0]]).replace(",", "")
    return int(data)

def make_percentage_every_team_data(element):
    data_list = []
    for team in team_list:
        result = make_percentage_team_data(team, element)
        data_list.append(result)
    return data_list

# 거리를 퍼센트로 해서 그냥 일반 정수로 나오는 문제는 해결이 되었다.
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
    
    df[f"{element}_percentage"] = percentages
    
    # 결과 저장
    df[["name", f"{element}_percentage"]].to_csv(f"2024_team_data/team_elements/mp_every_{element}.csv", index=False, encoding="utf-8-sig")











