import sys

def count_vowel_sequences(morse_string):
    vowel_codes = {
        'A': '.-',
        'E': '.',
        'I': '..', 
        'O': '---',
        'U': '..-'
    }
    n = len(morse_string)
    dp = [0] * (n+1) #an list of length n+1, initialized with all values ​​of 0
    dp[n] = 1 #Empty string
    #Calculate from back to front
    for i in range(n - 1, -1, -1):
        for pattern in vowel_codes.values():
            pattern_len = len(pattern)
            if i + pattern_len <= n and morse_string[i:i+pattern_len] == pattern:
                dp[i] += dp[i + pattern_len]
    return dp[0]

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0].strip())
    morse_string = lines[1].strip()
    count = count_vowel_sequences(morse_string)
    print(f"The Number of Vowel combinations is: {count}")

#Prgram Entry
if __name__ == "__main__":
    main()
