import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
cookies = {'cookie': 'll="108288"; bid=drH9aMo646U; dbcl2="169627121:znIl1vssquE"; _ga=GA1.2.1534375650.1512440313; _gid=GA1.2.617261649.1512440313; ck=i_X0; _pk_id.100001.8cb4=16b116138cf0bc53.1512440302.1.1512440327.1512440302.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0'}
url = 'http://www.douban.com'
r = requests.get(url, cookies = cookies, headers = headers)
with open('douban_2.txt', 'wb+') as f:
    f.write(r.content)
