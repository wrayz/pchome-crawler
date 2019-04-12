from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumPchome:
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(30)

    def get_page(self, keyword):
        driver = self.driver
        driver.get("https://www.pcstore.com.tw/")
        driver.find_element_by_id("id_search_word").click()
        driver.find_element_by_id("id_search_word").clear()
        driver.find_element_by_id(
            "id_search_word").send_keys(u"{}".format(keyword))
        driver.find_element_by_id("id_search_word").send_keys(Keys.ENTER)
        # driver.execute_script("s_k_search('/adm/psearch.htm');")
        # 上面兩行是一樣的結果
        return driver.page_source
