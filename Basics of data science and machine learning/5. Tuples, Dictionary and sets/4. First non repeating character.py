'''
In a given string, find the first non-repeating character .You are given a string, that can contain repeating characters. Your task is to return the first character in this string that does not repeat. i.e., occurs exactly once. The string will contain characters only from English alphabet set, i.e., ('A' - 'Z') and ('a' - 'z'). If there is no non-repeating character print the first character of string.
'''
def first(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return str1[0]

# Main
string = input()
print(first(string))
