english_score=int(input("Enter your English score: "))
math_score=int(input("Enter your Math score: "))
chinese_score=int(input("Enter your Chinese score: "))
total_score = sum([english_score, math_score, chinese_score])
if total_score>=180:
      print("Congratulations! You have passed your exam.")
else:
      print("Sorry, you have failed your exam.")