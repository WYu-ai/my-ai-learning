scores={'张三':85,'李四':92,'王五':78}
scores['赵六']=88
scores['李四']=95
del scores['王五']
for name,score in scores.items():
    print(f'{name}的成绩是{score}分')
totle=sum(scores.values())
average=totle/len(scores)
print(f'\n全班平均成绩:{average:.1f}分')
search=input('请输入学生名字')
if search in scores:
    print(f'{search}的成绩是{scores[search]}分')
else:
    print('查无此人')