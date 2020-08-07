# coding: utf-8
"""
异常处理文件
"""

import sys
from utils.myLog import log

logger = log.get_logger()


class exception:
    # 异常处理
    def getException(status):
        if status == 200:
            logger.info("程序正常退出")
            sys.exit("程序正常退出")
        elif status == 201:
            logger.warning("无符合要求的数据", exc_info=True)
            sys.exit("无符合要求的数据")
        elif status == 202:
            logger.warning("无符合类型要求的数据", exc_info=True)
            sys.exit("无符合类型要求的数据")
        elif status == 203:
            logger.warning("无法找到该文档", exc_info=True)
            sys.exit("无法找到该文档")
        elif status == 204:
            logger.warning("无法获取要写入的列标题", exc_info=True)
            sys.exit("无法获取要写入的列标题")
        else:
            print("程序无异常")
            logger.info("程序无异常")
