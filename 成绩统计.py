num = int(input("")) #表示人数
all_score = []
for i in range(num):
    i = float(input(""))
    all_score.append(i)
pass2=len([i for i in all_score if i>=60])/num*100 #及格率
excellent=len([i for i in all_score if i>=85])/num*100 #优秀率
print(str(int(pass2+0.5))+'%')#及格率
print(str(int(excellent+0.5))+'%')
##高级解法
n=int(input())
a=[int(input()) for i in range(n)]
def f(x):
    return format(100*len([i for i in a if i>=x])/n,'.0f')+'%'
print(f(60),f(85),sep='\n')
##########重写
n=int(input())
a = [int(input()) for i in range(n)]
def f(x):
    return format(100*len([i for i in a if i>=x])/n,'.0f')+'%'
print(f(60),f(85),sep='\n') #print sep分隔符设置为换行符

format(123,'.1f') #前面为数字 后面为保留多少位小数
