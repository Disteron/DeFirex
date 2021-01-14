
from core.driver_action import DriverAction

WEB_NAME = 'https://defirex.org/'

DICT_XPATH = {
    'Задать вопрос': '//button[text()="Задать вопрос"]',
    'WhatsApp': '//div[text()="WhatsApp"]',
    'Имя пользователя': '//input[@placeholder="Ваш номер телефона в WhatsApp"]',
    'Тема сообщения': '//input[@placeholder="Тема сообщения"]',
    'Сообщение': '//textarea[@placeholder="Сообщение"]',
    'Отправить': '//button[text()="Отправить"]',
    'Написать в поддержку': '//p[text()="Сообщение отправлено в поддержку. В ближайшее время с Вами свяжутся."]',
}


def get_xpath(name):
    return DICT_XPATH.get(name)


def test(start_browser):
    driver = start_browser
    driverObject = DriverAction(driver=driver, timeout=15)
    driverObject.go_to_web(WEB_NAME)
    driverObject.click_button(xpath=get_xpath("Задать вопрос"))
    driverObject.click_button(xpath=get_xpath("WhatsApp"))
    driverObject.fill_field(field_xpath=get_xpath("Имя пользователя"), value="+79991112233")
    driverObject.fill_field(field_xpath=get_xpath("Тема сообщения"), value="Тестовое сообщение")
    driverObject.fill_field(field_xpath=get_xpath("Сообщение"), value="Проведение тестирования формы")
    driverObject.click_button(xpath=get_xpath("Отправить"))
    driverObject.wait_field(xpath=get_xpath("Написать в поддержку"))