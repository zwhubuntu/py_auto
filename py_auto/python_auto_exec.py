'''
@author:wenhuizone
'''
import time, os

cmd = " python D:\py_mysql.py "
while True:
    current_time = time.localtime(time.time())
    if ((current_time.tm_hour == 12) and (current_time.tm_min == 30) and (current_time.tm_sec == 0)):
        try:
            os.system(cmd)
            time.sleep(1)
        #print "test python_auto"
        except:
            print "exec scripts error!"