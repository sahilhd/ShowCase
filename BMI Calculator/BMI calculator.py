print('Welcome to my BMI scanner and workout planner')
print('Are you ready?')
answer = str(input())
if answer == 'yes':
    print('lets get some measurements!')
    print('what is your height in meters?')
    height = float(input())
    print('what is your weight in Kg?')
    weight = float(input())
    chest = ['bench press', 'incline press', 'cable flies']
    legs = ['squats', 'leg press', 'lunges', 'deadlifts']
    back = ['bent over rows', 'lat pull downs', 'pull-ups', 'reverse flys']
    arms = ['barbell curls', 'tricep push-downs', 'hammer curles', 'tricep dips']

    BMI = weight / (height ** 2)
    print(BMI)

    if (3 < BMI < 18.5):
        print('you are underweight, but beautfiul')
        print('A caloric Surplus is recomended')
        print('how many calories do you intake?')
        calorie = int(input())
        goalc = str(calorie + 500)
        print('aim for ' + goalc + ' calories!')
        print('train for 6-8 heavy reps for 5 sets')
        print('What muscle group are you planning to workout today?')
        plan = str(input())
        print('do this')
        if plan == 'chest':
            print(chest)
        if plan == 'arms':
            print(arms)
        if plan == 'legs':
            print(legs)
        if plan == 'back':
            print(back)
    if 18.5 <= BMI <= 25:
        print('you are normal and healthy!')
    if BMI > 25.1:
        print('you are overweight and beautiful')
        print('A caloric defict is recomended')
        print('how many calories do you intake? ')
        calorie = int(input())
        goalc = str(calorie - 500)
        print('aim for ' + goalc + ' calories!')
        print('train for 8-12 moderate reps for 5 sets')
        print('What muscle group are you planning to workout today?')
        plan = str(input())
        print('do this')
        if plan == 'chest':
            print(chest)
        if plan == 'legs':
            print(legs)
        if plan == 'back':
            print(back)
        if plan == 'arms':
            print(arms)
    if BMI < 1:
        print('double check if your measurements are inputed correctly')


else:
    print('Come back when you are ready!')