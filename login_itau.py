import pyautogui
import time


class Login_Itau:
    def __init__(self):
        pass

    def login_itau(self, cartao, password, driver):
        try:
            driver.get("https://col.itaucardcorporate.com.br/col/login.jsp")
            time.sleep(6)
            pyautogui.typewrite(str(cartao), interval=0)
            pyautogui.press("tab")
            time.sleep(6)
            pyautogui.typewrite(password, interval=0)
            pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(3)
            return True
        except Exception as e:
            print("There was an error in the login module." + str(e))
            return False