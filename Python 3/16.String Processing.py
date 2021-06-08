# 21.06.08
# 짝수번째 대문자 문자열
def function_solution(variable_s):
    variable_answer = ''
    variable_s_list = list(variable_s).copy()
    for i in range(len(variable_s)):
        if i % 2 == 0:
            variable_s_list[i] = variable_s_list[i].upper()
        else:
            variable_s_list[i] = variable_s_list[i].lower()
    variable_answer = "".join(variable_s_list)
    return variable_answer

function_ex = "try hello world"
print(function_solution(function_ex))