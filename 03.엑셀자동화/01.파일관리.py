import openpyxl

# 새로운 엑셀 파일 생성
wb = openpyxl.Workbook()

# 현재 확성화된 sheet 선택
ws = wb.active

# sheet 이름 변경
ws.title = '자동화로만든sheet'

# 엑셀 저장
wb.save('자동화된엑셀.xlsx')
