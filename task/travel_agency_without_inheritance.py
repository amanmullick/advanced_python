#this program is for travel agency WITHOUT using INHERITANCE

class Destination:          #defination of class destination 

    city = ["Ahmedabad","Mumbai","Kolkata","Bangalore","Pune","Hyderabad","Jaipur","Agra","Chennai","New Delhi"]    #creating a list that contains all the cities            

    def show_city(self):                    #defining function show_city to display the city to the user
       
        print("\n================Welcome to Travel Agency===============\n")    #print function for dsigning 
        for i in self.city:                 #for loop to print the cities one by one
            print(i)

    def register(self):     #register function to ask the user whether they want to register or not
                           
        ch = input("\nDo You want To Register ? ['y/n'] : ")

        if ch == 'y' or ch == 'Y':          #if user want to register then show the signup else show thank you
            s.getData()                     #calling the getData method of signup class with the help of s object
            s.check_signup_data()           #calling the function
        else:
            print("\nThank You For The Visit\n")
            
            


class Signup:           #class for signup
    
    email = ""
    password = ""
    confirm_password = ""

    def getData(self):                                          #function to get the signup details
        print("\n=============Sign Up===================\n")    #print function for dsigning 
        self.email = input("enter email : ")                    #input for email
        self.password = input("enter password : ")              #input for password
        self.confirm_password = input("confirm password : " )    #input for confirm password

    def check_signup_data(self):                                #function to check the password
        if self.password==self.confirm_password:                #if both are same then registration success
            print("\nRegistration Success ")
            l.get_login_data()                                  #call the get_login_data function with the help of the object of Login class
            l.check_login_data()                                #call the function
        else:
            print("\npassword and confirm password not matched !!!! \n")    #when passwords does'nt match then print
            d.register()                                                    #call the register function 


class Login:                                                    #creating the login class

    email = ""
    password = ""

    def get_login_data(self):                                   #function to get the email and password
        print("\n===============Login=====================\n")  #print function for dsigning 
        self.email = input("enter email : ")
        self.password = input("enter password : ")

    def check_login_data(self):                                 #function to check the email and password entered by the user during signup
        if self.email == s.email and self.password == s.password:
            print("\nLogin Success\n")                          #if matches print success    
        else:
            print("\nAccess Denied !!\n")                       #if doesn't matches then print access denies


d = Destination()           #creating object for Destination class
s = Signup()                #creating object for Signup class
l = Login()                 #creating object for Login class

d.show_city()               #calling the show_city function with the help of d object
d.register()                #calling the register function with the help of d object





