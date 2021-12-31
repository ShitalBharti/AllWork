'''count and display the vowels of a given text'''
def check_vow(string,vowels):
    final=[each for each in string if each in vowels]
    print(len(final))
    print(final)

string="my name is shital"
vowels="aeiouAEIOU"
check_vow(string,vowels)