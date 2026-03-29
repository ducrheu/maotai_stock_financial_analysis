import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, Numeric, BIGINT, DATE
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(root_dir,".env"))

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_pwd = os.getenv("DB_PWD")
db_name = os.getenv("DB_NAME")


engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}")


data_dir = os.path.join(root_dir, "data")
csv_path = os.path.join(data_dir, "maotai_stock.csv")

df = pd.read_csv(
    csv_path,
    dtype={
        "open": str,
        "high": str,
        "low": str,
        "close": str,
        "volume": "int64"
    }
)

df.rename(columns={
    "date": "_date",
    "open": "open_price",
    "high": "high_price",
    "low": "low_price",
    "close": "close_price",
    "volume": "volume"
}, inplace=True)

df["_date"] = pd.to_datetime(df["_date"]).dt.date
try:
    lastest_date = pd.read_sql("SELECT MAX(_date) FROM maotai_stock", con = engine).iloc[0, 0]
    if lastest_date is not None:
        df = df[df["_date"] > lastest_date]
        print(f"检测到数据库最新日期：{lastest_date}，将导入{len(df)}条数据")
    else:
        print("数据库无历史数据，全量导入")
except Exception as e:
    print("数据库无历史数据，全量导入")
    pass
df.to_sql(
    name = f"maotai_stock",
    con = engine,
    if_exists = "append",
    index = False,
    chunksize = 1000,
    dtype = {
        "_date": DATE,
        "open_price":Numeric,
        "high_price":Numeric,
        "low_price":Numeric,
        "close_price":Numeric,
        "volume":BIGINT
    }
)

engine.dispose()
print('数据已成功导入!')