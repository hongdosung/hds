# BeautifulSoup은 HTML과 XML 파일을 파싱하고 탐색할 수 있는 라이브러리

# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup
import sys

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
#url = 'http://example.com'
url = 'http://naver.com'
url = 'https://www.jinhak.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else : 
    print(response.status_code)
    sys.exit(0)

#print(response.text)
# Create a BeautifulSoup object
#soup = BeautifulSoup(html_content, 'html.parser')


# Extract and print the title
title = soup.title.string
print(f"Title: {title}\n")

divs = soup.find_all('div')
#divs = soup.find_all('div', {class:"ad__Box"})
for div in divs:
    print(div.get_text(strip=True))
    #print(div.text.strip())
    
sys.exit(0)
# Extract and print the first paragraph
paragraphs = soup.find_all('p')
#print(f"Paragraph: {paragraphs}")
for p in paragraphs:
    print(f"p => {p.text}\n")

# Extract and print the link
# link = soup.find('a')['href']
# print(f"Link: {link}")

# 모든 링크 추출
links = soup.find_all('a')
for link in links:
    print(f"link => {link.get('href')}")

links = soup.find_all('script')
for link in links:
    print(f"src => {link.get('src')}")

# 특정 클래스 이름을 가진 모든 div 요소 추출
divs = soup.find_all('div', class_='specific-class')
#divs = soup.find_all('div', {class:"ad__Box"})
for div in divs:
    print(div.text)

# 특정 속성을 가진 모든 이미지 요소 추출
images = soup.find_all('img', attrs={'data-src': True})
for img in images:
    print(img['data-src'])
