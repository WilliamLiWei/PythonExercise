import requests
import html5lib
import re
from bs4 import BeautifulSoup


s = requests.Session()
url_login = 'https://www.douban.com/accounts/login?source=main'

formdata = {
    'redir':'https://www.douban.com',
    'form_email': '13651103204',
    'form_password': 'liwei200023',
    'login': u'登陆'
}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}

r = s.post(url_login, data = formdata, headers = headers)
content = r.text
soup = BeautifulSoup(content, 'html5lib')
captcha = soup.find('img', id = 'captcha_image')
if captcha:
    captcha_url = captcha['src']
    re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/>'
    captcha_id = re.findall(re_captcha_id, content)
    print(captcha_id)
    print(captcha_url)
    captcha_text = input('Please input the captcha:')
    formdata['captcha-solution'] = captcha_text
    formdata['captcha-id'] = captcha_id
    r = s.post(url_login, data = formdata, headers = headers)    
with open('contacts.txt', 'w+', encoding = 'utf-8') as f:
    f.write(r.text)
    print('ok')

