import subprocess,multiprocessing,time

def log(serial,suitename,srcfile):
    cmd = 'mkdir -p ../Testcase/result/' + suitename
    p = subprocess.call(cmd, shell=True)
    time.sleep(1)
    cmd = 'adb -s ' + serial + ' shell logcat -c '
    p = subprocess.call(cmd, shell=True)
    cmd = 'adb -s ' + serial+ ' shell logcat -v time > '+ ' ../Testcase/result/' + suitename + '/' + srcfile + '.log'
    cmd = cmd.replace('\n','')
    print cmd
    p = subprocess.call(cmd, shell=True)

def start(serial,suitename,srcfile):
    p = multiprocessing.Process(target=log,args=(serial,suitename,srcfile,))
    p.start()
    #p.join()
def end(serial,suitename,srcfile):
    # kill logcat on device
    cmd = 'adb -s '+ serial + ' wait-for-device root && adb -s '+ serial + ' wait-for-device remount && adb -s ' + serial + ' wait-for-device '
    print cmd 
    p = subprocess.call(cmd, shell=True)

    cmd = 'adb -s '+ serial + ' shell ps |grep logcat'
    p = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()
    process_list = stdout.split('\r\n')
    for item in process_list:
        if item:
            pid = item.split()[1]
            print pid
            cmd = 'adb -s '+ serial + ' shell kill ' + pid
            print cmd
            p = subprocess.call(cmd,shell=True)
    # kill defunct python process on linux
    cmd = 'ps -e |grep defunct'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()
    defunct = stdout.split()
    print defunct
    cmd = 'kill ' + defunct[0]
    print cmd
    p = subprocess.call(cmd, shell=True)  
    

    
