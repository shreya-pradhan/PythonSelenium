import xlsxwriter

def CreateWorkBook(name,items,price):
    workbook=xlsxwriter.workbook("workbook")
    worksheet=workbook.add_worksheet()
    row=1
    i=0
    j=0
    for item in items:

        if(item=='*'| i==0) :
            worksheet.write(row,0,name[i])
            j=j+1


        worksheet.write(row,1,item)
        worksheet.write(row,2,price[i])
        i=i+1
        row=row+1
    workbook.close()

