import xlwings as xw
from utils.myLog import log
import pdfplumber


# 读取Excel表中的所有数据
def readExcel(EXCEL_FILE):
    app = xw.App(visible=False, add_book=False)
    # 新建工作簿 wb = app.books.add()
    wb = app.books.open(EXCEL_FILE)
    # 引用工作表
    sht = wb.sheets[0]
    listExcel = sht.range('A1').expand().value  # 读取所有的值
    # listExcel = []
    # #计算单元格的行数
    # rng = sht.range('a1').expand('table')
    # nRows = rng.rows.count
    # #读取数据存入列表
    # for i in range(1,nRows+1):
    #     listExcel.append(sht.range(f"a{i}:j{i}").value)
    print("=============从Excel读取到的数据为：=============")
    print(listExcel)
    wb.save()
    wb.close()
    app.quit()
    log.get_logger().info("成功：读取Excel", exc_info=True)
    return listExcel


def readPdf(path):
    pdf = pdfplumber.open(path)
    pdfText = pdf.pages[0]
    text = pdfText.extract_text()
    pdf.close()
    return text
