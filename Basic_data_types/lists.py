if __name__ == '__main__':
    N = int(input())
    commands={}
    arr=[]
    for i in range(N):
        command_name,*rest=input().split()
        nums=list(map(int,rest))
        commands[command_name]=nums
        if(command_name=='insert'):
            arr.insert(commands[command_name][0],commands[command_name][1])

        elif(command_name=='print'):
            print(arr)    
            
        elif(command_name=='remove'):
            arr.remove(commands[command_name][0])    
            
        elif(command_name=='append'):
            arr.append(commands[command_name][0])    
            
        elif(command_name=='sort'):
            arr.sort()    
            
        elif(command_name=='pop'):
            arr.pop()    
   
        elif(command_name=='reverse'):
            arr.reverse()    
