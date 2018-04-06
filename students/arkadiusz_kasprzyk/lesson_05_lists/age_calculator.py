<<<<<<< HEAD
def age_calculator(ages):
    """
    Parameters
    ----------
    ll: int[]
        list of ages of people in a group

    Returns
    -------
    mean age of adults (>=18) and number of kids (<18)

    Examples
    --------
    ages = [18, 2, 24, 8, 9]
    print(age_calculator(ages))
    """
    adults = [l for l in ages if l >= 18]
    adults_mean = sum(adults)/len(adults)
    kids = [l for l in ages if l <18]
    kids_number = len(kids)
    return adults_mean, kids_number
=======
def age_calculator(ll):
    adults = [l for l in ll if l >= 18]
    adults_mean = sum(adults)/len(adults)
    kids = [l for l in ll if l <18]
    kids_number = len(kids)
    return adults_mean, kids_number

#ll = [5,2,1,4]
#sum(ll)/len(ll)

ll = [18, 2, 24, 8, 9]
print(age_calculator(ll))
>>>>>>> 00 adziu/lesson_05_lists
