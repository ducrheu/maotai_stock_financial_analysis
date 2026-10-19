import akshare as ak

# 直接获取贵州茅台 1分钟级别数据
df = ak.stock_zh_a_minute(symbol="sh600519", period="1", adjust="qfq")

# 直接保存CSV
df.to_csv("茅台分钟数据.csv", index=False, encoding="utf-8-sig")

print("获取成功！")
print(df.head())
print(df.info())