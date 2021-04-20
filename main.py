import webbrowser

def logo():
    print("      _          _            __  __   _______ ")
    print("     | |        (_)          |  \/  | |__   __|")
    print("     | |  ___    _    _ __   | \  / |    | |")
    print(" _   | | / _ \  | |  | '_ \  | |\/| |    | |")
    print("| |__| | |(_)|  | |  | | | | | |  | |    | |")
    print(" \____/  \___/  |_|  |_| |_| |_|  |_|    |_|")
    print("\n")
    print("Version 0.2 - Developed by Schema")

logo()

Bool = True

while (Bool == True):
    code = str(input("Write the class code: "))
    features = len(code)
    if (features == 12):
        webbrowser.open("https://meet.google.com/"+code+"")
        print("\nI just opened your browser!\n")
        _continue = str(input("Do you want to enter another code?: (y/n)"))
        if (_continue == "y"):
            Bool = True
        else:
            Bool = False 
    else:
        print("\nInvalid code meet")
        Bool = True
