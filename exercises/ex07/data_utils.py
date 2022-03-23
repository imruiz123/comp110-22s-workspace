"""Dictionary related utility functions."""

__author__ = "730335383"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]: 
    """Read the rows of csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file 
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings 
    csv_reader = DictReader(file_handle) 

    # Read each row of the CSV line-by-line 
    for row in csv_reader: 
        result.append(row) 

    # Close the file when we're done, to free its resources. 
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = [] 
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column) 

    return result 


def head(first_n: dict[str, list[str]], second_n: int) -> dict[str, list[str]]:
    """So we are doing something. """
    result: dict[str, list[str]] = {}
    for column in first_n: 
        whatever: list[str] = []
        other = 0 
        if len(first_n[column]) < second_n:
            result[column] = first_n[column] 
        else: 
            while other < second_n: 
                whatever.append(first_n[column][other])
                other += 1 
        result[column] = whatever
    return result


def select(first_k: dict[str, list[str]], second_k: list[str]) -> dict[str, list[str]]: 
    """Something else is happening."""
    k_whatever: dict[str, list[str]] = {}
    for column in second_k:
        k_whatever[column] = first_k[column]
        
    return k_whatever 


def concat(first_c: dict[str, list[str]], second_c: dict[str, list[str]]) -> dict[str, list[str]]:
    """Some other shit."""
    c_whatever: dict[str, list[str]] = {}
    for column in first_c:
        c_whatever[column] = first_c[column]
    
    return c_whatever 


def count(last_t: list[str]) -> dict[str, int]:
    """Last one purr."""
    last_r: dict[str, int] = {}
    for item in last_t: 
        if item not in last_r:  
            last_r[item] = 1 
        else: 
            last_r[item] += 1 
    return last_r 