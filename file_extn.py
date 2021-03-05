import os
entries = os.listdir()
print(entries)

inputfilename=input('Enter the filename:')
file_extension= inputfilename.split('.')
print('The extension of the file is:'+str(file_extension[-1]))





        
