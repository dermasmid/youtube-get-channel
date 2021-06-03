import time


def scroll_to_bottom(url, driver, scroll_pause_time):
    current_elements_count = None
    new_elements_count = count_videos_on_page(driver)

    def verify_scrolled_to_page_bottom():

        time.sleep(scroll_pause_time * 2)
        new_elements_count = count_videos_on_page(driver)
        return new_elements_count

    while new_elements_count != current_elements_count:
        current_elements_count = new_elements_count
        scroll_down(driver, scroll_pause_time)
        new_elements_count = count_videos_on_page(driver)
        if new_elements_count == current_elements_count:
            new_elements_count = verify_scrolled_to_page_bottom()

    return save_elements_to_list(driver)


def count_videos_on_page(driver):
    return driver.execute_script('return document.querySelectorAll("ytd-grid-video-renderer").length')




def scroll_down(driver, scroll_pause_time):
    driver.execute_script('window.scrollBy(0, 50000);')
    time.sleep(scroll_pause_time)


def save_elements_to_list(driver):
    elements = driver.find_elements_by_xpath('//*[@id="video-title"]')
    return elements
