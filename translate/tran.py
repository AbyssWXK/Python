# -*- coding: utf-8 -*-
import xlrd
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

fname= "dict.xlsx"
data = xlrd.open_workbook(fname)
table = data.sheet_by_name(u'Sheet1')
le = 'le.txt'
hao = 'hao.txt'
nu = 'nu.txt'
ai = 'ai.txt'
ju = 'ju.txt'
e = 'e.txt'
jing = 'jing.txt'
for i in range(table.nrows):
    lx = table.row_values(i)
    if lx[4]=='PA' or lx[4]=='PE':
        with open(le,'a') as fle:
            s= str(lx[0])+' '+ str(lx[5])+'\n'
            fle.write(s)

    elif lx[4]=='PD' or lx[4]=='PH'or lx[4]=='PG'or lx[4]=='PB'or lx[4]=='PK':
        with open(hao,'a') as fhao:
            s = str(lx[0]) + ' ' + str(lx[5])+'\n'
            fhao.write(s)

    elif lx[4]=='NA':
        with open(nu,'a') as fnu:
            s = str(lx[0]) + ' ' + str(lx[5])+'\n'
            fnu.write(s)

    elif lx[4]=='NB'or lx[4]=='NJ' or lx[4]=='NH' or lx[4]=='PF':
        with open(ai,'a') as fai:
            s = str(lx[0]) + ' ' + str(lx[5])+'\n'
            fai.write(s)

    elif lx[4]=='NI'or lx[4]=='NC' or lx[4]=='NG':
        with open(ju,'a') as fju:
            s = str(lx[0]) + ' ' + str(lx[5])+'\n'
            fju.write(s)

    elif lx[4]=='NE'or lx[4]=='ND' or lx[4]=='NN'or lx[4]=='NK' or lx[4]=='NL':
        with open (e,'a') as fe:
            s = str(lx[0]) + ' ' + str(lx[5])+'\n'
            fe.write(s)

    else :
        with open (jing,'a') as fjing:
            s = str(lx[0]) + ' ' + str(lx[5])+'\n'
            fjing.write(s)