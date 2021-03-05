import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class DriverAction:

    def __init__(self, driver, timeout=None):
        self.driver = driver
        if timeout == None:
            self.timeout = 30
        else:
            self.timeout = timeout

    def wait(self, method, timeout=None):
        if(timeout==None):
            timeout = self.timeout

        end = time.time()+ timeout

        while(end > time.time()):
            try:
                method()
                return
            except Exception as e:
                print(e)
                pass
        raise TimeoutException(method)

    def _silent_scroll_to(self, element):
        try:
            action_chains = ActionChains(self.driver)
            action_chains.move_to_element(element).perform()
        except Exception:
            pass
        return element

    def click_button(self, xpath, timeout=None):
        def method():
            self._silent_scroll_to(self.driver.find_element_by_xpath(xpath=xpath)).click()

        self.wait(method=method, timeout=timeout)

    def fill_field(self, field_xpath, value, timeout=None):
        def input_in_field():
            field = self.driver.find_element_by_xpath(field_xpath)
            field.clear()
            field.send_keys(value)
            field.send_keys(Keys.TAB)

        self.wait(method=input_in_field, timeout=timeout)

    def go_to_web(self, web):
        self.driver.get(web)

    def wait_field(self, xpath):
        def wait_element():
            self.driver.find_element_by_xpath(xpath)

        self.wait(method=wait_element)

    def frame_switch(self, xpath):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath))

    def default_content(self):
        self.driver.switch_to.default_content()

    def ab(self, xpath):
        text = self.driver.find_element_by_xpath(xpath).text
        return text

