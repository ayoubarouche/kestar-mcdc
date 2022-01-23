# created by kestar hacker ( arouche ayoub )

import ast
from typing import final




# get all the variable names in the expression : 
generale_result = []


def get_variables(expression):
    variables = [node.id  for node in ast.walk(ast.parse(expression))
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
            
            

def remove_duplicates_from_list(test_cases):
    result = []
    for test_case in test_cases :
        if test_case not in result :
            result.append(test_case)
    return result

def verify_and_add_test_case(test_cases) :
    final_test_cases = []
    length_test_varibles = len(test_cases)
    i = 0
    check = False
    for i in range(length_test_varibles) :
        check=True

        for part in test_cases[i] :
            
                for k in range(i , length_test_varibles-1):
                    if check and verify_one_of_two_test_cases_already_exist(part , test_cases[k+1]):
                        final_test_cases.append(part)
                        check=False
                    
    
    # last_test_cases_to_add = check_if_a_variable_contains_two_of_test_cases(final_result , test_cases[length_test_varibles-1])

    final_test_cases.append(test_cases[length_test_varibles-1][0])
    final_result = remove_duplicates_from_list(change_from_nested_lists_to_one_list(final_test_cases))
    return final_result

def check_if_a_variable_contains_two_of_test_cases(test_cases_to_verify , variable_test_case):
    for i in range(len(test_cases_to_verify)):
        for j in range(i , len(test_cases_to_verify)-1):
            for test_cases_part in variable_test_case :
                if test_cases_part == [test_cases_to_verify[i] , test_cases_to_verify[j+1]]:
                    return  [test_cases_to_verify[i] , test_cases_to_verify[j+1]]
    return []
            
def verify_one_of_two_test_cases_already_exist(pair_of_test_cases , test_cases_to_verify):
    first_test_case = pair_of_test_cases[0]
    secand_test_case = pair_of_test_cases[1]
    # verify for the first transaction  : 

    for test_cases_to_verify_part in test_cases_to_verify :
        if check_if_exist(first_test_case,test_cases_to_verify_part) :
            return True
    for test_cases_to_verify_part in test_cases_to_verify :
        if check_if_exist(secand_test_case,test_cases_to_verify_part) : 
            return True
   
    return False

def formating_output(test_cases , variabels):
    print("number      ", end="")
    for variable in variabels :
        print(variable+"          " , end="")
    print("result")
    print("-----------------------------------------")
    for test_case in test_cases :
        print(all_test_cases_with_results_with_id[str(test_case)],end="           ")
        for variable in variables :
            print(str(test_case[variable])+"     " , end="")
        print(test_case["result"])
        print("--------------------------------------------")    
def check_if_exist(test_case , test_cases):
    for test_case_part in test_cases : 
        if test_case==test_case_part:
            return True
    return False

def change_from_nested_lists_to_one_list(list):
    final_tests = []
    for test_case in list :
        for nested_test_case in test_case :
            final_tests.append(nested_test_case)
    return final_tests
if __name__ == "__main__":
    all_test_cases_with_results = []
    
    formula = input("entrer une expression :")
    formula = formula.replace('&&', ' and ').replace('||', ' or ').replace('!', ' not ')
    variables = get_variables(formula)
    print("les test case names sont : ",end="")
    print(variables)

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
    all_test_cases_with_results_with_id={}
    id= 1 
    for test_case in all_test_cases_with_results :
        all_test_cases_with_results_with_id[str(test_case)] = id
        id+=1
    general_valid_test_cases_for_each_variable = []
   
    for variable in variables :
        general_valid_test_cases_for_a_variable = []
        general_valid_test_cases_result = []
        
        for test_case in all_test_cases_with_results :
            valid_opposite_test_case = get_same_test_case(all_test_cases_with_results  , test_case.copy() , variable)
            if len(valid_opposite_test_case) == 1 : 
                continue
            general_valid_test_cases_for_a_variable.append(valid_opposite_test_case)
        general_valid_test_cases_result = general_valid_test_cases_for_a_variable[0:int(len(general_valid_test_cases_for_a_variable)/2)]   
        general_valid_test_cases_for_each_variable.append(general_valid_test_cases_result.copy())
    
    final_test_cases = []

   
    
    print("all the test cases with out MC/CD are : ")
    
    formating_output(all_test_cases_with_results , variables)
    print("general test cases for each variable : ")
    for i in range(len(general_valid_test_cases_for_each_variable)):
        print("for variable : "+variables[i])
        for j in range(len(general_valid_test_cases_for_each_variable[i])):
            print("the part number : "+ str(j+1))
            formating_output(general_valid_test_cases_for_each_variable[i][j] , variables)
    print("all the test cases or MC/CD are : ")
    
    final_result = verify_and_add_test_case(general_valid_test_cases_for_each_variable)
    
    formating_output(final_result , variables)
    