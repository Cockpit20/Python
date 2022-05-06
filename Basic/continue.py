while True:
    line =input('>>> ')
    if line[0]=='#':
        continue
    # goes back to the while condition
    if line=='done':
        break
    # breaks out of the while loop
    print(line)
print('Done!')

