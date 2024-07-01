def valid_soln(puz,soln):
    puzz=puz
    for k,v in soln.items():
        puzz=puzz.replace(k,str(v))
    try:
        return eval(puzz)
    except:
        return False

def solution(puz,letters,soln):
    if not letters:
        return valid_soln(puz,soln)
    l=letters[0]
    for digit in range(10):
        if digit not in soln.values():
            soln[l]=digit
            if solution(puz,letters[1:],soln):
                return soln
            del soln[l]
    return False


puz=input("Enter values in format word1 + word2 == ans\n")
letters=list(set([val for val in puz if val.isalpha()]))
ans=solution(puz,letters,{})

puzz=puz
print("SOLUTION ")
for k,v in ans.items():
    puz=puz.replace(k,str(v))
    print(k ," : ",v)
puz=puz.replace('==','=')
puzz=puzz.replace('==','=')
print(puzz)
print(puz)
