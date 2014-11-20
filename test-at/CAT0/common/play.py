import subprocess,multiprocessing

def playfile(serial,fname):
    cmd = 'adb -s ' + serial + ' shell am start -a android.intent.action.VIEW -d file:///sdcard/' + fname + ' -t video/* '
    cmd = cmd.replace('\n','')
    cmd = cmd.replace('\r','')

    print cmd
    p=subprocess.call(cmd, shell=True)


def play(serial,fname):
    p = multiprocessing.Process(target=playfile, args=(serial,fname,))
    p.start()
