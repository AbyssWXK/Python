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
    url = 'https://maoyan.com/board/4?offset='
    names = []
    for i in range(0,10):
        page = i*10
        urli = url + str(page)
        # print(urli)
        text = get_page(urli)
        # print(text)
        pattern = re.compile('<p\sclass="name"><a.*?title="(.*?)".*?<p\sclass="star">\s+(\S+)\s+</p>\s+<p\sclass="releasetime">(\S+)</p>.*?<i\sclass="integer">(.*?)<.*?class="fraction">(\d)',re.S)
        names.extend(re.findall(pattern,text))
    moives=[]
    fp=open('maoyan100.txt','w+',encoding='utf-8')
    for moive in names:
        name = [moive[0],moive[1],moive[2],str(moive[3])+str(moive[4])]
        for ele in name:
            fp.write(ele+' ')
        fp.write('\n')
        moives.append((name))
        print(name)
if __name__ == '__main__':
            main()