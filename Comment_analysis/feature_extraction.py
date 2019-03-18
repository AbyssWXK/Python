#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
import openpyxl
import os
import sys
import jieba
reload(sys)
sys.setdefaultencoding('utf-8')

fname= "comment.xlsx"
data = xlrd.open_workbook(fname)
table = data.sheet_by_name(u'Comments')
comment_list = table.col_values(2)
seg_list = []
for comment in comment_list:
    # print(coment)
    seg_cut = jieba.lcut(comment, cut_all=False)
    for seg in seg_cut:
        seg_list.append(seg)
seg_numb = []
seg_down = []
for seg in seg_list:
    if seg in seg_down:
        continue
    seg_down.append(seg)
    numb = 0
    for seg_times in seg_list:
        if seg_times == seg:
            numb = numb + 1
    dict = {'seg':seg,'numb':numb}
    seg_numb.append(dict)
seg_sorted = sorted(seg_numb, key = lambda x : x['numb'], reverse=True)
print(seg_sorted)

excel_value = []
wb=openpyxl.Workbook()
sheet = wb.active
sheet.title = "seg_numb_sorted"
for seg_in_dict in seg_sorted:
    seg = seg_in_dict['seg']
    numb = str(seg_in_dict['numb'])
    value = [seg, numb]
    excel_value.append(value)
for i in range(0, 100):
        for j in range(0, len(excel_value[i])):
            sheet.cell(i+1, j+1, value = str(excel_value[i][j]))
wb.save("seg_numb_sorted.xlsx")
print("写入数据成功！")


