patron = input('Patron?')

if patron == 'full':
    waitestimate = float(input('waitestimate?'))
    if waitestimate >= 0 and waitestimate <= 10:
        print ('yes')
    elif waitestimate > 10 and waitestimate <= 30:
        hungry = input ('hungry?')
        if hungry == 'yes':
            alternate = input('alternate?')
            if alternate == 'yes':
                raining = input('raining?')
                if raining == 'yes':
                    print('yes')
                elif raining == 'no':
                    print ('no')
            elif alternate == 'no':
                print ('yes')
        elif hungry == 'no':
            print ('yes')
    elif waitestimate > 30 and waitestimate <= 60:
        alternate = input('alternate?')
        if alternate == 'yes':
            print ('Fri/Sat?')
            Fri_Sat = input('Fri/Sat?')
            if Fri_sat == 'yes':
                print('yes')
            elif Fri_sat == 'no':
                print ('no')
        elif alternate == 'no':
            reservation = input('reservation?')
            if reservation == 'yes':
                print ('yes')
            elif reservation == 'no':
                bar = input('bar?')
                if bar == 'yes':
                    print('yes')
                elif bar == 'no':
                    print ('no')
    elif waitestimate > 60:
        print ('no')
    else:
        print ('wrong number')
elif patron == 'some':
    print ('yes')
elif patron == 'none':
    print ('no')


