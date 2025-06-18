'''
tp:
- a balanced collection is one where the difference between the max and min value of art pieces is 1
'''

def find_balanced_subsequence(art_pieces):
    
    unique_values = set(art_pieces)
    result = 0

    for val in unique_values:
        if val + 1 in unique_values:
            subsequence_length = 0
            for piece in art_pieces:
                if piece == val or piece == val + 1:
                    subsequence_length += 1
            result = max(result, subsequence_length)

    return result





art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))




