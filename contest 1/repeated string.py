def repeatedString(s, n):
    count=s.count('a')
    first=count*(n // len(s))
    left= s[0:n % len(s)].count('a')
    count=first + left
    return count
