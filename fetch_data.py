import requests
import pandas as pd

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=2200012"
response = requests.get(url)
data = response.json()
results = data["results"]
df = pd.DataFrame(results)

df.to_csv("sample_data.csv", index=False, encoding="utf-8-sig")
print("データの取得とCSV保存が完了しました！")