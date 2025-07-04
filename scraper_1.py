#爬虫程序模拟人类浏览器的行为，向网页服务器发送请求，获取网页内容，然后对获取到的内容进行解析、提取信息（文字、图片、链接）
#****************************发送 HTTP 请求 通过 requests 库获取网页内容************************************
import requests

# 定义目标 URL
url = "https://example.com"

# 设置请求头，伪装为浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

# 发送请求
response = requests.get(url, headers=headers)

# 检查状态码
if response.status_code == 200:
    print("请求成功！")
    print(response.text[:500])  # 打印部分网页内容
else:
    print(f"请求失败，状态码: {response.status_code}")

#******************************解析 HTML 数据**********************************************
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

#******************************保存数据到 CSV 文件**********************************************
import pandas as pd

# 构造数据字典
data = {"Links": links}

# 转换为 DataFrame
df = pd.DataFrame(data)

# 保存为 CSV
df.to_csv("links.csv", index=False, encoding="utf-8-sig")
print("数据已保存到 links.csv")
#***************************动态网页处理 有些网页通过 JavaScript 加载数据，requests 无法直接抓取。这时需使用浏览器自动化工具，如 Selenium 或 Playwright
from selenium import webdriver
from selenium.webdriver.common.by import By

# 配置 Selenium WebDriver（以 Chrome 为例）
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 无头模式
driver = webdriver.Chrome(options=options)

# 打开网页
driver.get("https://example.com")

# 等待页面加载
driver.implicitly_wait(10)

# 提取动态加载的内容
titles = driver.find_elements(By.TAG_NAME, "h1")
for title in titles:
    print(title.text)

# 关闭浏览器
driver.quit()
#***********************添加随机延迟 避免频繁请求被封禁********************************
import time
import random

time.sleep(random.uniform(1, 3))  # 随机延迟 1-3 秒
#***************************使用代理 IP 通过代理绕过 IP 封禁***************************
proxies = {
    "http": "http://username:password@proxyserver:port",
    "https": "http://username:password@proxyserver:port"
}

response = requests.get(url, headers=headers, proxies=proxies)
#***********************处理验证码 使用 OCR 识别验证码*******************************
from PIL import Image
import pytesseract

# 读取验证码图片
image = Image.open("captcha.png")

# 使用 OCR 识别文本
captcha_text = pytesseract.image_to_string(image)
print(f"验证码内容: {captcha_text}")
#************************爬取复杂数据的技巧 JSON 数据爬取*************************
api_url = "https://example.com/api/data"
response = requests.get(api_url, headers=headers)

# 解析 JSON 数据
data = response.json()
print(data)
#*********************************自动抓取多页内容**********************
base_url = "https://example.com/page={}"
for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url, headers=headers)
    print(f"抓取第 {page} 页内容")
#*********************下载图片或文件到本地********************************
file_url = "https://example.com/image.jpg"
response = requests.get(file_url, stream=True)

# 保存到本地
with open("image.jpg", "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        file.write(chunk)

print("文件下载完成！")