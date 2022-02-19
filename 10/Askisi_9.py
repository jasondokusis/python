from colorama import Fore

#Άνοιγμα αρχείου
file = open('TextFile1.txt', 'r')
data = file.read()

#Εγγραφή του κάθε γράμματος
letters = list(data)
print(letters)
print ('')

#Υπολογισμός τιμών ASCII
ASCII_letters = []

for letter in letters:
    ASCII_letters.append(ord(letter))

#Μετατροπή σε 7-μπιτους αριθμούς

bin_letters = []

for letter in ASCII_letters:
    length = len(bin(letter))
    print('{0:07b}'.format(letter)[-7:])
    bin_letters.append('{0:07b}'.format(letter)[-7:])

#Εγγραφή στο TextFile2.txt

file = open('TextFile2.txt', 'w')

for letter in bin_letters:
    file.write(letter)

file = open('TextFile2.txt', 'r')
data = file.read()

#Υπολογισμός θέσεων μέγιστης ακολουθίας μονάδων και εμφάνισή τους μέσα στο αρχείο
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
        print('Start of sequence of ones : ', end= " ")
    print(data[i], end = " ")
    if(i == max_end_pos):
        print('End of Sequence of ones.', end = " ")

    start_pos = 0

#Υπολογισμός μέγιστης ακολουθίας μηδενικών και εμφάνισή τους στο αρχείο
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

