#function.py

def times(a,b):
    return a*b

result = times(5,6)
print(result)

def setValue(newValue):
    x = newValue
    print('함수내부 : ', x)

result = setValue(5)
print(result)

#교집합을 리턴 하는 함수
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect('HAM','SPAM'))
print(result)