from common.checkpath import check_vrfolder, check_rfolder
from common.execonDUT import execonDUT
import time


def runTest(serial,srcfile,suitename):
    check_vrfolder(serial,suitename) 
    check_rfolder(serial,suitename)
    a = srcfile.split("_")[2].split('x')
    width = a[0]
    height = a[1]
    cmd = 'screenrecord --size ' + width + 'x' + height+ ' --bit-rate 1000000 --time-limit 60 /sdcard/screenrecord_'+width+'_'+height+'_h264.mp4'
    cmd = cmd.replace('\n','')    
    print "cmd: {}".format(cmd)
    return_value = execonDUT(cmd,serial)    
    print return_value[0]

