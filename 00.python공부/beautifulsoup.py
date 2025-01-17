# BeautifulSoup은 HTML과 XML 파일을 파싱하고 탐색할 수 있는 라이브러리
# 텍스트 정보만 뽑아 오고 싶다면 soup.title.get_text() 혹은 soup.title.string을 사용
# 특정 태그를 뽑아 오고 싶다면 soup.find('태그명')을 사용
# 특정 클래스 이름을 가진 모든 div 요소 추출시 soup.find_all('div', class_='specific-class')를 사용
# 특정 속성을 가진 모든 이미지 요소 추출시 soup.find_all('img', attrs={'data-src': True})를 사용
# 모든 링크 추출시 soup.find_all('a')를 사용
# soup.a.attrs(attribute)를 통해 이 element의 특성, 속성
# soup.a['href']를 통해 이 element의 href 속성값을 가져올 수 있음, soup.a.attrs["href"]와 동일
# soup.a.get('href')를 통해 이 element의 href 속성값을 가져올 수 있음
# soup.a.get_text()를 통해 이 element의 text를 가져올 수 있음
# soup.a.string를 통해 이 element의 text를 가져올 수 있음
# soup.a.text를 통해 이 element의 text를 가져올 수 있음
# soup.a.contents를 통해 이 element의 자식을 가져올 수 있음
# soup.a.children를 통해 이 element의 자식을 가져올 수 있음
# soup.a.parent를 통해 이 element의 부모를 가져올 수 있음
# soup.a.parents를 통해 이 element의 부모를 가져올 수 있음
# soup.a.next_sibling를 통해 이 element의 다음 형제를 가져올 수 있음
# soup.a.previous_sibling를 통해 이 element의 이전 형제를 가져올 수 있음
# soup.find('a', attrs={"class": "Nbtn_upload"})
# soup.find('a', class_='Nbtn_upload')
# soup.select('a.Nbtn_upload')
# soup.select_one('a.Nbtn_upload')
# soup.select('div > a')
# soup.select('div a')
# soup.select('div a[href]')
# soup.select('div a[href="http://example.com"]')
# soup.select('div a[href^="http"]')
# soup.select('div a[href$="com"]')
# soup.select('div a[href*="example"]')
# soup.select('div a:nth-of-type(2)')
# soup.select('div a:nth-of-type(n)')
# soup.select('a[href]')
# soup.select('a[href]')[0]['href']
# soup.select('a[href]')[0].get('href')
# soup.select('a[href]')[0].attrs['href']

    


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
