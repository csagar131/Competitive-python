from itertools import combinations

def checkvowel(s):
    if s[0] in ['A','E','I','O','U']:
        return True
    return False

def minion_game(test_str):
    ck,cs = 0,0
    lst = []
    s = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r = 2)]
    for i in range(len(s)):
        if checkvowel(s[i]) and s[i] not in lst:
            lst.append(s[i])
            ck+= s.count(s[i])
        else:
            if not checkvowel(s[i]) and s[i] not in lst:
                lst.append(s[i])
                cs+= s.count(s[i])
    if cs == ck:
        print("Draw")            
    elif cs > ck:
        print('Stuart',cs)
    else:
        print('Kevin',ck)
