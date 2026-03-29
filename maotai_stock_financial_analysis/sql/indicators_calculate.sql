--计算每日涨跌额、涨跌幅
SELECT 
	_date,
	close_price AS 当日收盘价,
	LAG(close_price,1) OVER (ORDER BY _date) AS 前一天收盘价,
	ROUND(close_price - LAG(close_price,1) OVER (ORDER BY _date),2) AS 涨跌额,
	ROUND((close_price - LAG(close_price,1) OVER (ORDER BY _date))/LAG(close_price,1) OVER (ORDER BY _date)*100,2) AS 涨跌幅_百分比
	FROM "maotai_stock";

--计算5日/20日均线
SELECT 
	_date,
	close_price AS clo_pri_day,
	ROUND(AVG(close_price) OVER (ORDER BY _date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW),2) AS "MA5",
	ROUND(AVG(close_price) OVER (ORDER BY _date ROWS BETWEEN 19 PRECEDING AND CURRENT ROW),2) AS "MA20"
	FROM "maotai_stock";

--五日成交量曲线
SELECT
	_date,
	volume AS 当日成交量,
	ROUND(AVG(volume) OVER (ORDER BY _date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW),0) AS "VOL5"
	FROM "maotai_stock";