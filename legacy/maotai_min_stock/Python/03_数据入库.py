from sqlalchemy import create_engine, NUMERIC, BIGINT, TIMESTAMP
from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")
table_name = os.getenv("DB_TABLE")

engine = create_engine(f'postgresql://{username}:{password}@{host}/{database}')

df.to_sql(
    name = table_name,
    con = engine,
    if_exists = 'append',
    index = False,
    dtype = {
        'time' : TIMESTAMP,
        'open' : NUMERIC(10, 2),
        'high' : NUMERIC(10, 2),
        'low' : NUMERIC(10, 2),
        'close' : NUMERIC(10, 2),
        'vol' : BIGINT
    }
)

print('导入 PostgreSQL 成功！')