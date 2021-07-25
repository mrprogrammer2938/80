#!/usr/bin/python3
# This Programm Write by Mr.nope
# 80 v1.0
import os, time, sys, platform, subprocess
try:
   from colorama import Fore,init
   init()
except ImportError:
    os.system("pip3 install colorama")
try:
   from pyfiglet import Figlet
except ImportError:
    os.system("pip install pyfiglet")
    from pyfiglet import Figlet
system  = platform.uname()[0]
End = '\033[0m'
run_Err = "\nThis Programm Run on Linux, MacOS, Windows!\n"
opt = Fore.GREEN + "\n80 ~# " + End
banner = Fore.GREEN + """
 █████   ██████ 
██   ██ ██  ████ 
 █████  ██ ██ ██ 
██   ██ ████  ██ 
 █████   ██████  
                 """ + End
def cls():
    if system == 'Linux':
      os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print(run_Err)
        sys.exit()
def title():
    if system == 'Linux':
      os.system("printf '\033]2;80\a'")
    elif system == 'Windows':
        os.system("title 80")
    else:
         print(run_Err)
         sys.exit()
def main():
    title()
    cls()
    print(banner)
    list()
def list():
    print("\n{1}.Black-Tool")
    print("{2}.Black-Tool-Termux")
    print("{3}.Black-Tool-Windows")
    print("{4}.ServerScan")
    print("{5}.K-Tool")
    print("{6}.Phone-Info")
    print("{7}.Hack-Framework")
    print("{8}.My-IP")
    print("{9}.Translate")
    print("{10}.Tools(20/40/60)")
    print("{99}.Exit")
    choose = input(opt)
    if choose == '1':
      cls()
      print("\nInstalling...")
      run_1 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Black-Tool")
      try1()
    elif choose == '2':
        cls()
        print("\nInstalling...")
        run_2 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Black-Tool-Termux")
        try1()
    elif choose == '3':
        cls()
        print("\nInstalling...")
        run_3 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Black-Tool-Windows")
        try1()
    elif choose == '4':
        cls()
        print("\nInstalling...")
        run_4 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/serverscan")
        try1()
    elif choose == '5':
        cls()
        print("\nInstalling...")
        run_5 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/K-Tool")
        try1()
    elif choose  == '6':
        cls()
        run_6 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Phone-Info")
        try1()
    elif choose == '7':
        cls()
        run_7 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Hack-Framework")
        try1()
    elif choose == '8':
        cls()
        print("\nInstalling...")
        run_8 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/My-IP")
        try1()
    elif choose == '9':
        cls()
        print("\nInstalling...")
        run_9 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Translate")
        try1()
    elif choose == '10':
        mr_Tool()
    elif choose == '99':
        ext()
    else:
        main()
def ext():
    cls()
    print("Exiting...")
    sys.exit()
s = Figlet(font="slant")
banner_2 = s.renderText('80')
def mr_Tool():
    cls()
    print(banner_2)
    print("\n{1}.20")
    print("{2}.40")
    print("{3}.60")
    print("{99}.Main Menu")
    choose2 = input(opt)
    if choose2 == '1':
      cls()
      print("\nInstalling...")
      run_10 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/20")
      try1()
    elif choose2 == '2':
        cls()
        print("\nInstalling...")
        run_11 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/40")
        try1()
    elif choose2 == '3':
        cls()
        print("\nInstalling...")
        run_12 = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/60")
        try1()
    elif choose2 == '99':
        main()
    else:
        mr_Tool()
if __name__ == '__main__':
  try:
     try:
        main()
     except EOFError:
         print("\nCtrl + D")
         print("\nExiting...")
         sys.exit()
  except KeyboardInterrupt:
      print("\nCtrl + C")
      print("\nExiting...")
      sys.exit()
