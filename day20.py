import time
user_value = str(input("Enter the THREE time values in order xs, xm, xh:\n"))
def countdown(ti):
    (seconds, minutes, hours) = ti
    h = 0
    if seconds[-1] == 's':
        s = int(seconds[:-1])
    else:
        print('Invalid Seconds value')
        return
    if minutes[-1] == 'm':
        m = int(minutes[:-1])
    else:
        print('Invalid Minutes Value')
        return
    if hours[-1] == 'h':
        h = int(hours[:-1])
    else:
        print('Invalid Hours value')
        return
    # if h > 0:
    #     m = (h * 60) + m
    def real_countdown(h, m, s):
        t = s + (m *60) + (h * 3600)
        while t:
            hours = t//3600
            mins, secs = divmod(t - (hours*3600), 60)
            # hours, mins = divmod(t, 60)
            # m, secs = divmod(t, 3600)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print('Fire in the hole!!')   

    real_countdown(h,m,s)

t_string = user_value.split(', ')
countdown(t_string)
