import xlwings as xw

from utils.myException import exception
from utils.readData import readExcel
from setting import *
from utils.writeData import toExcel


def filterData(list1, list2):
    dataList = []
    existlist = ['Corporation Bank', 'SBI', 'HDFC', 'ICICI']
    j = 1
    for i in range(1, len(list1)):
        paymentModeData = list1[i][1]
        bankNameData = list1[i][2]
        rrnData = list1[i][3]

        for i in range(1, len(list2)):
            paymentModeMacro = list2[i][1]
            bankNameMacro = list2[i][2]
            rrnMacro = list2[i][4]
            macroName = list2[i][5]
            if paymentModeData == paymentModeMacro and bankNameData == bankNameMacro and rrnData == rrnMacro:
                dataList.append([j, paymentModeMacro, bankNameMacro, rrnMacro, macroName])
                j += 1
                list2[i][1] = "该行数据已添加"
            elif (
                    bankNameData in existlist and bankNameMacro == '-') and paymentModeData == paymentModeMacro and rrnData == rrnMacro:
                dataList.append([j, paymentModeMacro, bankNameMacro, rrnMacro, macroName])
                j += 1
                list2[i][1] = "该行数据已添加"
                # del list2[i]

    return dataList


if __name__ == '__main__':
    # 读取data表所有数据
    bot2DataList = readExcel(Bot2_Data_Xlsx)
    # 读取macrosheet表所有数据
    bot2MacroSheetList = readExcel(Bot2_MacroSheet_Xlsx)
    # 筛选匹配的数据
    data = filterData(bot2DataList, bot2MacroSheetList)
    SAVE_PATH = '../Bot2/' + 'liugji@digitalchina.com' + '_Bot2_Output.xlsx'
    # 将匹配的数据写入新表中
    toExcel(data, Bot2_Data_Xlsx, A_Row='a2', SAVE_PATH=SAVE_PATH)
# 正常退出程序
exception.getException(status=200)