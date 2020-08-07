"""
发送邮件
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
from utils.myLog import log


def email(sheetFile, receivers, filename):
    # 登陆邮件服务器
    log.get_logger().info("正在发送邮件")
    smtpObj = smtplib.SMTP('smtp.qq.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    log.get_logger().info("设置收发人信息")
    # 传入相应的账号密码信息
    smtpObj.login('1430826258@qq.com', 'tdqvrjdewizwiceg')
    # 邮件收发信人信息
    sender = '1430826258@qq.com'  # 发件人信息
    receivers = [receivers]  # 收件人信息
    # receivers = ['liugji@digitalchina.com']  # 收件人信息

    # 完善发件人收件人，主题信息
    message = MIMEMultipart()
    message['From'] = formataddr(["RPA自动发送", sender])
    message['To'] = formataddr(["liugji", ''.join(receivers)])
    subject = 'Python SMTP 邮件， RPA邮件'
    message['Subject'] = Header(subject, 'utf-8')

    log.get_logger().info("尝试添加表格附件")
    # 尝试添加表格附件
    # sheetFile = "./excel/1、作业员入社名单（人事）.xls"
    print("表格附件文件名为：%s" % sheetFile)
    sheetFileLoc = os.path.join(sheetFile)
    sheetAtt = MIMEText(open(sheetFileLoc, 'rb').read(), 'base64', 'gb2312')
    sheetAtt.add_header('Content-Disposition', 'attachment', filename=filename)  # 附件的名字
    message.attach(sheetAtt)

    try:
        # 发送邮件操作
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        log.get_logger().info('成功:发送一封邮件')

    except smtplib.SMTPException:
        log.get_logger().error('失败：邮件无法发送')
