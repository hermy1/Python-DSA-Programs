'''
a program that utilizes a stack to determine if an inputted string is a palindrome or not

'''


import re 
class Palidrome(object):
    def __init__(self, word) -> None:
        self._stack = []
        self._top = -1
        self._word = re.sub(r'[^A-Za-z]', '', word).lower()

    def push(self, item):
        self._top += 1
        self._stack.append(item)
    
    def pop(self):
        if self._top <= -1:
            raise Exception('Underflow')
        copy = self._stack[self._top]
        self._stack[self._top] = None
        self._top -= 1
        return copy
    
    def is_palidrome(self):
        for letter in self._word:
            self.push(letter)
        backwords = ""
        for i in range(len(self._word)):
            backwords += self.pop()
        return backwords == self._word

word = "A man, a plan, a canal, Panama."
a = Palidrome(word)
print(a.is_palidrome())
        