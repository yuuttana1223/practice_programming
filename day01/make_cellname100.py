from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

# excelのautofill機能を使えば本来は十分
for i in range(1, 100 + 1):
    for j in range(1, 100 + 1):
        cell = sheet.cell(row=i, column=j)
        # coordinate A1, A2, B1などのセル名を取れる
        cell.value = cell.coordinate
wb.save("cellname100.xlsx")