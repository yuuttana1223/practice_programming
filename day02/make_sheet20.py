from openpyxl import Workbook

book = Workbook()

# 20個のシートを作成して、シート名を指定
for i in range(1, 20 + 1):
    sheet_name = f"シート{i}"
    sheet = book.create_sheet(title=sheet_name)
    sheet["A1"].value = sheet_name

# 最初から存在するSheetという名前のシートを削除
book.remove(book.worksheets[0])
book.save("sheet20.xlsx")