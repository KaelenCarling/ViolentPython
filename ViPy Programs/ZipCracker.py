import zipfile


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password.encode())
        return password
    except Exception:
        return


def main():
    zFile = zipfile.ZipFile('C:\\Users\\Kaelen\\PycharmProjects\\ViPy\\ViPy Programs\\resources\\Evil.zip')
    passFile = open('rockyou.txt')

    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zFile, password)
        if guess:
            print('Success! password is ' + password)


if __name__ == '__main__':
    main()
