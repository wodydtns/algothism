from posixpath import split


def solution(files):
    answer = []
    swap_dict = {}
    for file in files:
        swap_key = file.split('.')[0]
        swap_dict[swap_key] = file
        answer.append(swap_key)
    for i in answer:
        for j in range(len(answer)):
            standard_val = answer[i].isupper()
            compare_val = answer[j].isupper()
            # TODO text를 짤라서 확인
            if compare_val != standard_val:
                print('tte')
            else:
                continue
    return answer


# TODO case 1
files = ["img12.png", "img10.png", "img02.png",
         "img1.png", "IMG01.GIF", "img2.JPG"]
solution(files)

# TODO case 2
#files =["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# solution(files)
