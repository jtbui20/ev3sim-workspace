my_wake_time = ['Wed 1st: 10AM', 'Thu 2nd: 7AM', 'Fri 3rd: 9AM', 'Sat 4th: 6AM', 'Sun 5th: 9AM', 'Mon 6th: 10AM', 'Tue 7th: 7AM', 'Wed 8th: 10AM', 'Thu 9th: 8AM', 'Fri 10th: 7AM', 'Sat 11st: 7AM', 'Sun 12nd: 6AM', 'Mon 13rd: 9AM', 'Tue 14th: 7AM', 'Wed 15th: 10AM', 'Thu 16th: 8AM', 'Fri 17th: 8AM', 'Sat 18th: 9AM', 'Sun 19th: 9AM', 'Mon 20th: 8AM', 'Tue 21st: 7AM', 'Wed 22nd: 8AM', 'Thu 23rd: 7AM', 'Fri 24th: 9AM', 'Sat 25th: 7AM', 'Sun 26th: 10AM', 'Mon 27th: 6AM', 'Tue 28th: 8AM', 'Wed 29th: 10AM', 'Thu 30th: 9AM']

# Your list splice goes here \/\/\/\/\/\/\/
print(my_wake_time[0:10])
print(my_wake_time[20:])
print(my_wake_time[::2])
print(my_wake_time[4::7])
print(list(reversed(my_wake_time)))
print(list(reversed(my_wake_time))[1::7])