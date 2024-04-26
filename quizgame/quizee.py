print('hellooo quiz')

score = 0
qa = input('what is your name ?  ')
if(qa.lower() == 'yusuf'):
    print('correct')
    score += 1
else :
     print('incorrect')

qa =input('what is cpu stand for ?  ')
if qa.lower() == "central processor unit":  
    print('correct answer')
    score += 1
else : 
     print('incorrect')


qa =input('what is GPU stand for ?  ')
if qa.lower() == "graphic processor unit":
    print('correct answer')
    score += 1 
else : 
     print('incorrect')
    
qa =input('what is ML stand for ?  ')
if qa.lower() == "mechine learning" :
        print('correct answer')
else : 
     print('incorrect')

print('your score is ' + str((score/4) *100) + ' %' )
print('your got  ' + str(score ) + ' qa correct' )
