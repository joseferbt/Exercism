def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    calculo = 0
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    else :
        for i in range(1,number):
            if number % i == 0 :
                calculo += i
        if calculo == number:
            return "perfect"
        elif calculo < number:
            return "deficient"
        else : return "abundant"