import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+"Im blue "+ Fore.YELLOW+ Back.BLUE+"now I am YELLOW")
print(Back.CYAN+"What color is this ? silver or cyan??")
print(Fore.RED + Back.GREEN+ "this is a familiar one")
