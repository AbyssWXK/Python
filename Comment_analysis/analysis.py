#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
import openpyxl
import os
import sys
import jieba
import importlib,sys
from xlutils.copy import copy

importlib.reload(sys)
import classifiers as cl
# sys.setdefaultencoding('utf-8')

def write_in_excle(result,i,ws):

    ws.write(i + 1, 3, str(result))

fname= "comment.xlsx"
data = xlrd.open_workbook(fname)
table = data.sheet_by_name(u'Comments')
comment_list = table.col_values(2)
d = cl.DictClassifier()
i=0
new_excel = copy(data)
ws = new_excel.get_sheet(0)

result_list = []
for comment in comment_list:
    result = d.analyse_sentence(comment)
    result_list.append(result)
result_min = result_list[0]
for result in result_list:
    if result <result_min:
        result_min = result
print(result_min)
for result in result_list:
    result = -1*result/result_min
    write_in_excle(result, i, ws)
    i = i + 1




new_excel.save('new_comments.xls')
