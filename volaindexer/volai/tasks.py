from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from .models import Rooms
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
import time
import random



@task(name="newupdate")
def newupdate():
    PROXY = 'http://lum-customer-hl_90da9698-zone-static:t97txa5c5hgb@zproxy.lum-superproxy.io:22225'
    proxy = Proxy()
    proxy.http_proxy = PROXY
    proxy.ftp_proxy = PROXY
    proxy.sslProxy = PROXY
    proxy.no_proxy = "localhost" #etc... ;)
    proxy.proxy_type = ProxyType.MANUAL
    proxy.socksUsername = 'lum-customer-hl_90da9698-zone-static'
    proxy.socksPassword = "t97txa5c5hgb"
    capabilities = webdriver.DesiredCapabilities.CHROME

    proxy.add_to_capabilities(capabilities)

    dblist = Rooms.objects.all()
    chrome_path = r"/usr/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--incognito")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--proxy-server=http://%s' % PROXY)
    driver = webdriver.Chrome(chrome_path, chrome_options=options)
    driver.implicitly_wait(3)
    for elemento in dblist:
        driver.get(elemento.room_adress)
        print(elemento.room_adress)
        name = driver.find_element_by_id('room_name').text
        elemento.room_name = name
        try:
            passw = driver.find_elements_by_name('password')
            passw[0].send_keys(elemento.room_pass)
            botao = driver.find_elements_by_class_name("button")
            botao[1].click()
            time.sleep(3)
            passw = driver.find_elements_by_name('password')
            print(name)
            print(passw)
            if len(passw) > 0:
                elemento.delete()
            else:
                time.sleep(5)
                try:
                    quant= driver.find_element_by_class_name("chat_text").find_element_by_tag_name('strong')
                    elemento.room_viewers = quant.text
                except:
                    elemento.room_viewers = 0
                elemento.save()
        except:
            try:
                quant= driver.find_element_by_class_name("chat_text").find_element_by_tag_name('strong')
                elemento.room_viewers = quant.text
            except:
                elemento.room_viewers = 0
            elemento.save()
            pass



        time.sleep(3)
    driver.quit()

@task(name="checking")
def checking():
    dblist = Rooms.objects.all()
    chrome_path = r"/usr/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--incognito")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_path, chrome_options=options)
    driver.implicitly_wait(3)

    driver.get(dblist[0].room_adress)

    print(driver.page_source)
     #endereco = Rooms.objects.select_related('room_adress').all()
     #senha = Rooms.objects.select_related('room_pass').all()
     #visu = Rooms.objects.select_related('room_viewers').all()
@task(name="spam")
def spam():
    dblist = Rooms.objects.all()
    for i in array:
        PROXY = i
        try:
            for salas in dblist:

                chrome_path = r"/usr/bin/chromedriver"
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                options.add_argument('--no-sandbox')
                options.add_argument("--incognito")
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument('--proxy-server=http://%s' % PROXY)
                driver = webdriver.Chrome(chrome_path, chrome_options=options)
                driver.implicitly_wait(3)

                driver.get(salas.room_adress)
                texto = driver.find_elements_by_id('chat_input')
                texto[0].send_keys("Join volaindexer.org for new rooms")
                texto[0].send_keys(Keys.ENTER)

                print(driver.page_source)
        except Exception as e:
            print(e)
            pass
        time.sleep(600)
