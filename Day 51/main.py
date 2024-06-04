import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "YOUR_EMAIL_GOES_HERE"
TWITTER_PASSWORD = "YOUR_PASSWORD_GOES_HERE"
TWITTER_USERNAME = "YOUR_USERNAME_GOES_HERE"


option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-text")
        go_button.click()
        time.sleep(60)
        self.download_speed = self.driver.find_element(
            By.CLASS_NAME, value="download-speed"
        )
        print(f"down: {self.download_speed.text}")
        self.upload_speed = self.driver.find_element(
            By.CLASS_NAME, value="upload-speed"
        )
        print(f"up: {self.upload_speed.text}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(10)
        email_input = self.driver.find_element(
            By.XPATH,
            "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input",
        )
        email_input.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        try:
            pass_input = self.driver.find_element(
                By.XPATH,
                "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input",
            )
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = driver.find_element(
                By.XPATH,
                "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input",
            )
            username.send_keys(
                TWITTER_USERNAME
            )  # Your Username here in case Twitter asks for username before asking password
            username.send_keys(Keys.ENTER)
            time.sleep(5)
            pass_input = driver.find_element(
                By.XPATH,
                "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input",
            )
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)

        time.sleep(5)

        input = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        input.send_keys(
            f"My Current Internet Speed is {self.download_speed.text} Download and {self.upload_speed.text} Upload"
        )
        time.sleep(3)
        tweet = self.driver.find_element(
            By.XPATH,
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span",
        )
        tweet.click()
        time.sleep(5)
        print("Tweet Done")
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
time.sleep(5)
bot.tweet_at_provider()
