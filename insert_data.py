import requests
from bs4 import BeautifulSoup
import pymysql

# MySQL 연결 설정
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Jiwoo123',  # MySQL root 비밀번호 입력
    db='job_portal',
    charset='utf8mb4'
)

# 사람인 채용 공고 URL
url = "https://www.saramin.co.kr/zf_user/jobs/list/domestic"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 채용 공고 데이터 추출
jobs = []
for job in soup.select('.item_recruit'):
    title = job.select_one('.job_tit a').text.strip()
    company = job.select_one('.corp_name a').text.strip()
    location = job.select_one('.job_condition span').text.strip()
    link = job.select_one('.job_tit a')['href']
    jobs.append((title, company, location, f"https://www.saramin.co.kr{link}"))

# MySQL에 데이터 저장
try:
    with conn.cursor() as cursor:
        sql = "INSERT INTO jobs (title, company, location, link) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql, jobs)
        conn.commit()
        print("데이터 삽입 성공!")
finally:
    conn.close()