with open("temp.txt") as f:
    prev_line = ''
    for line in f:
        if line.find('title')!=-1:
            print (last_two)
        last_two = prev_line
        prev_line = line
