if __name__ == '__main__':
    n=int(input())
    ns=[[input(),float(input())] for i in range(n)]
    ns.sort(key=lambda x:x[1])
    sec_name=[]
    for i in range(n):
        if ns[i][1]!=ns[i+1][1]:
            sec_grade=ns[i+1][1]
            break
        
    for i in range(n):
        if sec_grade==ns[i][1]:
            sec_name.append(ns[i][0])

    sec_name.sort()
    for i in sec_name:
        print(i)
