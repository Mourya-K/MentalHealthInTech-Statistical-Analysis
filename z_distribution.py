def get_Z_TAB(significance_level, side):
    # Define the Z-table values
    z_table = {
        0.01: {'two_sided': 2.576, 'one_sided': 2.326},
        0.05: {'two_sided': 1.960, 'one_sided': 1.645},
        0.10: {'two_sided': 1.645, 'one_sided': 1.282}
    }

    # Check if the significance level is in the table
    if significance_level in z_table:
        # Check if the side is valid
        if side in ['two_sided', 'one_sided']:
            return z_table[significance_level][side]
        else:
            raise ValueError("Invalid side. Use 'two_sided' or 'one_sided'.")
    else:
        raise ValueError("Invalid significance level. Use 0.01, 0.05, or 0.10.")
