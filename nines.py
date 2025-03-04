'''
A program to compute the digital root of all multiples of 9.
It consists of a function to compute the digital root of a number, and a loop to iterate through all multiples of 9.
'''

import pandas as pd

def digital_root(n: int) -> int:
    """
    Compute the digital root of a number.

    Args:
        n (int): The number to compute the digital root for.

    Returns:
        int: The digital root of the number.
    """
    while n > 9: # Continue calculating until the nunmber n is a single digit
        n = sum(int(digit) for digit in str(n))  # Sum of digits
    return n

def main() -> None:
    """
    Main function to compute and print the digital root of multiples of 9.
    """
    # Create an empty DataFrame with columns 'Number' and 'Digital Root', and an index named 'Multiple'
    nines = pd.DataFrame(columns=['Multiple', 'Result', 'Digital Root'])

    # Iterate through the multiples of 9
    for i in range(10_000):
        nine_multiple = i * 9
        digital_root_num = digital_root(nine_multiple)
        nines.loc[i] = {'Multiple': i, 'Result': nine_multiple, 'Digital Root': digital_root_num}

        ## uncomment the following line to print progress
        #print(f'{i} * 9 = {nine_multiple}, digital root = {digital_root_num}')
        
    # Remove the first row from the DataFrame
    nines.drop(nines.index[0], inplace=True)
    
    # print the entire DataFrame summary
    print(nines)

if __name__ == "__main__":
    main()


