import subprocess
from common import color

def getfps(dfile):
    cmd = 'mediainfo '+ dfile + ' |grep "Frame rate" |tail -1'
    cmd = cmd.replace('\n','')
    p = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()
    print color.inred(stdout.replace('\n',''))

def getresolution(dfile):
    cmd = 'mediainfo ' + dfile + ' |grep "Width"'
    cmd = cmd.replace('\n','')
    p = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()
    print color.inred(stdout.replace('\n',''))

    cmd = 'mediainfo ' + dfile + ' |grep "Height"'
    cmd = cmd.replace('\n','')
    p = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()
    print color.inred(stdout.replace('\n',''))
def getformat(dfile):
    cmd = 'mediainfo ' + dfile + ' |grep "Format"'
    cmd = cmd.replace('\n','')
    p = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()
    print color.inred(stdout.replace('\n',''))
    
