def integertoroman (n=int):
        
    dictionnaire= {
                1000 :"M",
                900 :"CM",
                500 :"D",
                400 :"CD",
                100 :"C",
                90 :"XC",
                50 :"L",
                40 :"XL",
                10 :"X",
                9 :"IX",
                5 :"V",
                4 :"IV",
                1 :"I"  
                }
    ################################### start with an empty roman numeral ###################################
    romanNumeral = ''
    ################################## Initializing my variables#############################################
    rest = n
    ##### find the closest symbol that can be subtracted from the current number ############################
    while (rest != 0):
        
        for i in dictionnaire.keys() : 
            k = i
            if i > rest and rest != 0:
                print('yes, check with next roman numeral.')
                continue
            
            
            else:
                while rest >= i :
                    romanNumeral = romanNumeral + dictionnaire[k]
                    rest = rest - k 
                    
            print('index = ', i, 'rest = ', rest) 
            print('\n',romanNumeral)
        
    return romanNumeral 

integertoroman(1994)
integertoroman(58)
integertoroman(3)