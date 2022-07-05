from openpyxl import Workbook

wb = Workbook()
# アクティブなシートを取得(１つ目のタブ？)
sheet = wb.active
sheet["A1"] = "Hello, Excel"
wb.save("hello.xlsx")