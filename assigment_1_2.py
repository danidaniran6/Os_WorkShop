lessons = [float]
sum = float(0)
for i in range(0,3) :
    print("enter lesson",i+1," score :")
    while(1):
        if(score in range(0,2)):
            lessons.append(score)
            sum +=score
            break
        else :
            print("score not valid !!!")
            print("enter lesson",i+1," score :")
        score = float(input())


avg = float(sum/(len(lessons)-1))
print("%.2f" % avg)