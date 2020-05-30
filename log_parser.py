import re
import time
from time import strftime
from datetime import datetime

 
def main():
    log_file_path = r"/Users/mondini/Documents/Falabella/log_parser/out.txt"
    export_file_path = r"/Users/mondini/Documents/Falabella/log_parser/out.log"
 
    time_now = datetime.now()
    export_file = open(export_file_path, "wt")
 
    regex = '(UTC\s[A-Z][a-z]*\s[0-9]*\s[0-9]*:[0-9]*:[0-9]*)'
    timeIso = time_now.isoformat()
    parseData(log_file_path, export_file, regex, timeIso)
 
 
 
def parseData(log_file_path, export_file, regex, timeIso):
    file = open(log_file_path,("rw"))
    for i, line in enumerate(open(file)):
        data = file.read()
        data.replace(timeIso, regex)
        export_file.write(data)
            
if __name__ == '__main__':
    main()