import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])

    if ret == 0:
        print('Error Could not connect')
        return

    if 1 == ret:
        child.sendline('yes')

    ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])

    if ret == 0:
        print('Error could not connect')
        return

    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host = 'localhost'
    user = 'root'
    password = 'neon3643'