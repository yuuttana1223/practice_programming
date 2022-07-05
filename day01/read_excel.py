from openpyxl import load_workbook

wb = load_workbook("hello.xlsx")
# １つ目のタブのシートを取得
sheet = wb.worksheets[0]
cell = sheet["A1"]
print(cell.value)
# Hello, Excel