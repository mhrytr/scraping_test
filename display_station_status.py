import pandas as pd
from tabulate import tabulate

# CSVファイルを読み込む
df = pd.read_csv('station_status.csv')

# 必要な列を選択して表示用にリネーム
display_df = df[['is_renting', 'station_id', 'is_installed', 'is_returning', 'num_bikes_available', 'num_docks_available']].copy()
display_df.columns = ['Renting', 'Station ID', 'Installed', 'Returning', 'Bikes', 'Docks']

# ステータスを追加
def get_status(row):
    if not row['Renting']:
        return 'Not Renting'
    elif row['Bikes'] == 0:
        return 'No bikes'
    elif row['Docks'] == 0:
        return 'Full'
    else:
        return 'Available'

display_df['Status'] = display_df.apply(get_status, axis=1)

# 表形式で表示
print(tabulate(display_df, headers='keys', tablefmt='grid', showindex=False))

# または Markdown 形式で表示
print("\n\n--- Markdown Format ---\n")
print(tabulate(display_df, headers='keys', tablefmt='github', showindex=False))

# CSVで保存（オプション）
display_df.to_csv('station_status_formatted.csv', index=False)
print("\n\nFormatted data saved to 'station_status_formatted.csv'")
