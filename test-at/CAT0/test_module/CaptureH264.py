from common.execonDUT import execonDUT,remount,reboot 
import time,subprocess 
from common import getlog, play,getinfo


def runTest(serial,srcfile,suitename): 
    confile = 'conf/media_profiles/'+ suitename+'/'+srcfile 
    print remount(serial)[0]
   
    
    #cmd = 'adb -s ' + serial + "wait-for-device pull /etc/media_profiles.xml ../Testcase/result" 
    cmd = 'adb -s ' + serial + " wait-for-device push " + confile + ' /etc/media_profiles.xml' 
    cmd =cmd.replace('\n','')
    print cmd
    p = subprocess.call(cmd, shell = True)
    cmd = 'rm -r /sdcard/DCIM/Camera/'
    execonDUT(cmd, serial)
    time.sleep(3)
    reboot(serial)
    print '{}'.format('rebooting')
    time.sleep(10)
    raw_input('start record:')
    getlog.start(serial,suitename,srcfile) 
    time.sleep(10)
    raw_input('end record:')
    getlog.end(serial,suitename, srcfile)
    returnValue = execonDUT('ls /sdcard/DCIM/Camera/',serial)
    print returnValue[0]
    dfile = ' ../Testcase/result/'+suitename + '/'+ srcfile + '.mp4' 
    cmd = 'adb -s ' + serial + " pull /sdcard/DCIM/Camera/" + str(returnValue[0]) + dfile 
    cmd = cmd.replace('\r','')
    cmd = cmd.replace('\n','')
    print cmd
    p = subprocess.call(cmd, shell=True) 
    execonDUT('input keyevent 4',serial)
    execonDUT('input keyevent 4',serial)
    time.sleep(2)
    play.playfile(serial,'DCIM/Camera/'+returnValue[0])
    getinfo.getfps(dfile)
    getinfo.getresolution(dfile)
    
