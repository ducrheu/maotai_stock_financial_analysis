--查看前十条数据，验证导入是否成功
SELECT *
	FROM "maotai_stock"
	ORDER BY _date
	LIMIT 10;

--统计数据总条数
SELECT COUNT(*) AS total_date
	FROM "maotai_stock"