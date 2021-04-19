#Only use input() to get input from the console
in_str = input()



def get_factorial(num):
  prod = 1
  while num !=1:
    prod = prod * num
    num = num-1
    
  return prod

def get_dup():
    dist_list = [[]]

    
    for i in in_str:
        if i in dist_list[0]:
            for j in dist_list[0]:
                if j==i:
                    if dist_list[1] == None:
                        dist_list[1] = 1
                

    
    if 