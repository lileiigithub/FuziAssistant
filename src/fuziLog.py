# -*- coding: utf-8 -*-
'''
use dbscan algorithm to segment img of soil;
'''

import logging

class FzLog(object):
    logger =  logging.getLogger("FuziAssistant")
    logger.setLevel(logging.DEBUG)
    #  控制台 handler
    consoleHandle = logging.StreamHandler()
    consoleHandle.setLevel(logging.INFO)
    ch_formatter = logging.Formatter('%(levelname)s - %(message)s')
    consoleHandle.setFormatter(ch_formatter)
    logger.addHandler(consoleHandle)

    # 日志文件 handler
    fileHandle =logging.FileHandler('FuziAssistant.log')
    fileHandle.setLevel(logging.DEBUG)
    fileHandle_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandle.setFormatter(fileHandle_formatter)
    logger.addHandler(fileHandle)

    # def __init__(self):
    #     pass

    @staticmethod
    def debug(msg, *args, **kwargs):
        FzLog.logger.debug(msg, *args, **kwargs)

    @staticmethod
    def info(msg, *args, **kwargs):
        FzLog.logger.info(msg, *args, **kwargs)

    @staticmethod
    def warning(msg, *args, **kwargs):
        FzLog.logger.warning(msg, *args, **kwargs)

    @staticmethod
    def error(msg, *args, **kwargs):
        FzLog.logger.error(msg, *args, **kwargs)


if __name__ == '__main__':
    num = 0
    FzLog.debug("debug:%s",num)
    FzLog.info(num)
    FzLog.error("error")


