#미완성
def read_s(file_path):
    s_list = []
    for line in open(file_path,encoding='utf-8'):
        s_list.append(str(line.strip()))
    
    return s_list


s_list = read_s('./lis.txt')

def lis(string):

    if len(string) == 0:
        return 

    ret = 0
    for i in range(len(string)):
        pivot = string[i]
        for j in range(i+1,len(string)):
            if int(string[j]) > int(pivot[0]):
                pivot += string[j]
        poli_list.append(lis(pivot)) 
    return max(int(poli_list))
    

for s in s_list:
    print(lis(s))