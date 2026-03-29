# 贵州茅台股票金融数据分析项目
金融数据方向项目，实现股票数据抓取、数据库存储、数据质量校验、量化指标计算、可视化全流程

## 一、项目技术栈
- 数据抓取：baostock
- 数据库：PostgreSQL
- 数据处理：Python, pandas, SQLALchemy
- 可视化：Matplotlib
- SQL：基础查询, 窗口函数(LAG/AVG)

## 二、项目功能
1. 股票数据抓取：通过baostock获取茅台日K线数据
2. 数据库存储：PostgreSQL建表并导入数据，支持增量更新
3. 数据质量校验：排查空值、异常价格、重复数据
4. 涨跌幅、MA5/MA20均线、5日均量
5. 数据可视化：生成股价均线分析图

## 三、项目结构
```text
maotai-stock-financial-analysis/
├── sql/
│   ├── create_table.sql
│   ├── data_quality_check.sql
│   ├── indicators_calculate.sql
│   └── test_query.sql
├── python/
│   ├── data_crawl.py
│   ├── db_import.py
│   └── data_visualization.py
├── data/
│   └── maotai_stock_sample.csv  # 开源用样例，本地全量CSV用.gitignore忽略
├── images/
│   └── avg_chart_of_maotai.png
├── .env                # 本地敏感配置，绝对不上传GitHub
├── .env.example        # 配置模板，开源用
├── .gitignore          # 忽略敏感信息/全量数据
├── README.md           # 项目说明
└── requirements.txt    # 依赖清单
```

## 四、运行步骤
1. 安装依赖：`pip install -r requirements.txt`
2. 执行SQL脚本：在PostgreSQL运行`sql/create_table.sql`建表
3. 抓取数据：运行`python/data_crawl.py`
4. 导入数据：运行`sql/data_import.sql`
5. 可视化：运行`python/data_visualization.py`

## 五、项目成果
![茅台股价均线图]("images/avg_chart_of_maotai.png")
