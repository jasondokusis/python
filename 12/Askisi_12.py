from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import json

#driver = webdriver.Chrome('D:\Software Development\chromedriver\chromedriver.exe')
#driver.get('https://drand.cloudflare.com/public/latest')

#Φόρτωση σελίδας

page = requests.get('https://drand.cloudflare.com/public/latest')
print(page)

#Εύρεση απαραίτητων πληροφοριών στη σελίδα (δηλαδή του τελευταίου γύρους για να βρούμε τα τελευταία 100 στοιχεία με βάση αυτόν)
soup = BeautifulSoup(page.text, 'lxml')
text = soup.find('p').text
data = json.loads(text)

#Εμφάνιση της τυχαιότητας σε δυαδική μορφή
print(bin(int(data["randomness"], 16))[2:])

#Άνοιγμα του TextFile1
file = open('TextFile1.txt', 'w')

#Για κάθε από τις τελευταίες 100 τιμές θα υπολογίοζονται τα απαραίτητα στοιχεία και θα γράφονται 
#σε ένα αρχείο για περαιτπέρω επεξεργασία κκαι εύρεση των μεγίστων ακολουθιών μονάδων και μηδενικών
for i in range(100):
    page = requests.get('https://drand.cloudflare.com/public/' + str(data["round"] - i))
    soup = BeautifulSoup(page.text, 'lxml')
    text = soup.find('p').text
    data = json.loads(text)
    randomness = data["randomness"]
    randomness_hex = int(randomness, 16)
    file.write(bin(randomness_hex)[2:])

#Άνοιγμα του αρχείου για διάβασμα
file = open('TextFile1.txt', 'r')
data = file.read()

#Εύρεση των θέσεων της μέγιστης ακολουθίας από μονάδες και εμφάνισή της στην οθόνη
start_pos = 0
end_pos = -1
max_start_pos = 0
max_end_pos = 0
new_sequence = False
for i in range(len(data)):
    if(new_sequence):
        if(data[i] == '1'):
            end_pos = end_pos + 1
        else:
            new_sequence = False
            if(max_end_pos - max_start_pos + 1 < end_pos - start_pos + 1):
                max_start_pos = start_pos
                max_end_pos = end_pos
    else:
        if(data[i] == '1'):
            new_sequence = True
            start_pos = i
            end_pos = i

print(str(max_start_pos) + ' ' + str(max_end_pos))

for i in range(len(data)):
    if(i == max_start_pos):
        print('Start of sequence of ones : ' + data[i], end= " ") 
    print(data[i], end = " ")
    if(i == max_end_pos):
        print('End of Sequence of ones.', end = " ")

    start_pos = 0

#Εύρεση της μέγιστης ακολουθίας από μηδενικά και εμφάνιση στην οθόνη
end_pos = -1
max_start_pos = 0
max_end_pos = 0
new_sequence = False
for i in range(len(data)):
    if(new_sequence):
        if(data[i] == '0'):
            end_pos = end_pos + 1
        else:
            new_sequence = False
            if(max_end_pos - max_start_pos + 1 < end_pos - start_pos + 1):
                max_start_pos = start_pos
                max_end_pos = end_pos
    else:
        if(data[i] == '0'):
            new_sequence = True
            start_pos = i
            end_pos = i

print('Maximum sequence of zeroes:')

print(str(max_start_pos) + ' ' + str(max_end_pos))

for i in range(len(data)):
    if(i == max_start_pos):
        print('Start of sequence of zeroes : ', end= " ")
    print(data[i], end = " ")
    if(i == max_end_pos):
        print('End of Sequence of zeroes.', end = " ")
    

