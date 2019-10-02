dic = {1:['a', 'b', 'c', 'd'], 2:[1,2,3,4]}

dic[1][0], dic[1][2] = dic[2][0], dic[2][2]
print(dic)