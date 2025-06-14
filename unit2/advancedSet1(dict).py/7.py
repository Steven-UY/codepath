'''
tp:
- the two dictionaries would need to have the same characters and the same frequency of characters in order to be considered an
anagram
- initially we can put each string into their own dictionaries
- loop through the second string
- for each character in map1, if map2 has fewer then we'll need to replace some other characters in map2 to make up the difference
'''

def min_steps_to_match_maps(map1, map2):
    
    #get the characters and the frequencies from each map
    freq1 = {}
    freq2 = {}

    #put the characters and their frequencies into each dictionary
    for i in range(len(map1)):
        if map1[i] not in freq1:
            freq1[map[i]] = 1
        else:
            freq1[map[i]] += 1
    
    for i in range(len(map2)):
        if map2[i] not in freq2:
            freq2[map[i]] = 1
        else:
            freq2[map[i]] += 1
    
    #now we need to check for each character in map1 does map2 have fewer characters?
    steps = 0
    
    for char in freq1:
        count1 = freq1[char]
        count2 = freq2.get(char, 0)
        if count1 > count2:
            steps += count1 - count2 






        

    