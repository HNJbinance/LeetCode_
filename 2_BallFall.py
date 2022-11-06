def findBall( grid: list[list[int]]) -> list[int]:
    m = len(grid)
    n = len (grid[0])
    
    top = 0
    left = 0
   
    answer =[]
    
        
    for i in range (n-1):
        left = i
        while top < m :
            while grid [top][left]== grid [top][left+1]:
                if grid [top][left] == 1 and grid [top+1][left+1] == 1:
                    top +=1
                    left+=1
                    
                elif grid [top][left] == -1 and grid [top+1][left] == 1:
                    top +=1
                print(top, left)
                    
            if top == m and grid [top][left] == -1:
                answer.append(left)
                print('zebi')
            elif top == m and grid [top][left] == 1:
                answer.append(left+1)
                print('z')
            else:
                answer.append(-1)
        print('bsbjsqhqj')      
    return answer 


grid1 = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
grid2   =   [[-1]]
grid3  =   [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]

print(findBall(grid1))
# print(findBall(grid2))
# print(findBall(grid3))