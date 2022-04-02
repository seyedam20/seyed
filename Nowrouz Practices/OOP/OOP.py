import re
import hashlib
class Account:
    def __init__(self, username, password, phonenumber, Email):
        pattern_username = '[A-Za-z]_[A-Za-z]'
        pattern_password = '^(.{0,7}|[^0-9]*|[^A-Z]*|[^a-z]*|[a-zA-Z]*|[a-z1-9]*|[A-Z1-9]*)$'
        pattern_phonenumber1 = '^\+989[0-9]{9}$'
        pattern_phonenumber2 = '^09[0-9]{9}$'
        pattern_email = '^[\w\-\.]+@[\w\-\.]+\.[A-Za-z]{2,5}$'
        if re.findall(pattern_username, username):
            self.username = username
        else:
            raise Exception('invalid username')
        if re.findall(pattern_password, password):
            raise Exception('invalid Password')
        else:
            self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if re.findall(pattern_phonenumber1, phonenumber):
            self.phonenumber = '+989xxxxxxxxx'
        elif re.findall(pattern_phonenumber2, phonenumber):
            self.phonenumber = '09xxxxxxxxx'
        else:
            raise Exception('invalid phonenumber')
        if re.findall(pattern_email, Email):
            self.Email = Email
        else:
            raise Exception('invalid email')
class Site:
    def __init__(self, url, register_users, active_users):
        self.url = url
        self.register_users = register_users
        self.active_users = active_users
    def register(self, object):
       if [object.password, object.Email, object.username] not in self.register_users:
           self.register_users.append([object.password, object.Email, object.username])
           self.register_users.append([object.password, object.Email])
           self.register_users.append([object.password, object.username])
           print('register successful')
       else:
           raise Exception('user already registered')
    def login(self, password, email=None, username=None):
        ramz = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if email != None and username == None:
            if [ramz, email] in self.active_users:
                print('user already logged in')
            elif [ramz, email] in self.register_users:
                print('login successful')
                self.active_users.append([ramz, email])
        elif email == None and username != None:
            if [ramz, username] in self.active_users:
                print('user already logged in')
            elif [ramz, username] in self.register_users:
                print('login successful')
                self.active_users.append([ramz, username])
        elif email != None and username != None:
            if [ramz, email, username] in self.active_users:
                print('user already logged in')
            elif [ramz, email, username] in self.register_users:
                print('login successful')
                self.active_users.append([ramz, email, username])
            else:
                print('invalid login')
    def logout(self, object):
        if [object.password, object.Email, object.username] in self.active_users:
            self.active_users.remove([object.password, object.Email, object.username])
            print('logout successful')
        elif [object.password, object.Email] in self.active_users:
            self.active_users.remove([object.password, object.Email])
            print('logout successful')
        elif [object.password, object.username] in self.active_users:
            self.active_users.remove([object.password, object.username])
            print('logout successful')
        else:
            print('user is not logged in')