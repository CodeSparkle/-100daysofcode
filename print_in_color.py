import colorama
from colorama import Fore, Back, Style


def main():
    colorama.init()

    print(Fore.RED)
    print("This is RED color!!!")
    print(Style.RESET_ALL)
    print("Now the colors have been reset\n")

    print("You can color even a single " + Fore.YELLOW + Back.WHITE + "word" + Style.RESET_ALL + " and than reset the colors")

    print(Fore.RED+Back.LIGHTGREEN_EX)
    print("Pay attention: Dark colors are not recommended, because it's hard to see them over the black color of the terminal.")

    print(Style.RESET_ALL)
    print( Fore.GREEN + "H" + Fore.YELLOW + "A" + Fore.CYAN + "V" + Fore.RED + "E" + Fore.BLUE + " F" + Fore.WHITE + "U" + Fore.LIGHTGREEN_EX + "N")


if __name__ == '__main__':
    main()
