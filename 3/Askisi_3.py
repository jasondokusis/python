#Άνοιγμα αρχείου TextFile1
file = open('TextFile1.txt', 'r')
data = file.read()

#Αντικατάσταση συμβόλωμ
data = data.replace("\n", " ")
data = data.replace(".", "")
data = data.replace("\"", "")
data = data.replace("?", "")
data = data.replace(",", "")
print(data)

#Εισαγωγή λέξεων του αρχείου στην words
words = data.split()

#Λίστα λέξεων που πρέπει να αφαιρεθούν
words_to_remove = []

#Υπολογισμός λέξεων που πρέπει να αφαιρεθούν (Επιλέγονται μόνο αν δεν έχουν ήδη προστεθεί στη λίστα words_to_remove για αφαίρεση αργότερα)
for i in range(len(words)):
    for j in range(len(words)):
        if(i != j and len(words[i]) + len(words[j]) == 20 and words_to_remove.count(words[i]) == 0 and words_to_remove.count(words[j]) == 0):
            words_to_remove.append(words[i])
            words_to_remove.append(words[j])

print(words)
print(' ')
print(words_to_remove)

#Αφαίρεση λέξεων
for word in words_to_remove:
    words.remove(word)

print(' ')

#Υπολογισμός μήκους λέξεων και πρόσθεσή τους σε μια λίστα
wordlengths = []
for word in words:
    wordlengths.append(len(word))
print(wordlengths)

#Υπολογισμός λέξης με μέγιστο μήκος για να μην υπολογιστούν παραπάνω μήκη στα στατιστικά
max = 0
for length in wordlengths:
    if(length > max):
        max = length

#Λίστα στατιστικών για λέξεις με μήκη που έχουν ήδη τυπωθεί
already_told = []

#Υπολογισμός και εμφάνιση στατιστικών
for i in range(max + 1):
    if(already_told.count(wordlengths[i]) == 0):
        if(wordlengths.count(wordlengths[i]) != 1):
           print('There are ' + str(wordlengths.count(wordlengths[i])) + ' words with ' + str(wordlengths[i]) + ' letters')
        else:
           print('There is 1 word with ' + str(wordlengths[wordlengths[i]]) + ' letters')
        already_told.append(wordlengths[i])


