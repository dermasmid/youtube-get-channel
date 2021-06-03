import datetime
from . import scroller


def determine_action(url, driver, scroll_pause_time, reverse_chronological, file_name):
    videos_list = scroller.scroll_to_bottom(
        url, driver, scroll_pause_time)
    if len(videos_list) == 0:
        return
  
    return get_in_list(videos_list, reverse_chronological)


def get_in_list(list_of_videos, reverse_chronological):
    results = []
    for selenium_element in list_of_videos if reverse_chronological else list_of_videos[::-1]:
        data = {
            'video_title': selenium_element.get_attribute("title"),
            'video_url': selenium_element.get_attribute("href"),
        }
        results.append(data)
    return results

def now():
    return datetime.datetime.now().isoformat().replace(':', '-').replace('.', '_')
