def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some processing using f ...
            pass #The file will automatically be closed when exiting this 'with' block.
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None # Handle file not found error