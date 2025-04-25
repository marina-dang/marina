import sys

try:
      english_score=int(input("Enter your English score: "))
      if (english_score < 0 or english_score > 100):
            print("Score is invalid.")
            exit(1)
except ValueError:
      print("Score is invalid.")
      exit(1)
try:
      math_score=int(input("Enter your Math score: "))
      if (math_score < 0 or math_score >100):
            print("Score is invalid.")
            exit(1)
except ValueError:
      print("Score is invalid.")
      exit(1)
try:
      chinese_score=int(input("Enter your Chinese score: "))
      if (chinese_score < 0 or chinese_score > 100):
            print("Score is invalid.")
            exit(1)
except ValueError:
      print("Score is invalid.")
      exit(1)
else:
      if english_score >= 60 and math_score >= 60 and chinese_score >= 60:
            print("Congratulations! You have passed your exam.")
      else:
            print("Sorry, you have failed your exam.")

