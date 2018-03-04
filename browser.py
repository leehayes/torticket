from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.common.exceptions import WebDriverException

import time
import random

class Browser():
    def __init__(self, url, proxys, x, y, w, h, z):
        self.proxys = proxys
        self.url = url
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.z = z

    def run(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--proxy-server=" + random.choice(self.proxys))

            self.driver = webdriver.Chrome(chrome_options=chrome_options)

            self.driver.set_window_position(self.x, self.y)
            self.driver.set_window_size(self.w, self.h)

            self.driver.get(self.url)

            self.driver.execute_script("document.body.style.zoom='" + self.z + "%'")
        finally:
            while self.alive():
                time.sleep(1)
            self.run()

    def alive(self):
        try:
            self.driver.title
            return True
        except WebDriverException:
            return False


def worker(url, proxys, x, y, w, h, z):
    browser = Browser(url, proxys, x, y, w, h, z)
    browser.run()
    print("doing stuff :", str(x), str(y), str(w), str(h), z)

    return