email=input("Enter  a valid email Id")
a,b,c=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") or (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        a=1
                    elif i.isalpha():
                        if i==i.isupper():
                            b=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
    
                if a==1 or b==1 or c==1:
                    print("Right Email ")
                else:
                    print("Wrong Email 5")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")