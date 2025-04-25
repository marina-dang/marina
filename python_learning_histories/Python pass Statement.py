'''Python pass Statement'''
def handle_error(http_code_status):
    if http_code_status == 200:
        print("Successful Request")
    elif http_code_status == 400:
        print("Can't be found")
    elif http_code_status == 500:
        pass   # Temporarily ignore 500 err
    elif http_code_status -- 401:
        print("No access")
    else:
        print("unknown error")
handle_error(200)
handle_error(400)
handle_error(500)
handle_error(401)
'''Output is like below:'''
'''Successful Request'''
'''Can't be found'''
'''No access'''

################################
################################
def result(your_input):
    if isinstance(your_input, str):
        print("Your input is a string.")
    elif isinstance(your_input, int):
        print("Your input is an integer.")
    else:
        print("Your input is neither a string nor an integer.")
result("hello")
result(123)
result(int)
# Output are like below:
# Your input is a string.
# Your input is an integer.
# Your input is neither a string nor an integer.
################################
################################
