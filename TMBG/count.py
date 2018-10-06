## Unique words sung by They Might be Giants
# This script takes the first 17000 and first 35000 words in TMBG songs
# and returns the number of unique words sung. The sample has been taken
# from their studio albums in order of release (Pink album to ABCs).
# We excluded possessive "'s" to make things simpler

f = open('Test.dat', 'r') # Open raw lyrics file
# print f # print the file to make sure correct file has been opened

lyr = f.read() # Create a string of all lyrics
Lyr = lyr.split() # Split the string by spaces

print "Total Words: " + str(len(Lyr)) + "." # Total words sung

Lyr2 = [] # lyrics without special characters
y = "" # dummy string for the following loop

for x in Lyr: # this loop replaces special characters by empty strings
    y = x
    if '(' in x:
        y = y.replace('(', '')
    if ')' in x:
        y = y.replace(')', '')
    if '[' in x:
        y = y.replace('[', '')
    if ']' in x:
        y = y.replace(']', '')
    if ',' in x:
        y = y.replace(',', '')
    if "..." in x:
        y = y.replace('...', '')
    if '.' in x:
        y = y.replace('.', '')
    if ':' in x:
        y = y.replace(':', '')
    if '\\' in x:
        y = y.replace('\\', '')
    if '"' in x:
        y = y.replace('"', '')
    if '?' in x:
        y = y.replace('?', '')
    if '!' in x:
        y = y.replace('!', '')
    if '*' in x:
        y = y.replace('*', '')
    Lyr2.append(y.lower()) # lower case version of the word is added to collection of lyrics

Lyrmap = [] # Lyrics without possessives "'s"

for x in Lyr2: 
    if '\'' not in x and x != "":
        Lyrmap.append(x)

Lyr17k = Lyrmap[0:17000] # 17000 word cutoff
Lyr35k = Lyrmap[0:35000] # 35000 word cutoff

Voc17k = []
Voc35k = [] # List of unique lyrics sung by cutoff value

for x in Lyr17k:
    if x not in Voc17k:
        Voc17k.append(x)

for x in Lyr35k:
    if x not in Voc35k:
        Voc35k.append(x)

print "Total Vocabulary after 17k: " + str(len(Voc17k)) + "."
print "Total Vocabulary after 35k: " + str(len(Voc35k)) + "." # Display number of unique words sung
