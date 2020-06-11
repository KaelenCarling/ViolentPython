from ViPyPrograms.CookieMonster import FirefoxScrape

fireTest = FirefoxScrape.FirefoxScraper('~/.mozilla/firefox/z6p7xev5.default-release/'.strip(), '')


print(fireTest.returnPwdDic())
