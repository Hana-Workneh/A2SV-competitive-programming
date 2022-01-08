#HackerRank
def count_substring(string, sub_string):
    counter=0
    for i in range(0,len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            counter += 1
        else:
            pass
    return counter

if __name__ == '__main__':
