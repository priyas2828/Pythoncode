# import package
import openpyxl

# Create object of workbook and load the excel with path
wk = openpyxl.load_workbook("C:\\developement\\ReadandWriteData.xlsx")

# With objectname fetch the total sheetname
print(wk.sheetnames)

# This is ti fetch the current sheet with title
print("Active sheet is " + wk.active.title)

# Create any object of sheet in which you want to work
# We are finding sheet level and fetching the data
sh=wk['Sample']
print(sh.title)

