import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, Numeric, BIGINT, DATE

# 列名标准化，统一字段命名
df.rename(columns={
    'day': 'time',
    'open': 'open',
    'high': 'high',
    'low': 'low',
    'close': 'close',
    'volume': 'vol'
}, inplace = True)

# 时间格式标准化，转换为 datetime 类型
## 1. 正确转换时间：保留 年-月-日 时:分:秒（不要丢时分！）
df['time'] = pd.to_datetime(df['time'])
## 2. 提取【小时:分钟】用于筛选（关键！）
df['hour_min'] = df['time'].dt.strftime('%H:%M')

df['vol'] = pd.to_numeric(df['vol'], errors='coerce')

# 数据去重，剔除重复的分钟 K 线
df = df.drop_duplicates(subset=['time'])

# 剔除无效交易数据，过滤停牌 / 无成交行
df = df[df['vol'] > 0]

# 过滤异常价格数据，剔除错误 K 线
df = df[(df['high'] >= df['low']) & (df['close'] > 0) & (df['open'] > 0)]

# 缺失值填充，保证数据连续性
df[['open', 'high', 'low', 'close', 'vol']] = df[['open', 'high', 'low', 'close', 'vol']].ffill()

# 过滤合法交易时段，只保留 A 股有效交易时间
df = df[((df['hour_min'] >= '09:30') & (df['hour_min'] <= '11:30')) | ((df['hour_min'] >= '13:00') & (df['hour_min'] <= '15:00'))]

df = df.drop(columns=['hour_min', 'amount'])

print(df.info())
