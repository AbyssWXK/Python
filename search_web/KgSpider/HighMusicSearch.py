# coding=utf-8
import copy
import hashlib

import MusicParse
import MusicSearch

# V2版系统,pc版,加密方式为md5(hash +"kgcloudv2")
Music_api_1 = 'http://trackercdnbj.kugou.com/i/v2/?cmd=23&pid=1&behavior=download'
# V2版系统,手机版,加密方式为md5(hash +"kgcloudv2") （备用）
Music_api_2 = 'http://trackercdn.kugou.com/i/v2/?appid=1005&pid=2&cmd=25&behavior=play'
# 老版系统,加密方式为md5(hash +"kgcloud")（备用）
Music_api_3 = 'http://trackercdn.kugou.com/i/?cmd=4&pid=1&forceDown=0&vip=1'


def V2Md5(Hash):  # 用于生成key,适用于V2版酷狗系统
    return hashlib.md5((Hash + 'kgcloudv2').encode('utf-8')).hexdigest()


def Md5(Hash):  # 用于老版酷狗系统
    return hashlib.md5((Hash + 'kgcloud').encode('utf-8')).hexdigest()


def HighSearch(keyword):
    music_list = MusicSearch.search(keyword)
    if music_list is not None:
        item, items = {}, []
        for music in music_list:
            Hash = str.lower(music['Hash'].encode('utf-8'))
            key_new = V2Md5(Hash)  # 生成v2系统key
            try:
                DownLoadUrl = MusicParse.parse(Music_api_1 + '&hash=%s&key=%s' % (Hash, key_new))['url']
                item['Song'] = music['Song'].encode('utf-8')  # 歌名
                item['Singer'] = music['Singer'].encode('utf-8')  # 歌手
                item['url'] = DownLoadUrl
                items.append(copy.deepcopy(item))
            except KeyError:
                pass
        return items


if __name__ == '__main__':
    HighSearch()


