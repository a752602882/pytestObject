from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElement(self, locator):
        if not isinstance(locator, tuple):
            pass
        else:
            print('元素的定位方式%s---->%s', locator[0], locator[1])
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        if ele is None:
            print('定位元素%s---->%s---->未能定位到元素', locator[0], locator[1])
        return ele

    def findElements(self, locator):
        if not isinstance(locator, tuple):
            pass
        else:
            try:
                print('元素的定位方式%s---->%s', locator[0], locator[1])
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
                return eles
            except:
                return []

    def sendKeys(self, locator, _text=''):
        ele = self.findElement(locator)
        ele.send_keys(_text)

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSeleced(self, locator):
        ele = self.findElement(locator)
        return ele.is_selected()

    def isElemetExist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_title(self, _title=''):
        try:
            result = WebDriverWait(self.driver, self.timout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contain(self, _title=''):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text=''):
        if not isinstance(locator, tuple):
            print('locator 参数类型错误')
        try:
            # ele=self.findElement(locator)
            # if ele.text is None and ele.text in _text:
            #     return True
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(locator, _text))
            print('element %s包含字符 %s:', locator[1],_text)
            return result
        except:
            return False

    def is_value_in_element(self, locator, _value=''):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须穿元祖类')
        try:

            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def is_alert(self, timeout=3):
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        return self.driver.title

    def get_text(self, locator):
        try:
            t = self.findElement(locator).text
            return t
        except:
            print('获得text失败，返回‘’')
            return ''

    def get_attribute(self, locator, name):
        try:
            element = self.findElement(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败，返回''" % name)
            return ''

    def js_focus_element(self, locator):
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].srcollIntoView();", target)

    def js_scroll_top(self):
        js = 'window.scrollTo(0,0)'
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        js = 'window.scrollTo(%s,document.body.scrollHeight)' % x
        self.driver.execute_script(js)

    def move(self, locator):
        ele = self.findElement(locator)
        if ele is not None:
            print("开始移动鼠标")
            webdriver.ActionChains(self.driver).move_to_element(ele).perform()
        else:
            print('未找到定位元素')

    def max(self):
        self.driver.maximize_window()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    web = Base(driver)
    driver.get("https://www.baidu.com/")
    locator1 = ('id', 'su')
    t = web.get_attribute(locator1, 'value')
    print(t)
