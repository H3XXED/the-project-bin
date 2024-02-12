def calculate_bonus(employee_level, sales_total):
    """
    This function computes the bonus of an employee based on
    the employee's level and their sales total

    :param employee_level: int, 1-3
    :param sales_total: float
    :return: float
    """

    # employee level 3
    if employee_level == 3:
        if sales_total > 10000:
            bonus = sales_total * 0.15
        else:
            bonus = sales_total * 0.075

    # employee level 2
    elif employee_level == 2:
        if sales_total > 10000:
            bonus = sales_total * 0.1
        else:
            bonus = sales_total * 0.05

    # employee level 1 (otherwise)
    else:
        if sales_total > 10000:
            bonus = sales_total * 0.05
        else:
            bonus = sales_total * 0.025
    return bonus



