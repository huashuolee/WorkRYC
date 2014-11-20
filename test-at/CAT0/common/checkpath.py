from common.execonDUT import execonDUT


def check_vrfolder(serial,suitename):
    cmd = "test -d /sdcard/video-test/clip" + " && echo 'Directory exists' || echo 'Directory not found'"
    result = execonDUT(cmd,serial)
    return result
def check_rfolder(serial,suitename):
    cmd = "test -d /sdcard/video-test/result/"+suitename + " && echo 'Directory exists' || echo 'Directory not found'"
    result = execonDUT(cmd,serial)
    return result
def checkfile(serial,filename,suitename):
    cmd = "test -f /sdcard/video-test/clip/" + filename + " && echo 'File exists' || echo 'file not found'"
    result = execonDUT(cmd,serial)
    return result
	
