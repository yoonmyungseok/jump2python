def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
        
say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응선", 27, False)