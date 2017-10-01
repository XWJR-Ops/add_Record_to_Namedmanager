#Auther: xwjr.com

from selenium import webdriver
import time


class Namedmanager(object):

    def __init__(self, namedmanager_username, namedmanager_password, namedmanager_url, hostname, ip):

        self.driver = webdriver.PhantomJS("/usr/local/phantomjs-2.1.1-linux-x86_64/bin/phantomjs", service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
        #self.driver = webdriver.Chrome()
        self.namedmanager_url = namedmanager_url
        self.namedmanager_username = namedmanager_username
        self.namedmanager_password = namedmanager_password
        self.hostname = hostname
        self.ip = ip

    def add_Record(self):
        driver = self.driver
        driver.maximize_window()
        driver.set_window_size(1120, 900)
        driver.set_page_load_timeout(30)
        driver.get(self.namedmanager_url)
        time.sleep(2)
        try:
            driver.find_element_by_xpath("//input[@id='username_namedmanager']").send_keys(self.namedmanager_username)
            driver.find_element_by_xpath("//input[@name='password_namedmanager']").send_keys(self.namedmanager_password)

            driver.find_element_by_name("submit").click()

            driver.set_page_load_timeout(30)
            time.sleep(3)
            driver.find_element_by_xpath("//a[@href='index.php?page=domains/domains.php']").click()
            driver.find_element_by_xpath("//a[@href='index.php?page=domains/records.php&id=4']").click()
            time.sleep(3)

            driver.find_element_by_xpath("//input[@value='Record name, eg www']").send_keys(self.hostname)
            driver.find_element_by_xpath("//input[@value='Target IP, eg 192.168.0.1']").send_keys(self.ip)

            time.sleep(2)
            driver.find_element_by_name("submit").click()
        except Exception, e:
            print Exception, ":", e

if __name__ == '__main__':

    namedmanager_url = "https://xxx.xxx.cn//namedmanager/"
    namedmanager_username = "setup"
    namedmanager_password = "123456"
    hostname = "mars"
    ip = "114.114.114.114"
    N = Namedmanager(namedmanager_username, namedmanager_password, namedmanager_url, hostname, ip)
    N.add_Record()
