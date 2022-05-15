def climber(depth):
    height = 0
    days = 0
    while height < depth:
        if (height + 8) >= depth:
            days += 1
            break
        else:
            days += 1
            height += 8-2
    print('Number of days to the top is: {} days'.format(days))

climber(17)