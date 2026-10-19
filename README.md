# 贵州茅台股票金融数据分析（Python + PostgreSQL）

股票数据全流程项目：抓取 → PostgreSQL 入库 → 数据质量校验 → 指标计算 → 可视化。

## 内容

- `maotai_stock_financial_analysis/` — 日线主项目：baostock 抓取、PostgreSQL 建表/入库、质量校验、MA5/MA20 与 5 日均量、Matplotlib 可视化
- `legacy/maotai_min_stock/` — 分钟级版本（原独立仓库，已归档并入）：AKShare 1 分钟 K 线、清洗、入库、均线/涨跌幅/量比/振幅

## 技术栈

Python · pandas · SQLAlchemy · PostgreSQL · baostock · AKShare · Matplotlib · SQL 窗口函数

## 快速开始

见 [主项目 README](maotai_stock_financial_analysis/README.md)。
