from tenacity import retry_unless_exception_type


def try_me(size = "M") :
    """ Test module"""
    return f"Your size is {size} "

if __name__ == "__main__":
    new_size = 'L'
    print(try_me(new_size))
