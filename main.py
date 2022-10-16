def is_palindromic(number):
    number_str = str(number)
    number_str_reversed = number_str[::-1]

    return number_str == number_str_reversed


print(is_palindromic(5))
print(is_palindromic(20))
print(is_palindromic(55))
print(is_palindromic(515))
print(is_palindromic(12344321))
