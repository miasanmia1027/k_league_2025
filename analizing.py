# 내가 여기서 할것 pandas를 이용하여 전체 평균값과 가중치를 추가한 평균값 그래프 2개를 만들어서 어떤 수치가 승점을 쌓는데 도움이 되는지 확인
# 다음으로는 매 경기마다 어떤 것이 승점을 가르는지 파악하기 위해 경기마다 데이터를 분석하여해보기
import pandas as pd
# -------------------------------------------------------------------------
# df = pd.read_csv("C:\Codng\K_league\k_league\data_광원.csv")

# df["data"] = df["data"].astype("string")

# df["data"] = df["data"].str.replace(r",", r"", regex=False)


# print(df["data"])

# df_type = type(df["data"])

# print(df_type)
# ---------------------------------------------------------------------------
# 함수를 만들기 전에 내가 시도한것들

k_league_name_list = [
    "울산",
    "김천",
    "광원",
    "수원FC",
    "포항",
    "서울",
    "광주",
    "제주",
    "대전",
    "전북",
    "대구",
    "인천",
]


def csv_file_tablet(data_name):
    df = pd.read_csv(f"C:\Codng\K_league\k_league\data_{data_name}.csv")
    print(data_name)
    df["data"] = df["data"].astype("string")
    df["data"] = df["data"].str.replace(r",", r"", regex=False)


for x in k_league_name_list:
    csv_file_tablet(x)
# ------------------------------------------------------------
# 여기까지가 지금 모든 구단의 데이터를 가져온것

# 내가 다음에 해야하는것 여기서 for문으로 가져올때 변수명을 잘해서 가져오는것
# 다음으로 순서대로 for문을 서서 가중치를 사용한다.
