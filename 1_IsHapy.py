def isHappy( self, n: int)-> int :
    sum = n
    S = set()
    
    def to_list(k:int):
        to_lst =[int(elements) for elements in list(str(k))]
        return to_lst
    def sum_pow_list( l : list) :
        summ = 0
        for i in range(len(l)):
            summ += pow(l[i], 2)
        return summ
        
    while sum != 1:
        sum=sum_pow_list(to_list(sum)) 
        if S.__contains__(sum):
            return False
        S.add(sum)
        
    return True
    

print(isHappy(19))
print(isHappy(2))