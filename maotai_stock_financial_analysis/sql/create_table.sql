--创建股票行情表
DROP TABLE IF EXISTS "maotai_stock";

CREATE TABLE "maotai_stock"
(
_date DATE PRIMARY KEY,
open_price NUMERIC(10, 2) NOT NULL ,
high_price NUMERIC(10,2) NOT NULL ,
low_price NUMERIC(10,2) NOT NULL ,
close_price NUMERIC(10,2) NOT NULL ,
volume BIGINT NOT NULL 
);