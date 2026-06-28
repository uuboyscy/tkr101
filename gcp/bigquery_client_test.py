"""
gcloud config set project notional-zephyr-229707

gcloud auth application-default login \
--impersonate-service-account=<your_service_account> \
--scopes=https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/drive
"""

from google.cloud import bigquery

client = bigquery.Client()

# query = """
# select * from `notional-zephyr-229707.tkr101.gs_by_sql`
# """
query = """select * from `notional-zephyr-229707.tkr101.external_sale`"""

# 執行查詢
query_job = client.query(query)
results = query_job.result()

# 印出結果
print("查詢結果：")
for row in results:
    # print(f"名字: {row.name} | 總數: {row.total}")
    print(row)
