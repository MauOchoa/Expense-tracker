phrase = "Name not one man"
palabra = phrase.lower()
def isPalindrome(phrase):
    normal_list = []
    reversed_list=[]
    for i in range(len(phrase)):
        #print(phrase[i])
        normal_list.append(phrase[i])
        reversed_list = list(reversed(normal_list))
    for j in range(len(normal_list)):
        if normal_list[j]==reversed_list[j]:
            return True
        else:
            return False
    #print(normal_list, reversed_list)
print(isPalindrome(palabra))