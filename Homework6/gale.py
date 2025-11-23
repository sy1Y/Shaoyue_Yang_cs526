import sys
from collections import deque

def gale_women(f_pref, m_pref):
    free_female = deque(f_pref.keys()) #initialization
    pair = {} #storage pair:{male:female}
    proposal = {women: 0 for women in f_pref.keys()}
    #create a ranking of male preferences
    male_rank = {}
    for man, pref in m_pref.items():
        male_rank[man] = {woman: i for i, woman in enumerate(pref)}
    while free_female: #Loop: there are still women left
        woman = free_female[0] #1st woman
        man = f_pref[woman][proposal[woman]] #pair her proposed men(in sequence)
        proposal[woman] += 1
        if man not in pair:
            pair[man] = woman #set a pair
            free_female.popleft() 
        else:
            #if the male already has a match, compare his preference
            current_female = pair[man]
            #if this man prefers the new woman
            if male_rank[man][woman] < male_rank[man][current_female]:
                pair[man] = woman #update
                free_female.popleft()
                #push original matched woman back to front
                free_female.appendleft(current_female)
    return pair

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    m_pref = {}
    f_pref = {}
    for i in range(1, n+1): #analyzing male preferences
        m = lines[i].split()
        m_pref[m[0]] = m[1:n+1] #1st-name, followed-preferences
    for i in range(n+1, 2*n+1): #analyzing female preferences
        m = lines[i].split()
        f_pref[m[0]] = m[1:n+1]
    print("\nWomen priority:")
    women_match = gale_women(m_pref, f_pref) #optimal stable match for women
    for woman, man in sorted(women_match.items()): #output
        print(f"{man} - {woman}")

if __name__ == "__main__":
    main()
