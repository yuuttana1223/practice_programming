from openpyxl import load_workbook

wb = load_workbook("cellname100.xlsx")
sheet = wb.active

# 行単位で取り出す
for row in sheet["C2":"F4"]:
    values = [cell.value for cell in row]
    print(values)
    # ['C2', 'D2', 'E2', 'F2']
    # ['C3', 'D3', 'E3', 'F3']
    # ['C4', 'D4', 'E4', 'F4']
