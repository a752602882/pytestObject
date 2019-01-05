#运行报告的范本
#pytest -s -q --alluredir report


import pytest
from selenium import webdriver
from page.loginpage import _login


_driver = None

def pytest_addoption(parser):
    #"添加命令行参数 --browser --host"
    parser.addoption(
        '--browser',action ='store',
        default = 'chrome',help = 'browser option firefox or chrome'

    )

    parser.addoption(
        '--host',action ='store',
        default = 'https://www.imooc.com',help = 'test host->http://bestebit.ngrok.36dr.net:9999'
    )

@pytest.fixture(scope="session")
def host(request):
    '''全局host参数'''
    return request.config.getoption('--host')

@pytest.fixture(scope="session")
def driver(request):
    '''定义全局driver参数'''
    name = request.config.getoption("--browser")
    global _driver
    if _driver is None:
        if name =='firefox':
            _driver = webdriver.Firefox()
        elif name =='chrome':
            _driver = webdriver.Chrome()
        else:
            _driver = webdriver.Chrome()

    print("正在启动浏览器 %s" % name)

    def end():
        print("全部用例执行完毕后关闭浏览器： teardown quit  driver")
        _driver.quit()
    request.addfinalizer(end)
    return _driver

@pytest.fixture(scope="function",autouse=True)
def login(request,driver,host):
    '''登录功能'''
    _login(driver,host)
    #注册方法实际上就是结束的时候执行的方法
    def clearSession():
        print("————清除缓存————")
        driver.delete_all_cookies()
        driver.refresh()
    request.addfinalizer(clearSession)


'''
def _capture_screenshot(file_name):
    return  _driver.get_screenshot_as_base64()



@pytest.mark.hookwarpper
def pytest_runtest_makereprot(item):
   
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode('utf-8').decode('unicode-escape')


'''