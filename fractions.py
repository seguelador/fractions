input_example = "(5/6 + -4/8) * (9/5 - (12/5 * 6/4))"

def main(input):
    input_str = input.split("")
    operacion = ""
    if operacion == "+":
        sum_fractions(fraction1, fraction2)
    elif operacion == "-":
        substract_fractions(fraction1, fraction2)
    elif operacion ==  "*":
        multiply_fractions(fraction1, fraction2)
    elif operacion ==  "/":
        divide_fractions(fraction1, fraction2)
    else:
        print("Operation not valid")


def sum_fractions(fraction1, fraction2):
    numerator1           = fraction1[0]
    denominator1         = fraction1[1]
    numerator2           = fraction2[0]
    denominator2         = fraction2[1]
    common_denominator   = least_common_multiple(denominator1, denominator2)
    numerator1_amplified = numerator1 * denominator2
    numerator2_amplified = numerator2 * denominator1
    numerator_sum        = numerator1_amplified + numerator2_amplified
    result               = simplify_fraction(numerator_sum, common_denominator)
    return result

def substract_fractions(fraction1, fraction2):
    numerator1           = fraction1[0]
    denominator1         = fraction1[1]
    numerator2           = fraction2[0]
    denominator2         = fraction2[1]
    common_denominator   = least_common_multiple(denominator1, denominator2)
    numerator1_amplified = numerator1 * denominator2
    numerator2_amplified = numerator2 * denominator1
    numerator_sum        = numerator1_amplified - numerator2_amplified
    result               = simplify_fraction(numerator_sum, common_denominator)
    return result

def multiply_fractions(fraction1, fraction2):
    numerator1   = fraction1[0]
    denominator1 = fraction1[1]
    numerator2   = fraction2[0]
    denominator2 = fraction2[1]
    numerator    = numerator1 * numerator2
    denominator  = denominator1 * denominator2
    result       = simplify_fraction(numerator, denominator)
    return result


def divide_fractions(fraction1, fraction2):
    numerator1   = fraction1[0]
    denominator1 = fraction1[1]
    numerator2   = fraction2[0]
    denominator2 = fraction2[1]
    numerator    = numerator1 * denominator2
    denominator  = denominator1 * numerator2
    result       = simplify_fraction(numerator, denominator)
    return result

# Aux functions

def print_step(step):
    print(step)

def simplify_fraction(numerator, denominator):
    maximum     = max(numerator, denominator)
    maximum_aux = maximum
    while maximum_aux > 0:
        if (numerator % maximum_aux == 0) and (denominator % maximum_aux == 0) and (maximum_aux != 1):
            numerator   = numerator / maximum_aux
            denominator = denominator / maximum_aux
        else:
            maximum_aux = maximum_aux - 1

    return int(numerator), int(denominator)

def least_common_multiple(denominator1, denominator2):
    return denominator1 * denominator2

    


print(divide_fractions([1, 4], [1, 5]))
