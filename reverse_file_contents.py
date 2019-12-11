#Like BASH begin with the shabang #!
#!/usr/bin/env python3

with open('test.txt', "r") as openfile:
    with open('copy_' + 'test1.txt', "w") as outfile:
        for line in openfile:
            outfile.write(line[::-1])
