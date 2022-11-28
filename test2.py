import requests
import time
def check(bits):
    match bits:
        case 'B':
            return 1
        case 'KB':
            return 1024
        case 'MB':
            return 1024 ** 2
        case 'GB':
            return 1024 ** 3
        case _:
            print('ошибка в измерении файла')
            return ValueError

def convert(num : int):
    l={0:'B',1:'KB',2:'MB',3:'GB'}
    if num<1024:
        return num,'B'
    else:
        for i in range(4):
            if(num//(1024**i))<=1024:
                return [num//(1024**i),l[i]]


start=time.time()
url = requests.get('https://stepik.org/media/attachments/lesson/569749/files.txt')
date = url.text.split('\r\n')
date_2=[i.split() for i in date]
date_2_sorted_by_name = sorted(date_2,key = lambda x:x[0])
date2_sorted_by_type = sorted(date_2_sorted_by_name,key = lambda x:x[0].split('.')[1])
type_l=sorted(set(map(lambda x:  x[0].split('.')[1],date2_sorted_by_type)))
dict_date = {i:[] for i in type_l}
s=type_l[0]
sums=0
for i in date2_sorted_by_type:
    if s!=i[0].split('.')[1]:
        s=i[0].split('.')[1]
        print('----------')


        print('Summary:',*convert(sums))
        sums=0
        print()
    dict_date[i[0].split('.')[1]].append([i])
    sums+=int(i[1])*check(i[2])
    print(i[0])

print('----------')
print('Summary:', *convert(sums))

