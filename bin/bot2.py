import xlwings as xw

from utils.readData import readExcel
from setting import *




if __name__ == '__main__':
    bot2DataList = readExcel(Bot2_Data_Xlsx)
    bot2MacroSheetList = readExcel(Bot2_MacroSheet_Xlsx)
