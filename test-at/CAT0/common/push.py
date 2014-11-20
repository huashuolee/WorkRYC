from common.execonDUT import execonDUT
from common.checkpath import check_vrfolder, check_rfolder, checkfile
import time,subprocess

def pushfile(serial,filename,suitename):
    # check the Directory:vp8_encode
    return_value = check_vrfolder(serial,suitename)
    if str(return_value[0]).strip()=="Directory not found":
        print "mdkir -p /sdcard/video-test \n"
        execonDUT('mkdir -p /sdcard/video-test/clip',serial)
        time.sleep(1)
    #else: print "Directory exists"
    # check the Directory: result
    return_value = check_rfolder(serial,suitename)
    if str(return_value[0]).strip()=="Directory not found":
        print "mdkir -p /sdcard/video-test/result \n"
        execonDUT('mkdir -p /sdcard/video-test/result/'+suitename,serial)
        time.sleep(1)
   # else: print "Directory exists"

    
    # check the file
    return_value = checkfile(serial,filename,suitename)
    if str(return_value[0]).strip()=='file not found':
        print 'file not found'
        cmd = "../Clip/"+filename + " /sdcard/video-test/clip/" 
        mycmd = 'adb -s ' + serial + ' push ' + cmd
        mycmd = mycmd.replace('\n','')
        print mycmd
        p = subprocess.call(mycmd, shell=True)
        print "file is pushed"
    else: print "File exists"

def pushconf():
    pass
