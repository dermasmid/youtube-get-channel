'''
YouTube bot to make a YouTube videos list (including all video titles and
URLs uploaded by a channel) with end-to-end web scraping - no API tokens required.
🌟 Star this repo if you found it useful! 🌟
https://github.com/Shail-Shouryya/yt-videos-list
'''

from . import logic


__version__ = '0.5.8'
__author__ = 'Shail-Shouryya'
__email__ = 'yt.videos.list@gmail.com'
__development_status__ = '4 - Beta'
__intended_audience__ = 'Developers, Hobbyists'
__license__ = 'OSI Approved :: Apache License 2.0'
__ideal_python_version__ = 'Python 3.6+'
__source__ = 'https://github.com/Shail-Shouryya/yt-videos-list/tree/main/python'


class ListCreator:
    '''
    =====================================================
    | If you found this interesting or useful,          |
    | ** please consider STARRING this repo at **       |
    | https://github.com/Shail-Shouryya/yt-videos-list  |
    | so other people can more easily find and use this.|
    | Thank you!!                                       |
    =====================================================
    '''

    def __init__(self, reverse_chronological=True, headless=False, scroll_pause_time=0.8, driver=None, cookie_consent=False):
        self.reverse_chronological = reverse_chronological
        self.headless = headless
        self.scroll_pause_time = scroll_pause_time
        self.driver = None if driver is None else driver.lower()
        self.cookie_consent = cookie_consent


    def create_list_for(self, url=None, file_name=None):
        return logic.execute(url, file_name, self.reverse_chronological, self.headless, self.scroll_pause_time, self.driver, self.cookie_consent)

