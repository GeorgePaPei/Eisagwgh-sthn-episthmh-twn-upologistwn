import tweepy
import sys
#parakalw eisagetai ta authentication credentials sas
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


try:
    api.verify_credentials()
    print("Authentication OK.")
except:
    print("Error during authentication. \nPlease make sure your authentication credentials in the code are correct.")
    sys.exit()

userstring = input("Please insert user:")

statuses = api.user_timeline(userstring, count = 10)#Pernoume ta 10 teleutaia tweets.
last10 = ""
for status in statuses: #Ta vazoume ola se ena string.     
    last10 += status.text + "\n"

lista = [word for word in last10.split()] #Metatrepoume to string se lista apo lekseis

#Dhmiourgoume ena leksiko xrhsimopoiwntas tis lekseis pou uparxoyn mesa sth lista, etsi wste na afairesoume panomoiotipes lekseis.
#Kai sth sunexeia metatrpoume to leksiko pisw se lista.
lista = list(dict.fromkeys(lista))

#Taksinomhsh ths listas symfnwna me to mhkos twn leksewn.
lista.sort(key = len)

#Pop and show the 5 longest words.
for i in range(5):
    longest_word = lista.pop()
    print ("Longest word",i+1,":",longest_word) 

#Pop and show the 5 shortest words.
for i in range(5):
    shortest_word = lista.pop(0)
    print ("Shortest word",i+1,":",shortest_word)

        
   
    
        

