from google.cloud import bigquery

client = bigquery.Client()

# 撰寫 SQL 查詢（此為 BigQuery 提供的公開資料集）
query = """
    SELECT name, SUM(number) as total
    FROM `bigquery-public-data.usa_names.usa_1910_current`
    WHERE state = 'TX'
    GROUP BY name
    ORDER BY total DESC
    LIMIT 10
"""

# 執行查詢
query_job = client.query(query)
results = query_job.result()

# 印出結果
print("查詢結果：")
for row in results:
    print(f"名字: {row.name} | 總數: {row.total}")
