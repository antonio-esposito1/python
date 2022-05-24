from multiprocessing import parent_process
import sys

if __name__== "__main__":
    template ='{0}, {1} and {2}'
    print(template.format('spam', 'ham', 'eggs'))
    template = '{motto}, {pork} and {food}'
    print(template.format(motto='spam', pork='ham', food='eggs'))
    template = '{motto}, {0} and {food}'
    print(template.format('ham', motto='spam', food='eggs'))
    template ='{}, {} and {}'
    print(template.format('spam', 'ham', 'eggs'))
    '{0:10} = {1:10}'.format('spam', 123.4567)
    '{0:>10} = {1:<10}'.format('spam', 123.4567)
    '{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop'))
    '{0:e},{1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159)
    '{0:f},{1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159)
    format(1.2345, '.2f')
    print('%s=%s' % ('spam', 42))
    print('{0}={1}'.format('spam', 42))
    print('{}={}'.format('spam', 42))
    print('%s, %s and %s' % (3.14, 42, [1,2]))
    print('My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform' : sys.platform})
    print('My %(kind)s runs %(platform)s' % dict(kind= 'laptop', platform=  sys.platform))
    somelist = list('SPAM')
    print(somelist)
    parts = somelist[0], somelist[-1], somelist[1:3]
    print(parts)
    print("first=S, last=M, middle=['P', 'A']")
    print("""**************************LIST**********************************""")
    print(len([1,2,3]))
    print(['NIL'] * 4)
    print(str([1,2])+'34')
    print([1,2] + list('34'))
    print(3 in [1,2,3])
    for x in [1,2,3]:
        print(x, end=' ')
    print([c*4 for c in 'SPAM'])
    print(list(map(abs, [-1, -2, 0, 1, 2])))
    L = ['spam', 'Spam', 'SPAM!']
    print(L[2])
    print(L[-2])
    print(L[1])
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(matrix)
    print(matrix[1])
    print(matrix[1][1])
    print(matrix[2][0])
    L.append('please')
    print(L)
    L.sort()
    print(L)
    L=['abc', 'ABD', 'aBe']
    L.sort()
    print(L)
    L=['abc', 'ABD', 'aBe']
    L.sort(key=str.lower)
    print(L)
    L=['abc', 'ABD', 'aBe']
    L.sort(key=str.lower, reverse=True)
    print(L)
    L = [1,2]
    L.extend([3,4,5])
    print(L)
    L.pop()
    print(L)
    L.reverse()
    print(L)
    print(list(reversed(L)))
    L= []
    L.append(1)
    L.append(2)
    print(L)
    L = ['spam', 'Spam', 'SPAM!']
    print(L.index('Spam'))
    L.remove('Spam')
    print(L)
    print(L.pop(1))
    print(L.count('spam'))
    print("""**************************DICTIONARIES*************************""")
    D = {'spam': 2, 'ham': 1, 'eggs': 3}
    print(D['spam'])
    print(D)
    print(len(D))
    print('ham' in D)
    print(list(D.keys()))
    print(D)
    D['ham'] = ['grill', 'bake', 'fry']
    print(D)
    del D['eggs']
    print(D)

    print('''*************************Tuple***************************************''')

    x = (40)
    y = (40,)
    T = ('cc', 'aa', 'dd', 'bb')
    print(list(T))
    print(list(T).sort())
    tmp = list(T)
    tmp.sort()
    print(tmp)
    T = (1,2,3,4,5,2)
    L = [x + 20 for x in T]
    print(L)
    print(T.index(2))
    print(T.index(2,2))
    print(T.count(2))
    print('''********************Tuple Swap Variable***************************************''')
    nudge = 1
    wink = 2
    nudge, wink = wink, nudge
    print('ho scambiato le due variabili senza usare una variabile di appoggio')
    print(nudge,wink)

    print('''************************Sequence Assignment************************************''')
    [a, b, c] = (1, 2, 3)
    print(a,c)
    (a, b, c) ="ABC"
    print(a,c)

    print('''************************Advanced Sequence Assignment************************************''')
    string = 'SPAM'
    a, b, c, d = string
    print(a, d)
    a, b, c = string[0], string[1], string[2:]
    print(a,b,c)
    a,b,c = list(string[:2]) + [string[2:]]
    print(a,b,c)
    print('stesso ma più semplice')
    a,b = string[:2]
    c = string[2:]
    print(a,b,c)
    print('Nested sequence')
    (a,b),c = string[:2], string[2:]
    print(a,b,c)
    print('Assignment range')
    red, green, blue = range(3)
    print(list(range(3)))
    print(red, blue)
    print('sequence in while loop')
    L = [1, 2, 3, 4]
    while L:
        front, L = L[0], L[1:]
        print(front, L)
    print('Extended Sequence unpacking')
    seq = [1, 2, 3, 4]
    a, *b = seq
    print(a, b)
    *a,  b = seq
    print(a, b)
    a, *b, c = seq
    print(a, b, c)
    a, *b = 'spam'
    print(a, b)
    a, *b, c = 'spam'
    print(a, b, c)
    a, *b, c = range(4)
    print(a, b, c)
    print('Extended sequence in while loop')
    L = [1, 2, 3, 4]
    while L:
        front, *L = L
        print(front, L)
    print('Se la variabile con* match sono un item qursto viene comunque preso come lista')
    seq = [1, 2, 3, 4]
    a, b, c, *d = seq
    print(a, b, c, d)
    seq = [1, 2, 3, 4]
    a, b, c, d, *e = seq
    print(a, b, c, d, e)
    a, b, *e, c, d = seq
    print(a, b, c, d, e)
    print('Extended sequence in for loop ')
    for (a,b,c) in [(1, 2, 3), (4, 5, 6)]:
        print(a,b,c)
    print('multi-target assignment')
    a = b = c = 'spam'
    print(a, b, c)
    print('multi-target assignment for immutabile object, fino a che un oggetto è immutabile è irrilevante se più di un riferimento punta ad esse')
    a = b = 0
    b = b +1
    print(a, b)
    print('multi-target assignment for mutabile object')
    a = b = []
    b.append(42)
    print(a, b)
    print('''************************Augmented assignment*****************************************''')
    X=1
    X += X
    print(X)
    S = 'spam'
    S += 'SPAM'
    print(S)
    X = 2
    X *= 2
    print(X)
    X = 2
    X >>= 1
    print(X)
    X = 4
    X //= 2
    print(X)
    print('****************Augmented assignment per oggetti per oggetti mutabili, concatenazione crea sempre un nuovo oggetto mentre augmented assignment è un in place')
    print('chance che non crea un nuovo oggetto')
    L = [1, 2]
    M = L 
    L = L + [3,4]
    print(L, M)
    L = [1, 2]
    M = L 
    L += [3,4]
    print(L, M)
    print('''************************File In Action*****************************************''')
    f = open('myfile', 'w')
    f.write('Hello World\n')
    f.write('goodbye\n')
    f.close()
    f = open('myfile')
    print(f.readline())
    print(f.readline())
    print(f.readline())
    f.close()
    f = open('myfile')
    print(f.read())
    for line in open('myfile'):
        print(line, end='')
    print('''************************File Storing: Conversion*********************''')
    X,Y,Z = 43, 44, 45
    S = 'Spam'
    D = {'a': 1, 'b': 2}
    L = [1,2,3]
    F = open('datafile.txt', 'w')
    F.write(S + '\n')
    F.write('%s, %s, %s\n' % (X, Y, Z))
    F.write(str(L) + '$' + str(D) + '\n')
    F.close()
    char = open('datafile.txt').read()
    print(char)
    F = open('datafile.txt')
    line = F.readline()
    print(line)
    print(line.rstrip())
    line = F.readline()
    print(line)
    parts = line.split(',')
    print(parts)
    print(int(parts[1]))
    numbers = [int(P) for P in parts]
    print(numbers)
    line = F.readline()
    print(line)
    parts = line.split('$')
    print(parts)
    print(eval(parts[0]))
    objects = [eval(P) for P in parts]
    print(objects)
    F.close()
    print('''************************************Storing Native Objects: pickle*********************''')
    D = {'a': 1, 'b': 2}
    F = open('datafile.pkl', 'wb')
    import pickle
    pickle.dump(D, F)
    F.close()
    F = open('datafile.pkl', 'rb')
    E = pickle.load(F)
    print(E)
    F.close()
    print('''************************************Storing Native Objects: JSON*********************''')
    name = dict(first='Bob', last='Smith')
    rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
    import json
    S=json.dumps(rec)
    print(S)
    O = json.loads(S)
    json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
    print(open('testjson.txt').read())
    P=json.load(open('testjson.txt'))
    print(P)

    print('''************************try statement versione1**********************''')
    while True:
        reply = input('Enter text:')
        if reply == 'stop': break
        try:
            num = int(reply)
        except:
            print('Bad!' * 8)
        else:
            print(num**2)
    print('Bye')
    print('''************************try statement versione2 try senza else**********************''')
    while True:
        reply = input('Enter text:')
        if reply == 'stop': break
        try:
            print(int(reply)**2)
        except:
            print('Bad!' * 8)
    print('Bye')
    print('''************************try statement versione3 try gestisce float**********************''')
    while True:
        reply = input('Enter text:')
        if reply == 'stop': break
        try:
            print(float(reply)**2)
        except:
            print('Bad!' * 8)
    print('Bye')
    print('''***************************Nesting Code Three Level Deep********************************''')
    while True:
        reply = input('Enter text:')
        if reply == 'stop':
            break
        elif not reply.isdigit():
            print('Bad!' * 8)
        else:
            num = int(reply)
            if num < 20:
                print('low')
            else:
                print(num**2)
    print('Bye')
    print('*************************La funzione print ***************************************************')
    x = 'spam'
    y = 99
    z = ['eggs']
    print(x, y, z)
    print(x, y, z, sep = ', ')
    print(x, y, z, end = '')
    print(x, y, z, end = '...\n')
    print(x, y, z, sep = '...', end = '...\n')
    print(x, y, z, sep = '...', end = '...\n', file = open('data.txt', 'w'))
    print('il prossimo testo è letto dal file')
    print(open('data.txt').read())
    print('formattazione avanzata')
    text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
    print(text)
    print('***************Manual Stream Redirection********************************************************')
    temp = sys.stdout
    sys.stdout = open('log.txt', 'a')
    print('spam')
    print(1, 2, 3)
    sys.stdout.close()
    sys.stdout = temp
    print('bach here')
    print(open('log.txt').read())
