import os
import sys
import allure

from jproperties import Properties
from allure_commons.types import AttachmentType
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from core.logger_listener import LoggedListener

PROJECT_ROOT = os.path.dirname(__file__)

CHROME_DRIVER_DICT = {'linux': os.path.join(PROJECT_ROOT, 'webdrivers/chrome/chromedriver_lin'),
                      'darwin': os.path.join(PROJECT_ROOT, 'webdrivers/chrome/chromedriver_mac'),
                      'win32': os.path.join(PROJECT_ROOT, 'webdrivers/chrome/chromedriver_win.exe'),
                      'win64': os.path.join(PROJECT_ROOT, 'webdrivers/chrome/chromedriver_win.exe')}

OPERA_DRIVER_DICT = {'linux': os.path.join(PROJECT_ROOT, 'webdrivers/opera/operadriver_lin'),
                      'darwin': os.path.join(PROJECT_ROOT, 'webdrivers/opera/operadriver_mac'),
                      'win32': os.path.join(PROJECT_ROOT, 'webdrivers/opera/operadriver_win.exe'),
                      'win64': os.path.join(PROJECT_ROOT, 'webdrivers/opera/operadriver_win.exe')}

YANDEX_DRIVER_DICT = {'linux': os.path.join(PROJECT_ROOT, 'webdrivers/yandex/yandexdriver_lin'),
                      'darwin': os.path.join(PROJECT_ROOT, 'webdrivers/yandex/yandexdriver_mac'),
                      'win32': os.path.join(PROJECT_ROOT, 'webdrivers/yandex/yandexdriver_win.exe'),
                      'win64': os.path.join(PROJECT_ROOT, 'webdrivers/yandex/yandexdriver_win.exe')}

@fixture
def start_browser():
    configs = Properties()

    configs.load(open(os.path.join(PROJECT_ROOT, 'app.properties'), 'rb'))

    browser_name = configs.get("browser").data

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('lang=ru')

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_DICT[sys.platform], options=options)
    elif browser_name == "opera":
        driver = webdriver.Opera(executable_path=OPERA_DRIVER_DICT[sys.platform], options=options)
        driver.maximize_window()
    elif browser_name == "yandex":
        driver = webdriver.Opera(executable_path=YANDEX_DRIVER_DICT[sys.platform], options=options)
        driver.maximize_window()
    else:
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_DICT[sys.platform], options=options)

    yield driver

    if sys.exc_info():
        allure.attach(body=driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
    driver.quit()