# BeautifulSoup은 HTML과 XML 파일을 파싱하고 탐색할 수 있는 라이브러리

# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup

# Sample HTML content
html_content = """
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Welcome to the Sample Page</h1>
    <p>This is a sample paragraph.</p>
    <a href="https://example.com">Visit Example.com</a>
</body>
</html>
"""

# 웹 페이지 요청
url = 'http://example.com'
response = requests.get(url)

# Create a BeautifulSoup object
#soup = BeautifulSoup(html_content, 'html.parser')
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and print the title
title = soup.title.string
print(f"Title: {title}")

# Extract and print the first paragraph
paragraph = soup.find('p').text
print(f"Paragraph: {paragraph}")

# Extract and print the link
link = soup.find('a')['href']
print(f"Link: {link}")

# 모든 링크 추출
links = soup.find_all('a')
for link in links:
    print(link.get('href'))


# 특정 클래스 이름을 가진 모든 div 요소 추출
divs = soup.find_all('div', class_='specific-class')
for div in divs:
    print(div.text)

# 특정 속성을 가진 모든 이미지 요소 추출
images = soup.find_all('img', attrs={'data-src': True})
for img in images:
    print(img['data-src'])


#################################################################################
# BeautifulSoup을 사용한 뉴스 기사 스크래핑
import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = 'http://news.example.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')
    for article in articles:
        title = article.find('h2').text
        summary = article.find('p').text
        print(f"Title: {title}")
        print(f"Summary: {summary}")

# 예제 실행
scrape_news()
