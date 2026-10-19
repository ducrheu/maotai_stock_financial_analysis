-- 趋势类指标：均线系统
SELECT
	time,
	open,
	high,
	low,
	close,
	vol,
-- 五分钟收盘价均线
	ROUND(AVG(close) OVER(ORDER BY time ROWS BETWEEN 4 PRECEDING AND CURRENT ROW), 2) AS MA_5,
-- 十分钟收盘价均线
	ROUND(AVG(close) OVER(ORDER BY time ROWS BETWEEN 9 PRECEDING AND CURRENT ROW), 2) AS MA_10,
-- 三十分钟收盘价均线
	ROUND(AVG(close) OVER(ORDER BY TIME ROWS BETWEEN 29 PRECEDING AND CURRENT ROW), 2) AS MA_30
	FROM stock_basic
	ORDER BY time


-- 收益类指标：涨跌幅
SELECT
	time,
	open,
	high,
	low,
	close,
	vol,
	LAG(close, 1) OVER(ORDER BY time) AS pre_close,
-- 单分钟涨跌幅
	ROUND(close / LAG(close, 1) OVER(ORDER BY time), 12) AS single_min_rate,
-- 累计涨跌幅
	ROUND(close / FIRST_VALUE(close) OVER(ORDER BY time), 12) AS acc_rate
	FROM stock_basic
	ORDER BY time


-- 资金量指标：成交量和量能
SELECT
	time,
	open,
	high,
	low,
	close,
	vol,
-- 五分钟成交量均线
	ROUND(AVG(vol) OVER(ORDER BY time ROWS BETWEEN 4 PRECEDING AND CURRENT ROW), 3) AS VOL_MA5,
-- 量比 = 当前交易量 / 五分钟均量
	ROUND(vol::NUMERIC / NULLIF(AVG(vol) OVER(ORDER BY time ROWS BETWEEN 4 PRECEDING AND CURRENT ROW), 0), 12) AS quan_rate
	FROM stock_basic
	ORDER BY time


-- 波动类：振幅 & 真实振幅
SELECT
	time,
	open,
	high,
	low,
	close,
	vol,
-- 单分钟振幅
	ROUND((high - low) / low, 12) AS single_min_amp,
-- 真实振幅 TR(三个最大值)
	ROUND(
		GREATEST(
			high - low,
			high - LAG(close, 1) OVER(ORDER BY time),
			LAG(close, 1) OVER(ORDER BY time) - low
		), 2
	)AS TR
	FROM stock_basic
	ORDER BY time