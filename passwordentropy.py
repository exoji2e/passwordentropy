import subprocess
import time
import re

def main():
    print('Tell me your password :3')
    password = input()
    pf = open('passwords_john.txt','r')
    plist = pf.read()
    pf.close()
    appendedlist = open('appendedplist.txt','w')
    appendedlist.write(plist)
    appendedlist.write(password)
    appendedlist.close()
    
    #compresses both files
    bc1 = "tar -cvzf a.tar.gz passwords_john.txt"
    bc2 = "tar -cvzf b.tar.gz appendedplist.txt"
    subprocess.Popen(bc1.split(), stdout=subprocess.PIPE)
    subprocess.Popen(bc2.split(), stdout=subprocess.PIPE)

    #if we dont sleep sometimes the compression isn't finished, and filesizes are not correct.
    time.sleep(1)
    
    #counts size in bytes of both compressed files
    bc3 = "wc -c a.tar.gz"
    bc4 = "wc -c b.tar.gz"
    p1 = subprocess.Popen(bc3.split(), stdout=subprocess.PIPE)
    out1 = str(p1.communicate()[0])
    sizea = [int(s) for s in out1.split() if s.isdigit()][0]

    p2 = subprocess.Popen(bc4.split(), stdout=subprocess.PIPE)
    out2 = str(p2.communicate()[0])
    sizeb = [int(s) for s in out2.split() if s.isdigit()][0]    
    
    diff = sizeb - sizea
    print('your password has ' + str(diff) + ' bytes of entropy,')
    print('or ' + str(diff*8) + ' bits of entropy')

    #removes temporary files
    bcrm1 = "rm a.tar.gz"
    bcrm2 = "rm b.tar.gz"
    bcrm3 = "rm appendedplist.txt"
    subprocess.Popen(bcrm1.split(), stdout=subprocess.PIPE)
    subprocess.Popen(bcrm2.split(), stdout=subprocess.PIPE)
    subprocess.Popen(bcrm3.split(), stdout=subprocess.PIPE)
  
if __name__ == "__main__":
    main()