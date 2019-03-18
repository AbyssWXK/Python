import requests
import re
def get_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML,like Gecko)'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def main():
    singers = []
    for i in range(0,50):
        urli = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI8247160107523648&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22singerList%22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%22%2C%22param%22%3A%7B%22area%22%3A-100%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%3A-100%2C%22sin%22%3A'+ str(i*80) +'%2C%22cur_page%22%3A3%7D%7D%7D'
        # print(urli)
        text = get_page(urli)
        pattern = re.compile('{"country":"(.*?)","singer_id":(.*?),"singer_mid":"(.*?)","singer_name":"(.*?)","singer_pic":"(.*?)"}',re.S)
        # print(text)
        partSingers= re.findall(pattern, text)
        print(partSingers)
        singers.extend(partSingers)
    fp=open('QQmusicSingers.txt','w+',encoding='utf-8')
    for singer in singers:
        for ele in singer:
            fp.write(ele+' ')
        fp.write('\n')
if __name__ == '__main__':
            main()