
with open('test.txt', 'r') as reader :
    content = reader.readlines()
    print(content)
    reversed(content)
    with open('test.txt' , 'w') as writer :
        for line in reversed(content):
            writer.write(line)