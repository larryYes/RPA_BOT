# coding: utf-8
'''
常量配置文件
'''

#日志记录
loggers = {}
LOG_ENABLED = True  # 是否开启日志
LOG_TO_CONSOLE = True  # 是否输出到控制台
LOG_TO_FILE = True  # 是否输出到文件
LOG_TO_ES = False  # 是否输出到 Elasticsearch
LOG_PATH = "../report/runtime.log"  # 日志文件路径
LOG_LEVEL = 'DEBUG'  # 日志级别
LOG_FORMAT = '%(levelname)s - %(asctime)s - process: %(process)d - %(filename)s - %(name)s - %(lineno)d - %(module)s - %(message)s'  # 每条日志输出格式
# ELASTIC_SEARCH_HOST = 'eshost'  # Elasticsearch Host
# ELASTIC_SEARCH_PORT = 9200  # Elasticsearch Port
# ELASTIC_SEARCH_INDEX = 'runtime'  # Elasticsearch Index Name
APP_ENVIRONMENT = 'dev'  # 运行环境，如测试环境还是生产环境

Bot1_EMPLOYEE_XML = "../bot1/employee.xml"
Bot1_EMPLOYEE_XLSX = "../bot1/employee.xlsx"

Bot2_Data_Xlsx = "../bot2/Data.xlsx"
Bot2_MacroSheet_Xlsx = "../bot2/MacroSheet.xlsx"

Bot3_URL = 'http://rpademo.automationanywhere.com/master-pdf.php'
Bot3_XLSX = '../bot3/invoice_template.xlsx'
Bot3_Invoice_XLSX = '../bot3/invoice.xlsx'