# coding=utf-8
import copy

import MusicParse


def search(keyword):
    search_url = 'http://songsearch.kugou.com/song_search_v2?keyword={}page=1'.format(keyword)
    # 这里需要判断一下，ip与搜索字段可能会限制搜索，total进行判断
    total = MusicParse.parse(search_url)['data']['total']
    if total != 0:
        search_total_url = search_url + '&pagesize=%d' % total
        music_list = MusicParse.parse(search_total_url)['data']['lists']
        item, items = {}, []
        for music in music_list:
            if music['SQFileHash'] != '00000000000000000000000000000000':
                item['Song'] = music['SongName']  # 歌名
                item['Singer'] = music['SingerName']  # 歌手
                item['Hash'] = music['SQFileHash']  # 歌曲无损hash
                items.append(copy.deepcopy(item))
        return items
    else:
        return None


if __name__ == '__main__':
    search()
