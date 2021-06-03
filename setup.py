from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='get_channel',
    version='1.0.0',
    description='YouTube bot to make a YouTube videos list (including all video titles and URLs uploaded by a channel) with end-to-end web scraping - no API tokens required. 🌟 Star this repo if you found it useful! 🌟',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Shail-Shouryya/yt-videos-list/tree/main/python',
    author='Shail-Shouryya',
    author_email='yt.videos.list@gmail.com',
    license='Apache License 2.0',
    keywords='YouTube videos URL scraping automation Selenium csv txt macos windows linux',
    packages=find_packages(),
    python_requires='>=3.6.*, <4',
    install_requires=['selenium>=3.141.0, <4'],
)
