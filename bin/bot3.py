from utils.downFile import down
from setting import *
import pdfplumber

if __name__ == '__main__':
    # 下载网页中的文档
    # down(Bot3_URL, username="candidate", password="LetMeIn123!")

    path = '../bot3/invoice01.pdf'
    pdf = pdfplumber.open(path)

    for page in pdf.pages:
        # 获取当前页面的全部文本信息，包括表格中的文字
        print(page.extract_text())

        # for table in page.extract_tables():
        #     for row in table:
        #         print(row)
        #     print('---------- 分割线 ----------')
    pdf.close()
