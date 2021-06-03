import sys
import traceback

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from . import program


def execute(url, file_name, reverse_chronological, headless, scroll_pause_time, user_driver, cookie_consent):



    def process_url():
        channel_info = url.split('youtube.com/')[1]
        channel_type = channel_info.split('/')[0]
        channel = channel_info.split('/')[1]
        base_url = 'https://www.youtube.com'
        videos = 'videos'
        return f'{base_url}/{channel_type}/{channel}/{videos}'

    def open_user_driver():
        nonlocal user_driver
        supported_drivers = {
            'firefox': configure_firefoxdriver,
            'opera':   configure_operadriver,
            'chrome':  configure_chromedriver,
            'brave':   configure_bravedriver,
        }
        return supported_drivers[user_driver]()

    def configure_firefoxdriver():
        options = selenium.webdriver.firefox.options.Options()
        if headless is True:
            options.headless = True
        return webdriver.Firefox(options=options)

    def configure_operadriver():
        options = webdriver.ChromeOptions()
        if headless is True:
            options.add_argument('headless')
        return webdriver.Opera(options=options)


    def configure_chromedriver():
        options = webdriver.ChromeOptions()
        if headless is True:
            options.add_argument('headless')
        return webdriver.Chrome(chrome_options=options)

    def configure_bravedriver():
        options = webdriver.ChromeOptions()
        options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
        executable_path = '/usr/local/bin/bravedriver'
        return webdriver.Chrome(options=options, executable_path=executable_path)



    def run_scraper():
        with driver:
            driver.get(url)
            driver.set_window_size(780, 800)
            driver.set_window_position(0, 0)
            manage_cookie_consent_form()
            wait = selenium.webdriver.support.ui.WebDriverWait(driver, 9)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//yt-formatted-string[@class="style-scope ytd-channel-name"]')))

            file_name = determine_file_name()
            results = program.determine_action(
                url, driver, scroll_pause_time, reverse_chronological, file_name)
        return results

    def manage_cookie_consent_form():
        if 'consent.youtube.com' in driver.current_url:
            if cookie_consent is False:
                wait = selenium.webdriver.support.ui.WebDriverWait(driver, 9)
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//a[@aria-label="Customize"]')))
                driver.find_element_by_xpath(
                    '//a[@aria-label="Customize"]').click()
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//button[@aria-label="Turn off Ad personalization"]')))
                driver.find_element_by_xpath(
                    '//button[@aria-label="Turn off Search customization"]').click()
                driver.find_element_by_xpath(
                    '//button[@aria-label="Turn off YouTube History"]').click()
                driver.find_element_by_xpath(
                    '//button[@aria-label="Turn off Ad personalization"]').click()
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//button[@aria-label="Ad personalization is off"]')))
                driver.find_elements_by_xpath('//button')[-1].click()
            elif cookie_consent is True:
                driver.find_element_by_xpath(
                    '//button[@aria-label="Agree to the use of cookies and other data for the purposes described"]').click()


    def determine_file_name():
        if file_name is not None:
            return file_name.strip('.csv').strip('.txt').strip('.md')
        else:
            channel_name = driver.find_element_by_xpath(
                '//yt-formatted-string[@class="style-scope ytd-channel-name"]').text.replace(' ', '')
            suffix = 'reverse_chronological_videos_list' if reverse_chronological else 'chronological_videos_list'
            return f'{channel_name}_{suffix}'


    url = process_url()
    driver = open_user_driver()
    return run_scraper()
