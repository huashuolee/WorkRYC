import sys,argparse
#from common.color import inred
from common import color
"""
def runTestcase(serial,srcfile):
    pushfile(serial,srcfile)
    time.sleep(3)
    a = srcfile.split("_")[2].split('x')
    width = a[0]
    height = a [1] 
    cmd = "am startservice -n com.test.vp8/com.test.vp8.Vp8IntentService -e in /sdcard/vp8_encode/" + srcfile + " -e out /sdcard/vp8_encode/result/" + srcfile + ".ivf" + "--ei w "+ width + " --ei h " + height + " --ei fps 30"
    return_value = execonDUT(cmd,serial)    
    print return_value[0]
"""
def runTestsuite(serial,suitename):
    exec("from test_module." + suitename + " import runTest") 
    print color.inred('Make sure you have backup the /etc/media_profiles.xml')    
    f=open('../Testcase/suite_profile/'+suitename,'r')
    case=f.readlines()
    for srcfile in case:
       # print color.inread("Run " + caseNo + '/'+ taotalNo)
        if srcfile.startswith('#'): 
            continue
        else:
            print color.inred( " Case Name: {0} {1}".format(suitename,srcfile))
            runTest(serial,srcfile,suitename)
            raw_input('press any key to continue: ') 
    f.close()
    sys.exit(0)
     
def parseArgs(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('DeviceID', help="specify the device ID")
    parser.add_argument('-p', dest='fileName',help="Only push the video clip to sdcard")
    parser.add_argument('-c', dest='caseName',help="run single test case")
    parser.add_argument('-s', dest='suitename',help="CaptureBasic CaptureH264 fron vp8_encode CaptureH263 CaptureM4v   screenRecording") 
    args = parser.parse_args()
    deviceid = args.DeviceID
    if args.fileName:
        pushfile(deviceid,args.fileName)
    if args.caseName:
        runTestcase(deviceid,args.caseName)
    
    if args.suitename:
        runTestsuite(deviceid,args.suitename)
    
if __name__ == '__main__':
    parseArgs(sys.argv[1:])
    
