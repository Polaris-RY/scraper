# 爬虫项目

## 项目简介
本项目演示了多种常见的Python爬虫技术，包括：
- 使用 requests 抓取网页
- BeautifulSoup 解析HTML
- pandas 保存数据到CSV
- Selenium 处理动态网页
- 随机延迟与代理IP防封禁
- OCR识别验证码
- 抓取JSON数据与多页内容
- 下载图片或文件

## 环境依赖
- Python 3.7+
- requests
- beautifulsoup4
- lxml
- pandas
- selenium
- pillow
- pytesseract

安装依赖：
```bash
pip install -r requirements.txt
```
如无 requirements.txt，可手动安装：
```bash
pip install requests beautifulsoup4 lxml pandas selenium pillow pytesseract
```

## 使用方法
1. 根据需要修改 `scraper_1.py` 里的目标网址和参数。
2. 运行主程序：
   ```bash
   python scraper_1.py
   ```
3. 部分功能（如验证码识别、代理、Selenium）需根据实际情况配置相关资源。

## 注意事项
- 请遵守目标网站的robots协议及相关法律法规。
- 某些功能（如Selenium、OCR）需额外安装浏览器驱动或Tesseract-OCR。

## 目录结构
- `scraper_1.py`：爬虫主脚本
- `README.md`：项目说明
- 其它依赖文件

## 联系方式
如有问题请提交issue或联系作者。

