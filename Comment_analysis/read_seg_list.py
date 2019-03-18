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