from datetime import datetime

import pandas

from utils.downFile import down
from setting import *
import pdfplumber
import re
from utils.readData import readPdf, readExcel
from utils.setStyle import bordersStyle
from utils.writeData import toExcel


def filterData(str):
    list = []
    # 正则表达式
    data1 = re.compile(r'(DUE DATE\s*)(\w*)\s*(\w*\s\w*\s\w*)\s*(\w*\s\w*\s\w*)')
    invoiceNo = re.compile(r'86753\d*').search(text).group()
    dateList = re.compile(r'\d*-\w*-\d*').findall(text)
    company = re.compile(r'(INVOICE TO\s*)(\w*)').search(text).group(2)  # 将匹配内容分为两个模块，输出第二个模块
    salesPerson = data1.search(text).group(2)
    job = data1.search(text).group(3)
    paymentTerms = data1.search(text).group(4)
    # test=re.compile(r'(\d*)\s*(\w*\s\w*\s\w*\s\w*(\(.*\))?)\s*(\$\d*\.\d*)\s*(\$\d*\.\d*)').findall(text)#.group()
    data2=re.compile(r'(\d*.+)\s\s(\$\d*\.\d*)\s*(\$\d*,?\d*\.\d*)').findall(text)#.group()
    for i in range(len(data2)):
        quantity=re.compile(r'(\d*)\s(.*)').search(data2[i][0]).group(1)
        description=re.compile(r'(\d*)\s(.*)').search(data2[i][0]).group(2)
        list.append([company, dateList[0], invoiceNo, salesPerson, job, paymentTerms, dateList[1], quantity, description,data2[i][1],data2[i][2]])

    return list


if __name__ == '__main__':
    # 下载网页中的文档
    # down(Bot3_URL, username="candidate", password="LetMeIn123!")

    # 提取表格数据
    listData =[]
    for i in range(1, 7):
        # 读取PDF中的数据
        path = '../bot3/invoice0' + str(i) + '.pdf'
        text = readPdf(path)
        listData.extend(filterData(text))
    print("你总共写入数据量为：",len(listData))
    toExcel(listData,Bot3_XLSX,A_Row='a2')#将提取到的数据写入表格
    bordersStyle(Bot3_XLSX)#设置样式
    listBot3 = readExcel(Bot3_XLSX)#读取Excel表中所有数据

    #筛选数据
    listBot3Out = []
    for i in range(1,len(listBot3)):
        time = (listBot3[i][6] - datetime(2019, 5, 1)).total_seconds()
        if listBot3[i][7] >= 2 and listBot3[i][9] >=2 and  listBot3[i][10] >= 100 and listBot3[i][5]=="Due on Receipt" and time>0:
            listBot3Out.append(listBot3[i])
    save_path = '../bot3/liugji@digitalchinal.com_Bot_3_Output.xlsx'
    toExcel(listBot3Out, Bot3_Invoice_XLSX, A_Row='a2', SAVE_PATH=save_path)
    bordersStyle(Bot3_Invoice_XLSX)  # 设置样式


