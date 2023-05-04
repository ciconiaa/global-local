q1 = 'Press g if you choose the global alignment and press l if you choose the local alignment.\n'
from Bio import SeqIO
with open("foxp2human.fna") as s:
    for a_s in SeqIO.parse(s, "fasta"):
        q_s = a_s.seq[1:11]

with open("foxp2chimpanzee.fna") as t:
    for a_t in SeqIO.parse(t, "fasta"):
        q_t = a_t.seq[1:12]

# Global alignment
q1 = 'Press g if you choose the global alignment and press l if you choose the local alignment.\n'
block1 = 'Global alignment'
block2 = 'Local alignment'
q_s = a_s.seq[1:11]
q_t = a_t.seq[1:12]
termination = 'Exit'
printError = 'Error'
comment1 = 'p(i,j) matrix for the alignment'
comment2 = 'a(i,j) matrix for the score of the prefixes of the alignment'
g = -2
plus = 1
minus = -1
a1 = input(q1)
if a1 == 'g':
    print(block1)
    s = q_s.upper()
    t = q_t.upper()
    maxNumber = len(s+t)
    n_s = len(s)
    n_t = len(t)
    #print(maxNumber)
    import numpy as np             # імпорт пакету numpy для роботи з функцією array
    align_i = np.array(range(maxNumber), dtype=str)  # Формування матриць, тобто заповнення матриці align_i та align_j індексами
    #align_i = np.array(range(n_s), dtype=str)
    align_j = np.array(range(maxNumber), dtype=str)
    #align_j = np.array(range(n_t), dtype=str)
    #print(align_i, align_j)
    for i in range(maxNumber):
        align_i[i] = ' '
        align_j[i] = ' '
   # print(align_i)
    len_s = 0
    len_t = 0
    for i in range(n_s):
        if s[i] == 'A' or s[i] == 'G' or s[i] == 'C' or s[i] == 'T':
            len_s = len_s + 1
    for i in range(n_t):
        if t[i] == 'A' or t[i] == 'G' or t[i] == 'C' or t[i] == 'T':
            len_t = len_t + 1
    if (len_s == n_s) and (len_t == n_t):
        p = np.array([range(i, i + n_s) for i in range(n_t)], dtype=int) # Формування матриць (заповнення матриць р та а індексами)
        a = np.array([range(i, i + n_s + 1) for i in range(n_t + 1)], dtype=int)
# побудова масиву порівняння символів p(i,j)
        for i in range(n_t):
            for j in range(n_s):
                if t[i] == s[j]:
                    p[i][j] = plus
                else:
                    p[i][j] = minus
# ініціалізація нульового стовпчика та нульової строки матриці порівняння ваг префіксів a(i,j)
        for i in range(n_t + 1):
            a[i][0] = g * i
        for j in range(n_s + 1):
            a[0][j] = g * j
# розрахунок матриці порівняння ваг префіксів a(i,j)
        for i in range(n_t):
            for j in range(n_s):
                a[i+1][j+1] = max(a[i][j]+p[i][j],a[i][j+1]+g,a[i+1][j]+g)
        print(comment1)
        print(p)
        print(comment2)
        print(a)
        align_count = 0

# Розрахунок шляху вирівнювання, починаючи з останнього елементу матриці порівняння ваг префіксів a(i,j)
        i = 0
        j = 0
        while i<n_t:
            while j<n_s:         # Діагональний елемент в розрахунку шляху вирівнювання
                if a[n_t-i][n_s-j] == a[n_t-i-1][n_s-j-1]+p[n_t-i-1][n_s-j-1]:
                    align_i[align_count] = t[n_t-i-1]
                    align_j[align_count] = s[n_s-j-1]
                    i = i+1
                    j = j+1
                    align_count = align_count+1
                else:               # Внесення пробілу в послідовність s при розрахунку шляху вирівнювання
                    if a[n_t-i][n_s-j] == a[n_t-i-1][n_s-j]+g:
                        align_i[align_count] = t[n_t-i-1]
                        align_j[align_count] = ' '
                        i = i+1
                        align_count = align_count+1
                    else:           # Внесення пробілу в послідовність t при розрахунку шляху вирівнювання
                        if a[n_t-i][n_s-j] == a[n_t-i][n_s-j-1] + g:
                            align_i[align_count] = ' '
                            align_j[align_count] = s[n_s-j-1]
                            j = j+1
                            align_count = align_count+1
        print(align_i, '\n', align_j)
# Правильне розташування шляху вирівнювання
        res_t = ''
        res_s = ''
        for i in range(maxNumber):
            res_t = res_t + align_i[maxNumber - 1 - i]
            res_s = res_s + align_j[maxNumber - 1 - i]
        print('', res_t, '\n', res_s)
#        import numpy as np
#       np.set_printoptions( res_t, res_s)
    else:
        print(printError)


# Local alignment
if a1 == 'l':
    print(block2)
    s = q_s.upper()
    t = q_t.upper()
    maxNumber = len(s+t)
    n_s = len(s)
    n_t = len(t)
    #print(maxNumber)
    import numpy as np
    align_i = np.array(range(maxNumber), dtype=str)
    align_j = np.array(range(maxNumber), dtype=str)
    for i in range(maxNumber):
        align_i[i] = ' '
        align_j[i] = ' '
    #print(align_i)
    len_s = 0
    len_t = 0
    for i in range(n_s):
        if s[i] == 'A' or s[i] == 'G' or s[i] == 'C' or s[i] == 'T':
            len_s = len_s + 1
    for i in range(n_t):
        if t[i] == 'A' or t[i] == 'G' or t[i] == 'C' or t[i] == 'T':
            len_t = len_t + 1
    if (len_s == n_s) and (len_t == n_t):
        #print('true')
        p = np.array([range(i, i + n_s) for i in range(n_t)], dtype=int) # Формування матриць (заповнення матриць р та а індексами)
        a = np.array([range(i, i + n_s + 1) for i in range(n_t + 1)], dtype=int)
# побудова масиву порівняння символів p(i,j)
        for i in range(n_t):
            for j in range(n_s):
                if t[i] == s[j]:
                    p[i][j] = plus
                else:
                    p[i][j] = minus
# ініціалізація нульового стовпчика та нульової строки матриці порівняння ваг префіксів a(i,j)
        for i in range(n_t + 1):
            a[i][0] = 0 * i
        for j in range(n_s + 1):
            a[0][j] = 0 * j
# розрахунок матриці порівняння ваг префіксів a(i,j)
        for i in range(n_t):
            for j in range(n_s):
                a[i+1][j+1] = max(a[i][j]+p[i][j],a[i][j+1]+g,a[i+1][j]+g)
                if a[i+1][j+1]<0:
                    a[i + 1][j + 1]=0
        print(comment1)
        print(p)
        print(comment2)
        print(a)
        align_count = 0
    else:
        print(printError)
