def email_validator():
    global confirm_email_address
    email_address = input('Put in your email address: ')
    confirm_email_address = input('Confirm your email address: ')
    if email_address == confirm_email_address:
        password = input('Put in your password: ')
        confirm_password = input('Confirm your password: ')
    
        if password != confirm_password:
            print('Incorrect password, please try again')
            return
        else:
            display_email_address = input('Put in your email address: ') 
            display_password = input('Put in your password: =>')
            if display_email_address == confirm_email_address and display_password == confirm_password:
                print('Password and Email Validated')
            else:
                print('Incorrect password or email')
                display_email_address = input('Put in your email address: ') 
                display_password = input('Put in your password: =>')
                if display_email_address == confirm_email_address and display_password == confirm_password:
                    print('Password and Email Validated')
                else:
                    print('CREATE A NEW ACCOUNT')
                    email_validator()
    else:
        print('Incorrect email, please try again')
        display_email_address = input('Put in your email address: ') 
        display_password = input('Put in your password:=> ')
        if display_email_address == confirm_email_address and display_password == confirm_password:
            print('Password and Email Validated')
        else:
            print('CREATE A NEW ACCOUNT')
            email_validator()
    
        
   
    
    
email_validator() 

        