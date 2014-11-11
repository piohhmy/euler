""" Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names,  begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file? """


def alphabetical_value(name):
    return sum([ord(letter) - 64 for letter in name])

def solve_p22():
    with open('p022_names.txt', 'r') as namefile:
        names = namefile.readline()

    namelist = sorted([name.strip('"') for name in names.split(",")])

    total = 0
    for i, name in enumerate(namelist):
        total += (i+1) * alphabetical_value(name)
    return total

if __name__ == '__main__':
    print solve_p22()