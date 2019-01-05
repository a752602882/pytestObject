from selenium import webdriver
from common.base import Base
import  time

loc1 = ('name','email')
loc2 = ('name','password')
loc3 = ('className','moco-btn')

loc_move=('className','user-card-box')
loc_re =('className','name')



def _login(driver,host,user='18780113305',psw='5423110.'):
    '''
    登录函数
    '''
    imooc = Base(driver)
    driver.get(host+'/user/newlogin')
    imooc.max()
    imooc.sendKeys(loc1,user)
    imooc.sendKeys(loc2,psw)
    imooc.click(loc3)
    time.sleep(2)


def _login_result(driver,_text):
    '''
    登录成功后，获取当前页面的用户名，判断用户名
    '''
    imooc = Base(driver)
    imooc.move(loc_move)
    time.sleep(2)
    r = imooc.is_text_in_element(loc_re,_text)
    return r

