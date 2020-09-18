class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
            
        return ret

tc = int(input())
for _ in range(tc):
    sequence = input()
    original = input()
    password = input()
    answer = []
    key_dic = dict()
    idx_dic = dict()
    for idx, key in enumerate(sequence):
        key_dic[idx] = key
        idx_dic[key] = idx

    for i in range(len(sequence)):
        new_pass = ""
        for char in password:
            origin_idx = idx_dic[char]
            new_idx = (origin_idx + i) % len(sequence)
            new_char = key_dic[new_idx]
            new_pass += new_char
        if new_pass.count(original) == 1:
            answer.append(str(i))

    if not answer:
        print("no solution")
    elif len(answer) > 1:
        print("ambiguous: {}".format(" ".join(answer)))
    else:
        print("unique: {}".format(answer[0]))
