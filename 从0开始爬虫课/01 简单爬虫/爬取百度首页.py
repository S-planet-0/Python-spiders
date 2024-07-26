# 引入request库
import requests

# 要爬取的URL：
url = 'http://www.baidu.com'

# 获取网页内容
resp = requests.get(url)

# 获取结果
print(resp.status_code)
print(resp.text)

# 存储结果
with open('百度首页.txt', 'w', encoding='utf8') as f:
    f.write(resp.text)

