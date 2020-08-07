# coding: utf-8
'''
bot1作业主函数
'''
from setting import *
import bs4
from utils.myException import exception
from utils.myLog import log
from utils import writeData,sendEmail
from utils.setStyle import *
#日志导入
from utils.readData import readExcel
import xlwings as xw

logger = log.get_logger()


def xmlToList(file_xml):
    xml = open(file_xml,'r')
    doc = bs4.BeautifulSoup(xml,features='xml')
    employees = doc.select("Employee")
    #存储xml数据的数组
    xmlList = []

    for employee in employees:
        firstName = employee.FirstName.text
        lastName = employee.LastName.text
        contactNo = employee.ContactNo.text
        email = employee.Email.text
        city = employee.Address.City.text
        state = employee.Address.State.text
        zip = employee.Address.Zip.text
        years = int(employee.Years.text)
        performance = int(employee.Performance.text)

        #筛选符合要求的数据
        if years>=5 and performance>=5 and city=='NY' and state == 'New York':
            xmlList.append([firstName,lastName,contactNo,email,city,state,zip,years,performance,'Y'])
        else:
            xmlList.append([firstName,lastName,contactNo,email,city,state,zip,years,performance,'N'])

    #异常处理
    if len(xmlList) == 0:
        exception.getException(status=201)

    return xmlList

#按题目要求筛选数据
def filterData(list):
    outList = []
    #将列标题加入列表
    outList.append(list[0])
    #筛选Gratuity-Eligibility合格的数据
    for i in range(len(list)):
        if list[i][9] == 'Y':
            outList.append(list[i])
    return outList



#====程序入口====================================================================
if __name__ == '__main__':
    logger.info("======程序开始运行======")
    #读取xml、写入Excel，读取Excel，筛选符合条件的数据、将每条数据保存为对应的Excel文件、将每个Excel文件发送给对应的人

    #将xml文件数据提取到list中
    list=xmlToList(Bot1_EMPLOYEE_XML)

    # 将list数组全部写入Excel
    writeData.toExcel(list,Bot1_EMPLOYEE_XLSX,SHEET_NUMBER=0,A_Row='a2')

    bordersStyle(Bot1_EMPLOYEE_XLSX) #设置样式

   # 读取employee.xlsx,筛选表格数据
    logger.info("读取并筛选表格数据")
    listExcel = filterData(readExcel(Bot1_EMPLOYEE_XLSX))
    print("筛选得到的数据为：" )
    print(listExcel)

    #提取收件人邮箱和创建并设置附件名称
    EXCEL_FILE = []
    receivers = []
    receivers.append('liugji@digitalchina.com')
    for i in range(1, len(listExcel)):
        # 新建每一个所需发送的员工的表格
        app = xw.App(visible=False, add_book=False)
        wb = app.books.add()
        EXCEL_FILE.append("../report/" + listExcel[i][3] + "_Bot_1_Output.xlsx")
        bordersStyle(EXCEL_FILE[i - 1])#设置表格样式
        receivers.append(listExcel[i][3])
        wb.save(EXCEL_FILE[i - 1])
        wb.close()
        app.quit()



    # 二维列表按列取元素
    outPut = [i[7:10] for i in listExcel]
    #将数据写入各自的表格中
    for i in range(1,len(outPut)):
        writeData.toExcel([outPut[0],outPut[i]],EXCEL_FILE[i-1])
        filename=receivers[i]+"_Bot_1_Output.xlsx"
        print("收件人邮箱：" + receivers[i])
        # sendEmail.email(EXCEL_FILE[i], receivers[0],filename)

    # 正常退出程序
    exception.getException(status=200)






