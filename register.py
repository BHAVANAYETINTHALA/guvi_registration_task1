import re
def register():
    global db
    db=open('details.txt','r')
    username = input("Create Username:(Username shouldn't start with special characters and numbers)")
    password = input("Create Password:(Password should contain atleast one lowercase chaarcter,one uppercase character,one special character and one digit)")
    lp = len(password)
    x=create_dictionaries()
    if username in x:
        print("Username exists and pls try to register using different username")
        register()
    elif re.search("[0-9]", username[0]) or re.search("[_@$]", username[0]):
        print("Username shouldn't start with special characters and numbers")
        register()
    elif ("@" not in username) or ("." not in username):
        print("Username should have @ followed by .")
        register()
    elif ("@" in username) and ("." in username):
        if (username.index(".") == (username.index("@")) + 1):
            print("In username there shouldn't be any . immediate next to @")
            register()

    if lp < 5 or lp > 16:
        print("Password length should be minimum 5 characters and maximum 16 characters")
        register()
    elif not re.search("[a-z]", password):
        print("Password must have one special character,one lowercase character,one uppercase character and one digit")
        print("Currently,Password doesn't contain atleast one lowercase character")
        register()
    elif not re.search("[A-Z]", password):
        print("Password must have one special character,one lowercase character,one uppercase character and one digit")
        print("Currently,Password doesn't contain atleast one uppercase letter")
        register()
    elif not re.search("[0-9]", password):
        print("Password must have one special character,one lowercase character,one uppercase character and one digit")
        print("Currently,Password doesn't contain atleast one digit")
        register()
    elif not re.search("[_@$]", password):
        print("Password must have one special character,one lowercase character,one uppercase character and one digit")
        print("Currently,Password doesn't contain atleast one special character(_@$)")
        register()
    else:
        db_w=open("details.txt","a+")
        db_w.write(username+","+password+"\n")
        print("Successfully created username and password")

def access():
    global db
    db=open('details.txt','r')
    username=input('Enter your username:')
    password=input('Enter password:')
    if not len(username or password)<1:
        x=create_dictionaries()
        try:
            if x[username]:
                if password == x[username]:
                   print("Login success")
                   print("Hi",username)
                else:
                   print("password is incorrect")
                   fg_p=input('Login or ForgotPassword:')
                   if fg_p == 'Login':
                       access()
                   elif fg_p == 'ForgotPassword':
                       forgot_password(username,x)
                   else:
                       print('Please select either Login or ForgotPassword')
                       fg_p = input('Login or ForgotPassword:')
                       if fg_p == 'ForgotPassword' :
                           forgot_password(username,x)
                       else:
                           print('Pls try to login with correct details')
                           access()
            else:
                print("username doesn't exist")
                access()
        except KeyError:
            print("username doesn't exist")
            ch=input('Register or Login:')
            if ch == 'Register':
                register()
            else:
                print('Pls try to login once again')
                access()

def forgot_password(username,x):
    d=open('details.txt','r')
    if x[username]:
        print("Your password:",x[username])
    else:
        print('You can register with new username and password')
        register()


def home( ):
    option=input("Login or Signup:")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter either Login or Signup")

def create_dictionaries():
    u = []
    f = []
    for i in db:
        a, b = i.split(",")
        a = a.strip()
        b = b.strip()
        u.append(a)
        f.append(b)
    data = dict(zip(u, f))
    return data

home()