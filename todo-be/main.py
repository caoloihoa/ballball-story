import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hahuyen27361995",
  database="hiep"
)

mycursor = mydb.cursor()
# url_data = "https://metruyencv.com/truyen/vua-thanh-tien-than-con-chau-cau-ta-dang-co/chuong-1"
# Lấy nội dung và tên chương
def craw_data(url_data):
    print("crawling", url_data)
    res = requests.get(url=url_data)
    soup = BeautifulSoup(res.content, "html.parser")
    title_chapter = soup.find("div", class_="h1").text.strip()
    content = soup.find("div", id="article").text
    sql = "INSERT INTO content (chapter_name, chapter_content) VALUES (%s,%s)"
    val = (title_chapter, content)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    # return title_chapter, content

# craw_data(url)
if __name__ == "__main__":
    web_url = input("Nhap ten web \n")
    chapter_number = int(input("nhap so luong chuong \n"))
    for i in range(1, chapter_number):
        url = web_url+ "/" + "chuong"+"-"+str(i)
        craw_data(url)
        
# res = requests.get(url=url_data)
# soup = BeautifulSoup(res.content, "html.parser")
# title_chapter = soup.find("ul > li > h1 > a").text.strip()
# print(title_chapter)



    # title_story = title_h2.getText() if title_h2 else format_title(title=url_data)
    # last_anchor = soup.select_one("a.last")
    # relative_path = os.path.join(os.path.curdir, "data")
    # file_path = os.path.join(relative_path, f"{title_story}.txt")

#     if last_anchor:
#         total_page = find_all_page_from_paginate(last_anchor["href"])
#         for i in range(total_page):
#             print(i)
#             story_content = craw_one_page(link=url_data, page=i + 1)
#             with open(file_path, "a") as f:
#                 f.write(story_content)
#     else:
#         story_content = soup.select_one("div")
#         story_content = story_content.getText()
#         with open(file_path, "w") as f:
#             f.write(story_content)


# def find_all_page_from_paginate(link_page):
#     last_slash_index = link_page.rfind('/')
#     if last_slash_index != -1:
#         filename = link_page[last_slash_index + 1:]
#     else:
#         filename = link_page
#     return int(filename)


# def format_title(title):
#     last_slash = title.rfind("/")
#     new_title = title[last_slash + 1:]
#     new_title = new_title.split(".")[0]
#     return new_title


# def craw_one_page(link, page):
#     response = requests.get(f"{link}/{page}")
#     soup_page = BeautifulSoup(response.content, "html.parser")
#     content_page = soup_page.select_one("div.bai-viet-box")

#     return content_page.getText()


# def crawl_data_list_story(link_list_story):
#     response = requests.get(url=link_list_story)
#     soup = BeautifulSoup(response.content, "html.parser")
#     last_anchor = soup.select_one("a.last")
#     total_page = find_all_page_from_paginate(last_anchor["href"])
#     list_link = []
#     for i in range(total_page):
#         print(i)
#         list_data_link = crawl_one_page_list_link(link=link_list_story, page=i + 1)
#         print(list_data_link)
#         list_link.extend(list_data_link)

#     pd_df = pd.DataFrame(list_link, columns=['link'])
#     pd_df.to_csv('link.csv', index=False)


# def crawl_one_page_list_link(link, page):
#     list_data_link = []
#     url_link = link
#     if page > 1:
#         url_link = f"{url_link}/page/{page}"
#     res = requests.get(url_link)
#     soup = BeautifulSoup(res.content, "html.parser")
#     data_link = soup.select("div.list a")
#     for d in data_link:
#         list_data_link.append(d["href"])

#     return list_data_link


# # https://giaitri321.vip/doc-truyen/con-duong-mang-ten-em.html
# # https://giaitri321.vip/category/doc-truyen
        
