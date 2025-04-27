day = 3
match day:
    case 1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
# output is Tuesday

day = 'Sunday'
match day:
    case 'Sunday':
        print('today is weekend')
    case 'Monday':
        print('today is workday')
# output is "today is weekend"

day = '5'
match day:
    case 'Sunday':
        print('today is weekend')
    case 2:
        print('today is workday')
    case _:
        print('the day is not found')
# output is "the day is not found"
# note: if 'case _' is not added, the program will ouput nothing

# output depends on user input
holiday = input("Input your tagert hodliday:")
match holiday:
    case "New Year Day":
        print("New Year Day is from Jan 1 to Jan 3")
    case "Spring Festival":
        print("Spring Festival is from Jan 21 to Jan 27")
    case "Qing Ming":
        print("Qing Ming is from Apr 4 to Apr 6")
    case _:
        print("Sorry, I don't know this holiday")

# output depends on user input
food = input("请输入你要点的食物（burger / fries / coke / salad）：")
match food:
    case "burger":
        print("您点了汉堡 🍔，价格是 ¥25")
    case "fries":
        print("您点了薯条 🍟，价格是 ¥15")
    case "coke":
        print("您点了可乐 🥤，价格是 ¥10")
    case "salad":
        print("您点了沙拉 🥗，价格是 ¥20")
    case _:
        print("对不起，菜单中没有这个选项 🙁")


# one case have multiple valuse:
testday = input('Please input a day of week(Monday/Tueseday...):')
match testday:
    case 'Monday'|'Tuesday'|'Wednesday'|'Thursday'|'Friday':
        print('today is weekday')
    case 'Sunday'|'Saturday':
        print('today is weekend')
    case _:
        print('This is not a day of week')

# add if statement in case:
month = 5
day = 4
match day:
    case 1|2|3|4|5 if month == 4:
        print('It is a weekday in April')
    case 1|2|3|4|5 if month == 5:
        print('It is a weekday in May')
    case _:
        print('No match')


year = 2025
month = input('Input month(Jan/Feb...):')
match month:
    case 'Jan'|'Feb'|'Mar'|'Apr'|'May'|'Jun' if year==2025:
        print('It is', month, 'in 2025.')
    case 'Jan'|'Feb'|'Mar'|'Apr'|'May'|'Jun' if year==2026:
        print('It is', month, 'in 2026.')
    case _:
        print('Not Found')


# a simple holiday check:
month = input('Input month(Jan/Feb...):')
day = input('Input day(1/2/3...):')
match day:
    case '1' if month == 'Jan':
        print('It is New Year Day')
    case '1' if month == 'May':
        print('It is Labor Day')
    case '1' if month == 'Oct':
        print('It is National Day')
    case _:
        print(month, day, 'is not a holiday')