

import random
import colorama
from colorama import Fore,Back,Style
im
colorama.init(autoreset = True)
#class 


def dec1(fun):
  def exc():
    print(f"{Fore.GREEN} excuting know")
    fun()
    print(f"{Fore.GREEN} excuted")
  return exc



#class






title = f"{Fore.GREEN}W" + f"{Fore.RED}E" + f"{Fore.BLACK}L" + f"{Fore.BLUE}C" + f"{Fore.WHITE}O" + f"{Fore.GREEN}M" + f"{Fore.RED}E"

    

print(Style.BRIGHT + title)
print(Fore.GREEN + "option are ;")
print(f"{Fore.GREEN} 01 page 1 ")
print(f"{Fore.GREEN} 02 page 2 ")
print(f"{Fore.GREEN} 03 page 3 ")
print(f"{Fore.GREEN} 04 page 4 ")
print()
x = int(input(f"{Fore.BLUE}select the option "))


@dec1
def pro():
    if x== 1:
        print(f"{Fore.GREEN} option is ", x)
    if  x== 2:
        print(f"{Fore.GREEN} option is ", x)
    if  x== 3:
        print(f"{Fore.GREEN} option is ", x)
    if  x== 4:
        print(f"{Fore.GREEN} option is ", x)

    else:
    	print(f"{Fore.RED}{Style.BRIGHT}enter vaild option")
pro()  
