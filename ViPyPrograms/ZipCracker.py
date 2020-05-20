import zipfile
import optparse
from threading import Thread


# tries to extract it using the password provided. If successful it prints the password. otherwise does nothing
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password.encode())
        print('Success! password is ' + password)
    except:
        pass


def main():
    # tells the format used fro parameter opsions
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")

    # adds the zip file directory option
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')

    # adds the diction file directory option
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')

    # parses in passed in args and makes sure there is 2 arguements. if not exits and prints correct usage
    (options, args) = parser.parse_args()
    if (options.zname is None) | (options.dname is None):
        print(parser.usage)
        exit(0)
    # if there is correct parameters passed in it starts trying passwords from the dictionary file on the zip file
    else:
        # opens the zip file using the directory given
        zFile = zipfile.ZipFile(options.zname)

        # opens the password file using the directory given
        passFile = open(options.dname)

        for line in passFile.readlines():
            # strips formatting from password
            password = line.strip('\n')

            # starts a thread with the extract file function
            thr = Thread(target=extractFile, args=(zFile, password))
            thr.start()


if __name__ == '__main__':
    main()
