--查空值/负价格/负成交量
SELECT *
	FROM "maotai_stock"
	WHERE
	_date IS NULL
	OR open_price <= 0
	OR high_price <= 0
	OR low_price <= 0
	OR close_price <= 0
	OR volume < 0;

--K线逻辑检查
SELECT *
	FROM "maotai_stock"
	WHERE
	high_price < open_price
	OR high_price < close_price
	OR high_price < low_price
	OR low_price > open_price
	OR low_price > close_price;

--检查重复交易日
SELECT 
	_date,
	COUNT(*) AS 重复次数
	FROM "maotai_stock"
	GROUP BY _date
	HAVING COUNT(*) > 1;