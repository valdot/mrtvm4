# -*- coding: utf-8 -*-
import requests, threading, os, sys, time
os.system("clear")
print ("""
               .----------.
              /            \   \033[32;1mAuthor : MR.TVM4 & EMP4TKOSONG4\033[37;1m
             /              \ \033[33;1m B L A C K _ C O D E R _ C R U S H \033[37;1m
             |,  .-.  .-.  ,| \033[31;1m ___  ___  ___  \033[32;1m_____  _  _    _         _   \033[37;1m
             | )(\033[31;1m##/  \##\033[37;1m)( |\033[31;1m | | ||   || | |\033[32;1m|   __||_|| |_ | |_  _ _ | |_ \033[37;1m
             |/     /\     \| \033[31;1m|_  || | ||_  |\033[32;1m|  |  || ||  _||   || | || . |\033[37;1m
       (@_   <__    ^^    __>   \033[31;1m|_||___|  |_|\033[32;1m|_____||_||_|  |_|_||___||___|\033[37;1m
  _     ) \___\__|\033[31;1mIIIIII\033[37;1m|__/____________________________________
 (_)\033[31;1m0000\033[37;1m{}<_____________________________________________________\033[31;1m>>\033[37;1m
        )_/     \ \033[31;1mIIIIII\033[37;1m /
       (@        --------
""")
print ("\033[1;31m[\033[33;1m+\033[31;1m]\033[1;33m=====================================================================\033[1;31m[\033[33;1m+\033[31;1m]")
print ("\033[1;31m[\033[33;1m+\033[31;1m] \033[1;33mExample \033[31;1m: \033[33;5m\033[32;1mgrab.github.io")
bcotan = raw_input("   \033[31;1m┌─[ Input Domain/IP ]-[ Black Coder Crush ]\n   \033[37;1m└─────▶ # \033[31;1m")
req = requests.get("https://api.hackertarget.com/reverseiplookup/?q=" + (bcotan))
tu = open("bcc.txt", "w")
tu.write(req.text)
tu.close
cok = open("bcc.txt", "r")
cad = open("bcc.txt", "r")
leno = cad.read().split()
print ("\033[33;5mTotal Web: \033[37;5m" + str(len(leno)))
hoho = len(leno)
time.sleep(0.5)
tai = "Tai Lu Mwuehehe"
print ("\033[32;5m[\033[33;5m+\033[32;5m]\033[37;5mWaiting For Get \033[31;5m404 \033[37;5mWeb....")
print 55*"\033[32;5m_"
def mulai(tek):
        global p
        p = 0
        while True:
          try:
            p +=1
            yah = cok.readline().strip()
            v = "http://" + (yah)
            try:
              cat = requests.get(v)
            except:
              continue
            if p > hoho:
                print ("\033[32;5m[!]Selesai")
                sys.exit()
            if cat.status_code ==404:
                print ("\033[34;5m" + yah + " \033[35;5m>> \033[31;5m404")
                continue
            else:
               continue
          except KeyboardInterrupt:
            print("\033[31;5m[!]Keluar")
            sys.exit()
threads = []
for x in tai:
    t = threading.Thread(target=mulai, args=(tai,))
    threads.append(t)
    t.start()
for t in threads:
    t.join
