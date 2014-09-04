"""From Python Win32com
"""
from win32com.client import Dispatch
class easyExcel:
    """A utility to make it easier to get at Excel. Remembering
    to save the data is your problem, as is error handling.
    Operates on one workbook at a time.
    """

    def __init__(self, filename=None):
        self.xlApp = Dispatch("Excel.Application")
        if filename:
            self.filename = filename
            self.xlBook = self.xlApp.Workbooks.Open(filename)

        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = ""
    
    def save(self, newfilename=None):
        if newfilename:
            self.filename = newfilename
            self.xlBook.SaveAs(newfilename)
        else:
            self.xlBook.Save()

    def close(self):
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp

    def getCell(self, sheet, row, col):
        "Get value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        return sht.Cells(row,col).Value

    def setCell(self, sheet, row, col, value):
        "set value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row, col).Value = value

    def setRange(self, sheet, leftCol, topRow, data):
        """insert a 2d array starting at given location.
        Works out the size needed for itself"""

        bottomRow = topRow + len(data) - 1

        rightCol = leftCol + len(data[0]) - 1

        sht = self.xlBook.Worksheets(sheet)
        sht.Range(sht.Cells(topRow, leftCol), sht.Cells(bottomRow, rightCol)).Value = data


    def fixStringsAndDates(self, aMatrix):
        # converts all unicode strings and times
        newMatrix = []
        for row in aMatrix:
            newRow = []
            for cell in row:
                if type(cell) is UnicodeType:
                    newRow.append(str(cell))
                elif type(cell) is TimeType:
                    newRow.append(int(cell))
                else:
                    newRow.append(cell)
            newMatrix.append(tuple(newRow))
        return newMatrix

    def getContiguousRange(self, sheet, row, col):
        """Tracks down and across from top left cell unit it
        encountours blank cells; returns the non-blank range.
        Looks at first row and column
        Blanks at bottom or right
        are OK and return None within the array
        """

        sht = self.xlBook.Worksheets(sheeT)

        # find the bottom row
        bottom = row
        while sht.Cells(bottom + 1, col).Value not in [None, ""]:
            bottom = bottom + 1

        # right column
        right = col
        while sht.Cells(row, right + 1).Value not in [None, ""]:
            right = right + 1

        return sht.Range(sht.Cells(row, col), sht.Cells(bottom, right)).Value

