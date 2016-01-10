from itertools import count, takewhile

class TriangleNumberLazySolver():
    def __init__(self):
        self._triangles = []
        self._finder = self.triangle_num_generator()
        self._triangles.append(next(self._finder))

    def is_triangle_num(self, num):
        while num > self._triangles[-1]:
            self._triangles.append(next(self._finder))

        return num in self._triangles

    @staticmethod
    def triangle_num_generator():
        for n in count(1):
            yield (n * (n+1))//2

def letter_value(letter):
    return ord(letter.upper()) - 64

def word_value(word):
    return sum(letter_value(letter) for letter in word)

def read_word_list(filename):
    with open(filename) as f:
        words = f.readline()
    return [word.strip('"') for word in words.split(',')]

def solve_p042():
    words = read_word_list('p042_words.txt')
    solver = TriangleNumberLazySolver()
    tri_words = [w for w in words if solver.is_triangle_num(word_value(w))]
    return len(tri_words)
        
    
