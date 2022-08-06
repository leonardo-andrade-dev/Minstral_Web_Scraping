import pyautogui
from selenium.webdriver.common.by import By
import time
import os


class Download_Ultima_Fatura:
    def __init__(self):
        pass

    def download_ultima_fatura(self, path, end_path, driver):
        button_download = driver.find_element(By.XPATH,
                                              '/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[4]/div[2]/font[1]/b'
                                              '/map/area[4]')
        button_download.click()
        time.sleep(2)
        pyautogui.press("tab")
        time.sleep(2)
        pyautogui.press("tab")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("enter")

        lst_file = os.listdir(path)
        lst_end_file = os.listdir(end_path)

        if 'Fatura_Mensal.csv' in lst_end_file:
            os.remove(end_path)

        for file in lst_file:
            if "fatura.csv" in file:
                os.rename(r"C:\Users\BlueShift\Downloads\fatura.csv",
                          r"C:\Users\BlueShift\Desktop\Paytrack\Mensal\Fatura_Mensal.csv")