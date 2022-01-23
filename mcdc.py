# created by kestar hacker ( arouche ayoub )

import ast
from typing import final

import itertools

from numpy import array

# get all the variable names in the expression : 
generale_result = []


def get_variables(expression):
    variables = [node.id  for node in ast.walk(ast.parse(formula))
             if isinstance(node , ast.Name)
             ]
    variables = list(dict.fromkeys(variables))
    return variables 
# assign values to variables function 
def assign_values_to_variables(names_of_variables , values ):
    all_variables_with_values = {}
    for i in range(len(names_of_variables)) : 
        all_variables_with_values[names_of_variables[i]] = values[i]
    return all_variables_with_values
# evaluate an expression
def evaluate_expression (expression):
    return eval(expression)

# to generate all the test cases to test i used the branch and bound algorithme : 
def generate_all_test_cases(length , current_variable , result):
    if current_variable == length:
        
        generale_result.append(result)
    else : 
        adding_true_value_to_result = result.copy()
        adding_true_value_to_result.append(True)
        generate_all_test_cases(length , current_variable+1 , adding_true_value_to_result) 
        adding_false_value_to_result = result.copy()
        adding_false_value_to_result.append(False)
        generate_all_test_cases(length , current_variable+1 , adding_false_value_to_result)
    
def create_variables_dynamiqually(variabels_with_associated_value):
    for variable in variabels_with_associated_value :
            globals()[variable] = variabels_with_associated_value[variable]
    return 

def get_same_test_case(all_the_test_cases  , test_case , variable_to_change ):
    same_test_cases = []
    same_test_cases.append(test_case.copy())
    test_case[variable_to_change] = not test_case[variable_to_change]
    test_case['result'] = not test_case['result']
    for current_test_case in all_the_test_cases :
        if current_test_case == test_case :
            same_test_cases.append(current_test_case.copy())
    return same_test_cases
            
            
def remove_duplicate_valid_test_cases (valid_test_cases_of_all_variabels):
    final_test_cases = []
    merged_test_cases = []
    for valid_test_case in valid_test_cases_of_all_variabels:
        # for each variable : 
        result  = list(itertools.chain.from_iterable(valid_test_case)) # merge all the test cases :
        print("inside the merging algorithm : ")
        
        result = remove_duplicates_from_list(result)
        merged_test_cases.append(result)
        print(result)
    return merged_test_cases

def remove_duplicates_from_list(test_cases):
    result = []
    for test_case in test_cases :
        if test_case not in result :
            result.append(test_case)
    return result
def get_mcdc(valid_test_cases) :
    mcdcs = []
    test_cases = remove_duplicate_valid_test_cases(valid_test_cases)
    
    for i in range(len(valid_test_cases)) :
        for j in range(len(test_cases)):
            if(i==j):
                continue
            test_cases2 = [x for x in test_cases[i] if x in test_cases[j]]
        print("the value is : ")
        print(test_cases2)
        mcdcs.append(test_cases2)
    return mcdcs   
    
def check_if_exist(test_case , test_cases):
    return (test_case in test_cases)
# def generate_lests_from_dict(dict):
#     result = []
#     result.append(dict)
#     result.append(dict[])
if __name__ == "__main__":
    all_test_cases_with_results = []
    formula = 'a & (b | c)'
    variables = get_variables(formula)
    print(variables)
    print(len(variables))
    # generating all the test cases that we should do 
    generate_all_test_cases(len(variables) , 0 , [])
    
    # now we will calculate the results of these test cases : 
    for test_case in generale_result:
        result = {}
        result = assign_values_to_variables(variables , test_case)
        create_variables_dynamiqually(result)
        result["result"] = evaluate_expression(formula)
        result_copy = result.copy()
        #print(result_copy)
        all_test_cases_with_results.append(result)
    general_valid_test_cases_for_each_variable = []
    print("before the values : ")
    for variable in variables :
        general_valid_test_cases_for_a_variable = []
        general_valid_test_cases_result = []
        print("for variable "+ variable)
        for test_case in all_test_cases_with_results :
            valid_opposite_test_case = get_same_test_case(all_test_cases_with_results  , test_case.copy() , variable)
            if len(valid_opposite_test_case) == 1 : 
                continue
            general_valid_test_cases_for_a_variable.append(valid_opposite_test_case)
            print(valid_opposite_test_case)
        general_valid_test_cases_result = general_valid_test_cases_for_a_variable[0:int(len(general_valid_test_cases_for_a_variable)/2)]
        general_valid_test_cases_for_each_variable.append(general_valid_test_cases_result.copy())
    
        print("the size is : "+str(len(general_valid_test_cases_result)))
        print("==========================================================")
        print(general_valid_test_cases_result)
        print("==================================================")
    # print("after the values : ")
    # print(len(general_valid_test_cases_for_a_variable))

    # print("after remving test cases : ")
    # print(len(general_valid_test_cases_for_a_variable))
    final_test_cases = []
    print("the general values is : ")
    print(general_valid_test_cases_for_each_variable)
    # final_result = remove_duplicate_valid_test_cases (general_valid_test_cases_for_a_variable)
    
    print("getting mcdcs : ")
    length = len(general_valid_test_cases_for_each_variable)
    for i in range(length) :
        variable_test_cases  = general_valid_test_cases_for_each_variable[i]
        for j in range(len(variable_test_cases)):
            for k in range(2) :
                ## algo katchof ila kan 4ir wahd element mn l pair f test cases lakhrin kat2ajoutihom bjoj o kadoz l variable lakher
                	
        
    
    # for valid_cases_for_variable in general_valid_test_cases_for_each_variable:
    #     print("for a variable : ")
    #     print(valid_cases_for_variable)    
    # print("the final result is : ")
    # print("the lenght is "+ str(len(final_result)))
    # for test_case in final_result :
    #     print(test_case)
   # print()
    ## applicating the mcdc of our test cases : 
    
    # assign_values_to_variables(variables , values)
    # result = evaluate_expression(formula)
    # print("result is :  "+str(result))
    # for i in variables :
    #     print("the variable name is : " +str(i))
    
    # range = locals()
    # for i in range :
    #     print("the local name is : "+locals[])
    # print(names)
    # locals()['k'] = 3
    # y = function_expression(k ,2)
    # print("the value of is y is : "+str(y))
