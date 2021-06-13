import openpyxl

# Work book is class Hence creating object of workbook and a workbook wil create internally . by default sheet will
# be there
wk = openpyxl.Workbook()
sh = wk.active
sh.title = "HellTestings"
print(sh.title)

sh['A4'].value = "www.Gmail.com"  # Writing the data in A4 column

# 3. We are going to enter the data in to the second sheet
wk.create_sheet(title="Hello")  # This is to create the sheet and write the title of sheet and second sheet is created
sh1 = wk['Hello']
sh1['A3'] = "+91-2345678"

# To remove any sheet
wk.remove((wk['Hello'])) # We need to pass the object of the shet no only name

# Saving
wk.save("C:\\developement\\Writedata.xlsx")  # Saving the document and provide the path
