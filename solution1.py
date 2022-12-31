import importlib  
from datetime import datetime
record_to_string_library = importlib.import_module("record-to-string-convert")
file_append_library = importlib.import_module("binary-file-append")


## Its called walrus operator , coz it looks like walrus :=
## Walrus operator was first introduced in python 3.8

while (a :=  input('add record or quit: ')) != 'quit':
    

    if a == 'add record':


        input_string = input(' write your comma separated record: ')

       
        list_of_input_string = input_string.split(',')
        list_of_input_string[0] = int(list_of_input_string[0])
        list_of_input_string[2] = datetime.strptime(list_of_input_string[2], record_to_string_library.DATE_STRING_FORMAT).date()
        

        strRecord = record_to_string_library.stringifyRecord(list_of_input_string)
        # print(type(strRecord))
        # print(strRecord)
        
        
        f = file_append_library.createOrOpenFileForAppend("D:\\Lobby\\msc_srd\\output") ## put your desired directory
        file_append_library.appendToFile(f, strRecord+"******")
        file_append_library.closeFile(f)