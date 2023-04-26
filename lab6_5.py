# QUESTION 1
def findCommon(list1, list2):
    common = []
    for elem in list1:
        if elem in list2 and elem not in common:
            common.append(elem)
    return common

# QUESTION 2
def palindromes(strings):
    palindromes = []
    for s in strings:
        if s == s[::-1]:
            palindromes.append(s)
    return palindromes

# QUESTION 3
def getPrimes(numbers):
    primes = []
    while numbers:
        prime = numbers[0]
        primes.append(prime)
        numbers = [n for n in numbers if n % prime != 0]
    return primes

# QUESTION 4
def anagrams(word, word_list):
    word_list1 = [ch.lower() for ch in word if ch != " "]
    anagrams_list = []
    for string in word_list:
        string_list = [ch.lower() for ch in string if ch != " "]
        if len(word_list1) == len(string_list):
            is_anagram = True
            for ch in word_list1:
                if ch in string_list:
                    string_list.remove(ch)
                else:
                    is_anagram = False
                    break
            if is_anagram:
                anagrams_list.append(string)
    return anagrams_list

print("Question 1:")
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = findCommon(list1, list2)
print(result)
print()

print("Question 2:")
strings = ["level", "python", "computer", "madam", "noon"]
result = palindromes(strings)
print(result)
print()

print("Question 3:")
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = getPrimes(numbers)
print(primes)
print()

print("Question 4:")
word = "listen"
word_list = ["enlists", "google", "inlets", "banana", "computer"]
anagrams_list = anagrams(word, word_list)
print(anagrams_list)

