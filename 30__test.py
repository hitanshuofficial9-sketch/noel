str = "Welcome to the world of python"
str = str + " "
a  = 0
words = []
for i in range(0, len(str)):
    if str[i] == " ":
        temp = str[a:i]
        words.append(temp)
        a = i+1
long = 0
for i in words:
    if len(i)>long:
        long = len(i)
        long_word = i
print(long_word)