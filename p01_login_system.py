correct_account1="admin"
correct_account2="zhangsan"
correct_account3="taoge"
correct_password1="666888"
correct_password2="123456"
correct_password3="888666"
while True:
    account = input("请输入你的用户名")
    password = input("请输入你的账号密码")
    if account=="" or password=="":
        print("用户名或密码不能为空，请重新输入")
        continue
    if account == correct_account1 and password == correct_password1:
        print("登陆成功，进入b站首页~")
        break
    elif account == correct_account2 and password == correct_password2:
        print("登陆成功，进入b站首页~")
        break
    elif account == correct_account3 and password == correct_password3:
        print("登陆成功，进入b站首页~")
        break
    else:
        print("用户名或密码错误，请重新输入")


