from bs4 import BeautifulSoup

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(response.text, "lxml")

# 提取网页标题
title = soup.title.string
print(f"网页标题: {title}")

# 提取所有超链接
links = []
for a_tag in soup.find_all("a", href=True):
    links.append(a_tag["href"])

print("提取到的链接:")
print("\n".join(links))
