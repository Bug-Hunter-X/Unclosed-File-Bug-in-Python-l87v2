def function_with_unclosed_file(filename):
    f = open(filename, 'r')
    # ... some processing using f ...
    return  # Forgot to close the file