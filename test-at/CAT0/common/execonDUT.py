import subprocess


def execonDUT(cmd,serial):
    mycmd = 'adb -s ' + serial + ' shell ' + ' "'+cmd+' "'
    mycmd = mycmd.replace('\n','')
    print mycmd
    p = subprocess.Popen(mycmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout, stderr

def remount(serial):
    mycmd = 'adb -s ' + serial+ ' wait-for-device root && adb -s ' + serial + ' wait-for-device remount'  
    mycmd = mycmd.replace('\n','')
    p = subprocess.Popen(mycmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout, stderr

def reboot(serial):   
    mycmd = 'adb -s ' + serial+ ' reboot'  
    mycmd = mycmd.replace('\n','')
    p = subprocess.call(mycmd,shell=True)

def get_file(cmd,serial):
    cmd = cmd.replace('\n','')
    cmd = cmd.replace('\r','')
    p = subprocess.call(cmd, shell=True)
