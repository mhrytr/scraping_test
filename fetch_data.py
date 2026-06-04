import requests
import pandas as pd

# ① 共有していただいたURLを指定
url = "https://api.odpt.org/api/v4/gbfs/hellocycling/station_status.json?acl:consumerKey=oipscg64zbjypuybs3l5c74n4vu73gctuunf4861vs17chnq57o7u249ul7esmlc"

response = requests.get(url)
data = response.json()

# ② GBFS形式のJSON構造に合わせて，データの階層（data -> stations）を指定して取り出します
stations_data = data["data"]["stations"]

# ③ データを表形式（データフレーム）に変換
df = pd.DataFrame(stations_data)

# ④ CSVファイルとして保存
df.to_csv("station_status.csv", index=False, encoding="utf-8-sig")

print("自転車ステーション情報の取得とCSV保存が完了しました！")
