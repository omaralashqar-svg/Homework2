

userpass = (input())

userpass = userpass.replace('i', '!')
userpass = userpass.replace('a', '@')
userpass = userpass.replace('m', 'M')
userpass = userpass.replace('B', '8')
userpass = userpass.replace('o', '.')
appendstr = 'q*s'

finalstr = userpass + appendstr


print(finalstr)
