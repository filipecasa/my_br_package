def try_me(num, num_1):

    if type(num) == str or type(num_1) == str:
        return "REASON FOR EXCLUSION"

    return num + num_1

if __name__ == "__main__":
    try_me(2, 2)
