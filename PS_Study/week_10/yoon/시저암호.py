import string
def solution(s, n):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    answer = ''
    for char in s:
        if char in lower:
            new_char = ord('a') + ((ord(char) - ord("a")) + n) % 26

        elif char in upper:
            new_char = ord('A') + ((ord(char) - ord("A")) + n) % 26
        else:
            new_char = ord(char)
        answer += chr(new_char)
    return answer

def solution(s, n):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    answer = ''
    for char in s:
        if char in lower:
            idx = lower.index(char)
            new_char = lower[(idx + n) % 26]
        elif char in upper:
            idx = upper.index(char)
            new_char = upper[(idx + n) % 26]
        else:
            new_char = char
        answer += new_char
    return answer
