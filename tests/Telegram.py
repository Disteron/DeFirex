from core.driver_action import DriverAction

WEB_NAME = 'https://defirex.org/'

DICT_XPATH = {
    'Задать вопрос': '//button[text()="Задать вопрос"]',
    'Имя пользователя': '//input[@placeholder="Ваше имя пользователя в Telegram"]',
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
    driverObject.fill_field(field_xpath=get_xpath("Имя пользователя"), value="testUser")
    driverObject.fill_field(field_xpath=get_xpath("Тема сообщения"), value="Тестовое сообщение")
    driverObject.fill_field(field_xpath=get_xpath("Сообщение"), value="Проведение тестирования формы")
    driverObject.click_button(xpath=get_xpath("Отправить"))
    driverObject.wait_field(xpath=get_xpath("Написать в поддержку"))