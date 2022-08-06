import login_itau
import download_ultima_fatura
import download_proxima_fatura
from selenium import webdriver

if __name__ == '__main__':

    chromeOptions = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path='chromedriver.exe')

    try:
        obj_login_itau = login_itau.Login_Itau()
        obj_login_itau.login_itau(4076000251661592, 'marc2020', driver)

        obj_download_ultima_fatura = download_ultima_fatura.Download_Ultima_Fatura()
        obj_download_ultima_fatura.download_ultima_fatura(r"C:\Users\BlueShift\Downloads",
                                                          r'C:\Users\BlueShift\Desktop\Paytrack\Mensal', driver)

        obj_download_proxima_fatura = download_proxima_fatura.Download_Proxima_Fatura()
        obj_download_proxima_fatura.download_proxima_fatura(r"C:\Users\BlueShift\Downloads",
                                                            r'C:\Users\BlueShift\Desktop\Paytrack\Mensal', driver)
    except FileExistsError:
        pass
