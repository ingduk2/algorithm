def solution(numbers):
    append_list = []
    for num in numbers:
        str_num = str(num)
        if len(str_num) < 3:
            append_str = ''
            for i in range(3):
                append_str += str_num
            append_list.append([append_str, num])
        else:
            append_list.append([str_num, num])
    append_list = sorted(append_list, key=lambda x:x[0], reverse=True)
    print(append_list)
    if append_list[0][1] == 0:
        return "0"
    else:
        return ''.join([str(i[1]) for i in append_list])

numbers = [900,998]
print(solution(numbers))

numbers = [40,403]
print(solution(numbers))

numbers = [10,101]
print(solution(numbers))

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))

numbers = [3, 30, 34, 5, 9, 2, 1]
print(solution(numbers))

numbers = [1, 10, 100]
print(solution(numbers))
# 1101001000

numbers = [91,12,920,1000]
print(solution(numbers))

print(solution([6, 10, 2]),6210)
print(solution([3, 30, 34, 5, 9]),9534330)
print(solution([40,400]), 40400)
print(solution([40,404]), 40440)
print(solution([12,121]), 12121)
print(solution([3054,305]), 3054305)
print(solution([3044,304]), 3044304)
print(solution([340,3403]), 3403403)
print(solution([340,3402]), 3403402)
print(solution([340,3405]), 3405340)
print(solution([40,405]), 40540)
print(solution([40,404]), 40440)
print(solution([40,403]), 40403)
print(solution([40,405]), 40540)
print(solution([40,404]), 40440)
print(solution([50,403]), 50403)
print(solution([50,405]), 50405)
print(solution([50,404]), 50404)
print(solution([30,403]), 40330)
print(solution([30,405]), 40530)
print(solution([30,404]), 40430)
print(solution([12,121]), 12121)
print(solution([2,22,223]), 223222)
print(solution([41,415]), 41541)
print(solution([2,22 ]), 222)
print(solution([70,0,0,0]), 70000)
print(solution([0,0,0,1000]), 1000000)
print(solution([0,0,0,0]),0)
print(solution([0,0,70]),7000)
print(solution([12,1213]), 121312)
print(solution([3, 30, 34, 5, 91]),91534330)
print(solution([3, 30, 34, 5, 191]),534330191)
print(solution([3, 30, 34, 5, 191, 432789]),543278934330191)
print(solution([1,2,3,4,5,44]),5444321)
print(solution([1,2,3,4,5,66]),6654321)
print(solution([3, 30, 31, 5, 9]),9533130)
print(solution([3, 30, 31, 34, 5, 9]),953433130)
print(solution([3, 30, 31, 34, 33, 5, 9]),95343333130)
print(solution([10, 101]),10110)
print(solution([1, 11, 111, 1111]),1111111111)
print(solution([0, 0, 0, 0, 0, 0]),0)

