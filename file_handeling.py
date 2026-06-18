f = open("test.text",'w')
f.write('hello abhishek')
f.close()
print("file created")


f = open('test.text','r')
constant = f.read()
print(constant)
f.close()

f = open('test.txt','a')
f.write('\n new line added')
f.close()
print("data added")