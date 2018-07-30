import sys,math,re

password = input("Please Enter a Password.")

pl = str(len(password)) #Password Length
global gpc #Good Password Checker

global cmp #Common Matched Password
digits = len(re.findall(r"[0-9]", password)) #Checks For All Digits
UC = len(re.findall(r"[A-Z]", password)) #Checks For All Uppercase Letters

cpw = ['123456' , '123456789' , 'qwerty' , '111111' , 'LetMeIn' , 'welcome' , 'dragon' , 'password' , 'passw0rd' , 'test']

space = ' ' #Checking For Spaces in Passwords
spaces = password.split()

if len (password) < 6:
    print("[!] Password Must be Atleast 6 Characters Long.")
    print("[!] Your Password Is" , pl , "Character(s) Long.")
    gpc = False

else:
    print("[*] Password Is" , pl , "Characters Long.")
    gpc = True

if space in spaces:
    print("[!] Make Sure your Password Has No Spaces in.")
    gpc = False

for cps in cpw:

    if cps == password:
        print("[!] Password Supplied Is a Commonly Used Password.")
        cmp = True

if digits == 0:
    print("[!] Password Contains no Digits!")

if UC == 0:
    print("[!] Password Contains no Uppercase Letters.")

if digits > 0:
    print("[*] Password Contain(s)" , digits , "Digits.")

if UC > 0:
    print("[*] Password Contain(s)" , UC , "Uppercase Letters.")

if cps != password:
        print("[*] Password Supplied Is Not a Commonly Used Password.")
        cmp = False

print("=" * 20)

print("Password Evaluation:")

print("=" * 20)
if gpc == True:
    print("[*] Password Length is good.")

else:
    print("[!] Password is too short.")

if UC >= 3:
    print("[*] Your password Contains a Good Amount of Uppercase Letters.")

else:
    print("[!] Your password Doesn't Contain Enough Uppercase Letters.")

if digits >= 3:
    print("[*] Your password Contains a Good Amount of Digits.")

else:
    print("[!] Your password Doesn't Contain Enough Digits.")

if gpc == True and digits >= 3 and UC >= 3:
    print("[*] You have a good Password.")
else:
    print("[!] Your Password may be Vunerable.")