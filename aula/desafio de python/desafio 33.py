from datetime import date
from colorama import init, Fore, Back, Style
int = int(input(Fore.BLACK + "que ano quer analizar> "))
if (int == 0):
    int = date.today().year
    if int % 4 == 0:
        print (Fore.GREEN + f"o ano é bisseeto {int}")
else:
    print (Fore.RED + f"o ano não é bissesto {int}")