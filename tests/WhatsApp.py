import time

from core.driver_action import DriverAction

# WEB_NAME = 'https://onlinetestpad.com/'
WEB_NAME = 'https://onlinetestpad.com/ru/test/44089-test-na-kompyuternuyu-gramotnost'

DICT_XPATH = {
    'Тесты': '//i[@class="icon-exam nav-link-icon"]',
    'Компьютерные программы': '//a[@href="/ru/tests/computerprograms"]',
    'Тест на грамотность': '//a[text()="Тест на компьютерную грамотность"]',
    'Фрейм1': '//iframe[@id="google_esf"]',
    'Фрейм2': '//iframe[@id="aswift_3"]',
    'Фрейм3': '//iframe[@name="ad_iframe"]',
    'Рекламазакрыть': '//div[@aria-label="Закрыть рекламу"]',
    'Пройти тест': '//a[@class="btn btn-primary btn-outline btn-go"]',
    'Далее1':'//input[@value="Далее"]',
    'Средство просмотра веб страницы': '//span[text()="средство просмотра веб-страниц"]',
    'От частоты процессора': '//span[text()="от частоты процессора"]',
    'Символ': '//span[text()="символ"]',
    'Прямое по оптоволоконному каналу': '//span[text()="прямое по оптоволоконному каналу"]',
    'Текстовый редактор': '//span[text()="текстовый редактор"]',
    'Программа или данные на диске': '//span[text()="Программа или данные на диске"]',
    'При скачивании музыки из интернета': '//span[text()="при скачивании музыки из интернета"]',
    '1 бит': '//span[text()="1 бит"]',
    'Видео, изображение и сообщения': '//span[text()="видео, изображение и сообщения"]',
    'Подключать монитор': '//span[text()="подключать монитор"]',
    'ip-адрес': '//span[text()="ip-адрес"]',
    'В двоичном коде': '//span[text()="в двоичном коде"]',
    'Отправьте его на email': '//a[text()="Отправьте его на email"]',
    'Поле для email': '//input[@placeholder="Введите свой email адрес"]',
    'Почта': 'is_o.o.rudenko@mpt.ru',
    'Отправить': '//i[@class="icon icon-aeroplane"]/..'
}


def get_xpath(name):
    return DICT_XPATH.get(name)


def test(start_browser):
    driver = start_browser
    driverObject = DriverAction(driver=driver, timeout=15)
    driverObject.go_to_web(WEB_NAME)
    # driverObject.click_button(xpath=get_xpath("Тесты"))
    # driverObject.click_button(xpath=get_xpath("Компьютерные программы"))
    # driverObject.click_button(xpath=get_xpath("Тест на грамотность"))
    # driverObject.click_button(xpath=get_xpath("Пройти тест"))
    # # time.sleep(3)
    # # driverObject.frame_switch(xpath=get_xpath("Фрейм1"))
    # # driverObject.default_content()
    # driverObject.frame_switch(xpath=get_xpath("Фрейм2"))
    # driverObject.frame_switch(xpath=get_xpath("Фрейм3"))
    # driverObject.default_content()
    # # time.sleep(3)
    # driverObject.click_button(xpath=get_xpath("Рекламазакрыть"))
    # driverObject.default_content()
    driverObject.click_button(xpath=get_xpath("Далее1"))

    for i in range(12):

        text = driverObject.ab(xpath='//span[@class="qtext"]')
        if text == "От чего зависит производительность компьютера?":
            driverObject.click_button(xpath=get_xpath("От частоты процессора"))
        elif text == 'Что такое "браузер"?':
            driverObject.click_button(xpath=get_xpath("Средство просмотра веб страницы"))
        elif text == 'Что такое "слэш"?':
            driverObject.click_button(xpath=get_xpath("Символ"))
        elif text == "Через какой тип подключения Internet работает быстрее?":
            driverObject.click_button(xpath=get_xpath("Прямое по оптоволоконному каналу"))
        elif text == "Microsoft Word это....":
            driverObject.click_button(xpath=get_xpath("Текстовый редактор"))
        elif text == "Что такое файл?":
            driverObject.click_button(xpath=get_xpath("Программа или данные на диске"))
        elif text == "Как может произойти заражение компьютерным вирусом?":
            driverObject.click_button(xpath=get_xpath("При скачивании музыки из интернета"))
        elif text == "Что является единицей измерения количества информации?":
            driverObject.click_button(xpath=get_xpath("1 бит"))
        elif text == "Что можно передавать по e-mail?":
            driverObject.click_button(xpath=get_xpath("Видео, изображение и сообщения"))
        elif text == "Какое действие не рекомендуется выполнять при включённом компьютере?":
            driverObject.click_button(xpath=get_xpath("Подключать монитор"))
        elif text == "Что обязательно имеет компьютер, подключённый к интернету?":
            driverObject.click_button(xpath=get_xpath("ip-адрес"))
        elif text == "В каком виде процессор обрабатывает информацию?":
            driverObject.click_button(xpath=get_xpath("В двоичном коде"))
        driverObject.click_button(xpath=get_xpath("Далее1"))

    driverObject.click_button(xpath=get_xpath("Отправьте его на email"))
    driverObject.fill_field(field_xpath=get_xpath("Поле для email"), value=("is_o.o.rudenko@mpt.ru"))
    driverObject.click_button(xpath=get_xpath("Отправить"))





