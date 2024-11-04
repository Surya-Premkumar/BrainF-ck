code=str(input())
code=list(code)
array= [0] * 16
pointer=0
skiploop=0
counter=0
while counter<len(code):
    if code[counter]=="+":
        array[pointer]+=1
    elif code[counter]=="-":
        array[pointer]-=1
    elif code[counter]==">":
        pointer+=1
    elif code[counter]=="<":
        pointer-=1
    elif code[counter]==".":
        print(array[pointer])
    elif code[counter]==",":
        array[pointer]=int(input())
    elif code[counter]=="[":
        if array[pointer]==0:
            for counter2 in range(counter+1,len(code)-1):
                if code[counter2]=="[":
                    skiploop+=1
                elif code[counter2]=="]":
                    skiploop-=1
                    if skiploop==0:
                        counter=counter2
                    break
    elif code[counter]=="]":
        if array[pointer]!=0:
            for counter2 in range(counter-1,0,-1):
                if code[counter2]=="]":
                    skiploop+=1
                elif code[counter2]=="[":
                    if skiploop!=0:
                        skiploop-=1
                    if skiploop==0:
                        counter=counter2
                    break
    else:
        print("Error: Unknown character , Line", counter+1)
    counter+=1