import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# 连接PG
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_pwd = os.getenv("DB_PWD")
db_name = os.getenv("DB_NAME")


engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}")

#读取PG中数据
df_ma = pd.read_sql("""
    SELECT _date, close_price, "MA5", "MA20"
    FROM (
         SELECT
            _date,
             close_price,
             ROUND(AVG(close_price) OVER (ORDER BY _date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW), 2) AS "MA5",
             ROUND(AVG(close_price) OVER (ORDER BY _date ROWS BETWEEN 19 PRECEDING AND CURRENT ROW), 2) AS "MA20"
                FROM maotai_stock
         ) t
        ORDER BY _date
""", con = engine)

# 画均线图
plt.figure(figsize=(12,6)),
plt.plot(df_ma['_date'], df_ma['close_price'], label='clo_pri_day', alpha=0.5),
plt.plot(df_ma['_date'], df_ma['MA5'], label='MA5', linewidth=2),
plt.plot(df_ma['_date'], df_ma['MA20'], label='MA20', linewidth=2),
plt.title('avg_chart_of_maotai'),
plt.legend(),
plt.show()
