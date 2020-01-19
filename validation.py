def validation(action):
    options = ['-s', '-l', '-i', '-lst']
    if action in options:
        pass
    else:
        print("Enter valid arguments.   (-s, -l, -i, -lst)")
        exit()


