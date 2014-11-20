from common.push import pushfile
from common.execonDUT import execonDUT
import time


def runTest(serial,srcfile,suitename):
    pushfile(serial,srcfile,suitename)
    time.sleep(3)
    a = srcfile.split("_")[2].split('x')
    width = a[0]
    height = a [1] 
    cmd = "am startservice -n com.test.vp8/com.test.vp8.Vp8IntentService -e in /sdcard/video-test/clip/" + srcfile + " -e out /sdcard/video-test/result/"+suitename+'/' +suitename+'_'+ srcfile + ".ivf" + " --ei w "+ width + " --ei h " + height + " --ei fps 30"
    cmd = cmd.replace('\n','')    
    print cmd
    return_value = execonDUT(cmd,serial)    
    print return_value[0]

