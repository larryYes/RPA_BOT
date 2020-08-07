# coding: utf-8
'''
文件数据写入
'''

import xlwings as xw
from utils.myLog import log


#配置日志和异常
logger = log.get_logger()

#将list数组写入Excel表格，SHEET_NUMBER为传入第几个sheet，A_Row为从第几行开始写入
def toExcel(list,EXCEL_FILE,SHEET_NUMBER=0,A_Row='a1',SAVE_PATH=None):
    print("=======你即将写入的数据为：=======")
    print(list)
    print("=============================")

    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(EXCEL_FILE)
    wb.sheets[SHEET_NUMBER].range(A_Row).expand('table').value = list
    wb.save(SAVE_PATH)
    wb.close()
    app.quit()
    logger.info("成功：list已写入Excel表格")
