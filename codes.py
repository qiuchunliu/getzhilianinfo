
import requests
import re
# 本次采用正则来匹配内容，而不是用json

# 设置好 headers
head = {
    'Host': 'fe-api.zhaopin.com',
    'Referer': 'https://sou.zhaopin.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
    }
cityid = 530
# 找到 xhr 文件的url
url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=530&workExperienc' \
      'e=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=p' \
      'ython&kt=3&lastUrlQuery={"jl":"530","kw":"python","kt":"3"}&_v=0.56077230&' \
      'x-zp-page-request-id=f1b7230deefe42119667d5e89f36e577-1541315140533-99124'
ht = requests.get(url, headers=head)
ht.encoding = 'utf-8'
res = ht.text
print(res)
# 用正则匹配到职位名称和薪资
print(re.findall(r'"jobName":"(.*?)",', res))
print(re.findall(r'"salary":"(.*?)",', res))
