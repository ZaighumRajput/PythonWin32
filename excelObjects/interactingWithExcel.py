''''Example from Python Win32Com

'''


#Starting up excel
from  win32com.client import Dispatch
xlApp = Dispatch("Excel.Application")
xlApp.Visible = 1 
xlApp.Workbooks.Add()

xlBook = xlApp.Workbooks(1)
xlSheet = xlApp.Sheets(1)


xlBook.Sheets["Sheet2"]

#KeywordArguments
#xlBook.SaveAs(FileName="C:\\Temp\\mysheit.xls")


#Passing Data In and Out
xlSheet.Cells(1,1).Formula = "=ln(5/3)"
xlSheet.Cells(1,1).Value

import time
now = time.time() #Unix time

import pythoncom
time_object = pythoncom.MakeTime(now)
int(time_object)

#Accessing Ranges

myRange1 = xlSheet.Cells(4,1)
myRange2 = xlSheet.Range("B5:C10")
myRange3 = xlSheet.Range(xlSheet.Cells(2,2), xlSheet.Cells(3,8))

