import win32com.client
xl = win32com.client.Dispatch("Excel.Application")
xd = win32com.client.Dispatch("Word.Application")

print xl.Visible
xl.Visible = True
print xl.Visible
xd.Visible = True

xl = None #kills excel
xd = None