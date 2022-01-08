#HackerRank
def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = ''.join(string)
    return string

if __name__ == '__main__':
