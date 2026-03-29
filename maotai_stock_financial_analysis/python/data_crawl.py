import os
import baostock as bs
import pandas as pd

# 1. 登录
lg = bs.login()

# 2. 获取数据（贵州茅台600519，2023-2026年日K线）
rs = bs.query_history_k_data_plus("sh.600519",
    "date,open,high,low,close,volume",
    start_date='2023-01-01', end_date='2026-03-27',
    frequency="d", adjustflag="3")  # 3=不复权

# 3. 转为DataFrame并保存CSV
data_list = []
while (rs.error_code == '0') and rs.next():
    data_list.append(rs.get_row_data())
df = pd.DataFrame(data_list, columns=rs.fields)
script_dir = os.path.dirname(__file__)
data_dir = os.path.join(script_dir, "../data")
os.makedirs(data_dir, exist_ok = True)
df.to_csv(os.path.join(data_dir, "maotai_stock.csv"), index = False, encoding = "utf-8-sig")

# 4. 登出
bs.logout()
print(f"数据抓取完成，共{len(df)}条数据，已保存到data文件夹中")