import importlib
from datetime import date

binary_file_read_library = importlib.import_module("binary-file-read")
record_to_string_library = importlib.import_module("record-to-string-convert")

type_list = [int, str, date, str]

file = binary_file_read_library.openFile("D:\\Lobby\\msc_srd\\output")

a = file.read().decode()

limit = len(a.split("******"))-1

binary_file_read_library.jumpToReadingOffset(0, file)

for i in range(limit):


    record = binary_file_read_library.readRecord(file).decode()
    
    _record = record_to_string_library.retrieveRecordFromString(record, type_list)
    print(_record)
    
binary_file_read_library.closeFile(file)