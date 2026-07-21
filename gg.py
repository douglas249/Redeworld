from openpyxl import Workbook

conectores1 = 'comida'
conectores2 = 'maca'
conectores3 = 'banana'
wb = Workbook()
planilha = wb.worksheets[0]


planilha['A2'] = conectores1
planilha['A3'] = conectores2
planilha['A4'] = conectores3

wb.save(r"C:\Users\Cristian\OneDrive\Desktop\Projetos.xlsx")
      
               

        