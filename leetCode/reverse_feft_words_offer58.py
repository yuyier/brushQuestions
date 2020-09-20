class ReverseLeftWords(object):
    def reverseLeftWords(self, s, n):
        str_len = len(s)
        s = s[n:str_len] + s[0:n]
        return s
