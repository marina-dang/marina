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

        