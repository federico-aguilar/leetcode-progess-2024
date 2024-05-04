
def valid_palindrome(s):
    s = "".join([char.lower() for char in s if char.isalnum()])
    front = 0
    back = len(s) - 1

    while front <= back:
        if s[front] != s[back]:
            return False
        front += 1
        back -= 1
    return True


if __name__ == "__main__":
    print(valid_palindrome(" "))
