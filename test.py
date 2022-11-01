def solution(n, arr1, arr2):
    answer = []
    temp_list = []
    for i in range(n):
        b = arr1[i]
        b = bin(b)
        b = b.replace('0b','')
        b = int(b)   

        c = arr2[i]
        c = bin(c)
        c = c.replace('0b','')
        c = int(c)
        sum_text= str(b+c)
        if len(sum_text) < n:
            sum_text = sum_text.rjust(n,'0')
        temp_list.append(sum_text)
    for i in range(len(temp_list)):
        append_text= ''
        for j in range(len(temp_list[i])):
            text1 = temp_list[i][j]
            if int(text1) > 0:
                append_text = append_text + '#'
            else:
                append_text = append_text + ' '
        answer.append(append_text)
    print(answer)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n,arr1,arr2)