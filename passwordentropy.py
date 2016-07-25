import subprocess
import time

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
    bc1 = "tar -cvzf a.tar.gz passwords_john.txt"
    bc2 = "tar -cvzf b.tar.gz appendedplist.txt"
    process1 = subprocess.Popen(bc1.split(), stdout=subprocess.PIPE)
    #print(process1.communicate())
    process2 = subprocess.Popen(bc2.split(), stdout=subprocess.PIPE)
    bc3 = "wc -c a.tar.gz"
    bc4 = "wc -c b.tar.gz"
    time.sleep(1)
    process3 = subprocess.Popen(bc3.split(), stdout=subprocess.PIPE)
    x = int(str(process3.communicate()[0]).split(' ')[3],10)
    process4 = subprocess.Popen(bc4.split(), stdout=subprocess.PIPE)
    y = int(str(process4.communicate()[0]).split(' ')[3],10)
 
    time.sleep(1)
    
    
    bcrm1 = "rm a.tar.gz"
    bcrm2 = "rm b.tar.gz"
    bcrm3 = "rm appendedplist.txt"
    prm1 = subprocess.Popen(bcrm1.split(), stdout=subprocess.PIPE)
    prm2 = subprocess.Popen(bcrm2.split(), stdout=subprocess.PIPE)
    prm3 = subprocess.Popen(bcrm3.split(), stdout=subprocess.PIPE)
    
    diff = y - x
    print('your password has ' + str(diff*8) + ' bits of entropy')
    
    
if __name__ == "__main__":
    main()