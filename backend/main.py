import sys
import datetime
import subprocess
import time




#Current directory
SRC_PATH="C:\\Users\\SKSHREYA\\Desktop\\msgGenerator-gui\\backend"

#Filebeat input directory
DST_PATH="C:\\Users\\SKSHREYA\\Desktop\\msgGenerator-gui\\backend\\output"

#USE CASE (User will provide case number as 1,2 or 3)
CASE1_Percent=sys.argv[1]

#Maximum number of message within 60 seconds
#MAX_MSG=$2
TOTAL_MSG=sys.argv[2]

# FILENAME='synthetic_data_'+date+'.json'
# cmd = "python "+SRC_PATH+"\\json_generator.py "+TOTAL_MSG+" tmp.json "+CASE1_Percent
# cmd2= "cp tmp.json "+DST_PATH+"\\"+FILENAME
# cmd3= "rm -f tmp.json"

# print(CASE1_Percent)
# print(TOTAL_MSG)

# print(FILENAME)
# print(cmd)
# print(cmd2)
# print(cmd3)
# print(SRC_PATH)
# print(DST_PATH)


while True:
    date = datetime.datetime.now()
    date= date.strftime('%y%m%d_%H%M%S')
    FILENAME='synthetic_data_'+date+'.json'
    cmd = "python "+SRC_PATH+"\\json_generator.py "+TOTAL_MSG+" tmp.json "+CASE1_Percent
    cmd2= "copy tmp.json "+DST_PATH+"\\"+FILENAME
    cmd3= "del /f tmp.json"
    print( subprocess.getoutput(cmd) )
    print( subprocess.getoutput(cmd2) )
    print( subprocess.getoutput(cmd3) )
    print(FILENAME)
    time.sleep(1)
