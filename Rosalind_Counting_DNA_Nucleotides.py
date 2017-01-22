f = open('rosalind_dna.txt', 'r')
rawdata = f.readlines()
data = []                                   #empty list awaiting to be occupied with the DNA sequence 
for i in rawdata:                           #This for loop is necessary just in case the text file has multiple lines of data.
    data.append(i.strip('\n'))              #The string '\n' needs to be stripped from the DNA sequence and then I add the DNA
                                            #sequence to the "data" list
data = ''.join(data)                        #I then converted the list into a string so that I can interate through the string one
                                            #nucletotide at a time
count_dict = {'A':0, 'T':0, 'C': 0, 'G':0}  #this dictionary will act as the counting ledger
for i in data:
    if i == 'A':
        count_dict['A'] += 1                #adds the number 1 to the value of the dictionary key(in this case the key is the nucleotide)
    elif i == 'T':                          #each time the respective nucleotide appears in the DNA strand
        count_dict['T'] += 1
    elif i == 'C':
        count_dict['C'] += 1
    elif i == 'G':
        count_dict['G'] += 1
f = open('rosalind_counting_nuc_output.txt','w')
f.write(str(count_dict['A'])+' '+ str(count_dict['C'])+' '+str(count_dict['G'])+' '+str(count_dict['T']))
