#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AppleMusic():
    def setupMethod(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.prefs = {"profile.managed_default_content_settings.images": 2}
        self.chrome_options.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}

    def setupVariables(self, countryID=None, inputFunction=None):
        self.variables = {
            "countryID": "gb",
            "inputFunction": (input, "Enter 2FA Code:\n")
        }

        if countryID is not None:
            self.variables["countryID"] = countryID

        if inputFunction is not None:
            self.variables["inputFunction"] = inputFunction

    def initiateWindow(self):
        url = "https://music.apple.com/{}/browse".format(self.variables["countryID"])
        self.driver.get(url)
        self.driver.set_window_size(945, 1020)

    def waitForWindow(self, timeout = 2):
        sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def login(self, appleID, password):
        sleep(0.5)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "#ember16 .web-navigation__auth-button").click()
        self.vars["win1689"] = self.waitForWindow(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win1689"])
        self.driver.switch_to.frame(0)
        sleep(0.5)
        self.driver.find_element(By.ID, "account_name_text_field").send_keys(appleID)
        self.driver.find_element(By.ID, "account_name_text_field").send_keys(Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.ID, "password_text_field").send_keys(password)
        self.driver.find_element(By.ID, "password_text_field").send_keys(Keys.ENTER)
        self.driver.switch_to.default_content()
        sleep(0.2)
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".button-primary").click()
        except NoSuchElementException:
            code = self.variables["inputFunction"][0](self.variables["inputFunction"][1])
            self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
            for x in range(0, 6):
                self.driver.find_element(By.ID, "char" + str(x)).send_keys(code[x])
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[3]/div/button[3]").click()
            sleep(4)
            self.driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div[2]/button").click()
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])

    def playSong(self, userInput):
        self.driver.find_element(By.CSS_SELECTOR, ".dt-search-box__input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".dt-search-box__input").send_keys(userInput)
        sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR, ".dt-search-box__input").send_keys(Keys.ENTER)
        sleep(5)
        self.driver.find_element_by_xpath("//*[@class='shelf-grid__list']/li/div/div/div/div/div/button").click()
        song = self.driver.find_element_by_xpath("//*[@class='shelf-grid__list']/li/div/div/div/ul/li/span/span").text
        artist = self.driver.find_element_by_xpath("//*[@class='shelf-grid__list']/li/div/div/div/ul/li[2]/a").text
        return "Playing {0} by {1}".format(song, artist)

    def resumeOrPause(self):
        self.driver.find_element_by_xpath("//*[@class='web-chrome-playback-controls__directionals']/div[2]/button[2]").click()

    def restartSong(self):
        self.driver.find_element_by_xpath("//*[@class='web-chrome-playback-controls__directionals']/div[2]/button[1]").click()

    def previousSong(self):
        self.driver.find_element_by_xpath("//*[@class='web-chrome-playback-controls__directionals']/div[2]/button[1]").click()
        self.driver.find_element_by_xpath("//*[@class='web-chrome-playback-controls__directionals']/div[2]/button[1]").click()

    def nextSong(self):
        self.driver.find_element_by_xpath("//*[@class='web-chrome-playback-controls__directionals']/div[2]/button[3]").click()

    def shuffle(self):
        self.driver.find_element_by_xpath("//*[@class='web-chrome-playback-controls__directionals']/div[1]").click()

if __name__ == "__main__":
    AM = AppleMusic()
    AM.setupMethod()
    AM.setupVariables()
    AM.initiateWindow()
    AM.login("Johnny_Applebottom@iCloud.com", "password123")
