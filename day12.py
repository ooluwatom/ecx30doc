def email(number):
    emails = []
    count = 0
    student_count = 0
    prof_count = 0
    while count in range(number):
        a = input('Please enter email address of student/professor: ')
        emails.append(a)
        count += 1
    for email in emails:
        if '@student.college.edu' in email:
            student_count += 1
        elif '@prof.college.edu' in email:
            prof_count += 1
    return(f'The number of student emails entered is {student_count} and professor emails is {prof_count}')

print(email(3))
