import requests
from bs4 import BeautifulSoup

# pip install beautifulsoup4 설치
# pip install lxml 설치 (구문 파서)

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a) # 첫번쨰로 발견한 a element 정보를  출력
print(soup.a.attrs) # a element의 속성 정보를 출력
print(soup.a["href"]) # a element의 href 속성 값 정보 출력

print(soup.find("a", attrs={"class":"Nbtn_upload"})) # a 태그의 class 값이 Nbtn_upload 인 것을 찾아줭~
print(soup.find(attrs={"class":"Nbtn_upload"})) # class가 Nbtn_upload 인 어떤 element를 찾아줭~
print(soup.find("li", attrs={"class":"rank01"}))

rank1 = soup.find("li", attrs={"class":"rank01"}) # li 태그의 class가 rank01인 것을 찾아줭~
print(rank1.a) # 찾은 값 아래에 a 태그를 찾아줭~



