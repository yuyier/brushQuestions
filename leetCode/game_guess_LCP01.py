# coding=utf-8

class Game(object):
    def game(self, guess, answer):
        guess_len = len(guess)
        sum_guess = 0
        for i in range(guess_len):
            if guess[i] == answer[i]:
                sum_guess = sum_guess + 1
        return sum_guess
