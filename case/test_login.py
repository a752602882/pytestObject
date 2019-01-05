import  pytest
import  time

from  page.loginpage import  _login ,_login_result

class TestLogin():


    # @pytest.fixture(scope='function',autouse=True)
    # def startpage(self,driver,host):
    #      print('--function --start---!')
    #      driver.get(host+'/user/newlogin')
    #      driver.delete_all_cookies()
    #      driver.refresh()


    def test_login_pass(self,driver,host,login):
        #_login(driver,host)
        results = _login_result(driver,"LV_V")
        print('登录结果：%s'%results)
        assert  results


    def test_login_fail(self,driver,host,login):
        #_login(driver,host)
        results = _login_result(driver,"LV_V")
        print('登录结果：%s'%results)
        assert  results

if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])