import numpy as np
def t(name):
  rows = int(input(f"enter  number of rows {name}:") )   
  cols = int(input(f"Enter number of cols {name}:")) 
  print("Enter elements for {name} each row (space seperated)")     
  element=[]  
  for i in range(rows):
    row = list(map(int,input(f"Rows{i+1}").split()))
    if(len(row)  != cols):
        print("Enter row same as column of matrix 1.")
        return t(name)
    element.append(row)
    
  return  np.array(element)


print("Matrix  a:")
A=t("A")
print("Matrix  B:")
B=t("b")

if(A.shape[1] != B.shape[0]):
    print("Enter row same as column of matrix 1.")
else:
    result=np.dot(A,B) 
    print(result)