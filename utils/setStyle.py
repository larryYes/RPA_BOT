import xlwings as xw


# 居中和添加所有边框
def bordersStyle(Bot1_EMPLOYEE_XLSX):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(Bot1_EMPLOYEE_XLSX)
    sht = wb.sheets.active
    all = sht.range('A1').expand()  # 读取所有有数据的单元格

    all.columns.autofit()  # 列宽自适应
    all.api.HorizontalAlignment = -4108  # 水平居中
    all.api.Borders(7).LineStyle = 1  # 左边框
    all.api.Borders(8).LineStyle = 1  # 顶部边框
    all.api.Borders(9).LineStyle = 1  # 底部边框
    all.api.Borders(10).LineStyle = 1  # 右边框

    # Borders(11) 内部垂直边线。
    all.api.Borders(11).LineStyle = 1
    # Borders(12) 内部水平边线。
    all.api.Borders(12).LineStyle = 1
    wb.save()
    wb.close()
    app.quit()
    print("成功设置样式")
