from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(markup=yc_web_page, features="html.parser")

article_elements = soup.find_all(name="span", class_="titleline")
upvote_elements  = soup.find_all("span", class_="score")

for index, article_element in enumerate(article_elements):
    article = article_element.select_one(".titleline a:first-child")
    article_text = article.text
    article_link = article.get("href")
    print(article_text)
    print(article_link)
    article_upvote = upvote_elements[index].text.split(" ")[0]
    print(article_upvote)




















# print(target_title.getText)
# with open("website.html", "r") as file:
#     content = file.read()
    
# # print(content)
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.prettify())
# # print(soup.title.string)
# # print(soup.p)

# all_anchor_tags = soup.find_all("a")
# # print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
    
# heading = soup.find(name="h1", id="name")
# # print(heading)/

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))

# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)

# name = soup.select_one("#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)