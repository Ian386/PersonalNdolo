class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val   


# paragraph Contains famous poem "Road not taken" by poet Robert Frost. You have to print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.



paragraph='''Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference.'''

hashTable = {}
for word in paragraph.split():
    word= word.replace('\n','')
    if word in hashTable:
        hashTable[word] +=1
    else:
        hashTable[word] = 1

# format the print statement
for key in hashTable:
    print(key,':',hashTable[key],end='\n')