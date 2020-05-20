import zipfile
zFile = zipfile.ZipFile('C:\\Users\\Kaelen\\PycharmProjects\\ViPy\\ViPy Programs\\resources\\Evil.zip')
passFile = open('rockyou.txt')

try:
    #zFile.extractall(pwd=b"crackmes.one")
    zFile.extractall(pwd=b"password")
except Exception as e:
    print(e)