from google import auth
from google.auth import impersonated_credentials
from google.cloud import bigquery

# 1. 定義您的 Scopes
GCP_CREDENTIAL_SCOPE = [
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/bigquery",
]

# 2. 關鍵修正：在取得來源憑證（ADC）時，就將 Scopes 綁定進去
source_credentials, _ = auth.default(scopes=GCP_CREDENTIAL_SCOPE)

# 3. 建立模擬憑證（這裡只帶 target_scopes，移除了不支援的 scopes 參數）
creds = impersonated_credentials.Credentials(
    source_credentials=source_credentials,
    target_principal="bigquery-user@notional-zephyr-229707.iam.gserviceaccount.com",
    target_scopes=GCP_CREDENTIAL_SCOPE,
)

# 4. 初始化 BigQuery 客戶端
client = bigquery.Client(
    credentials=creds, 
    project="notional-zephyr-229707"
)

# 撰寫 SQL 查詢（此為 BigQuery 提供的公開資料集）
query = """
    SELECT name, SUM(number) as total
    FROM `bigquery-public-data.usa_names.usa_1910_current`
    WHERE state = 'TX'
    GROUP BY name
    ORDER BY total DESC
    LIMIT 10
"""
query = """
select * from `notional-zephyr-229707.tkr101.external_gs`
"""

# 執行查詢
query_job = client.query(query)
results = query_job.result()

# 印出結果
print("查詢結果：")
for row in results:
    # print(f"名字: {row.name} | 總數: {row.total}")
    print(row)
