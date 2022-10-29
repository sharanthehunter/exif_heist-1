


class Colors(object):
    st = "\033[1;"  # Bold Style
    RED___ = f"{st}31;40m"
    GREEN_ = f"{st}32;40m"
    YELLOW = f"{st}33;40m"
    BLUE__ = f"{st}34;40m"
    PURPLE = f"{st}35;40m"
    CYAN__ = f"{st}36;40m"
    WHITE_ = f"{st}37;40m"



class Config(object):
    ENTER_IMAGE_PATH = f"\nEnter Image Path: "
    CHOOSE_FROM_MENU = "\n" \
                       f"\n 1.Get Exif Data" \
                       f"\n 2.Exit Script" \
                       "\n" \
                       f"\nChoose an option: "
    
    @staticmethod
    def banner():
        BANNER = f"""
'########:'##::::'##:'####:'########::::'##::::'##:'########:'####::'######::'########:
 ##.....::. ##::'##::. ##:: ##.....::::: ##:::: ##: ##.....::. ##::'##... ##:... ##..::
 ##::::::::. ##'##:::: ##:: ##:::::::::: ##:::: ##: ##:::::::: ##:: ##:::..::::: ##::::
 ######:::::. ###::::: ##:: ######:::::: #########: ######:::: ##::. ######::::: ##::::
 ##...:::::: ## ##:::: ##:: ##...::::::: ##.... ##: ##...::::: ##:::..... ##:::: ##::::
 ##:::::::: ##:. ##::: ##:: ##:::::::::: ##:::: ##: ##:::::::: ##::'##::: ##:::: ##::::
 ########: ##:::. ##:'####: ##:::::::::: ##:::: ##: ########:'####:. ######::::: ##::::
........::..:::::..::....::..:::::::::::..:::::..::........::....:::......::::::..:::::
                                       v1.0
   ____  , _                              ____                                  
  / __,\/|/ \  _,   _,   _,       |\     / __,\ () |)    _,   ,_   _,           
 | /  | ||__/ / |  / |  / | |  |  |/    | /  | |/\ |/\  / |  /  | / |  /|/|     
 | \_/|/ | \_/\/|_/\/|_/\/|/ \/|_/|_/   | \_/|//(_)|  |/\/|_/   |/\/|_/ | |_/   
  \____/                 (|              \____/                                                                        
                                
"""
        print("\033c")
        print(BANNER)

