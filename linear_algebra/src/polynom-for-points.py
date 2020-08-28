def points_to_polynomial(coordinates):
    """
    coordinates is a two dimensional matrix: [[x, y], [x, y], ...]
    number of points you want to use

    >>> print(points_to_polynomial([]))
    The program cannot work out a fitting polynomial.
    >>> print(points_to_polynomial([[]]))
    The program cannot work out a fitting polynomial.
    >>> print(points_to_polynomial([[1, 0], [2, 0], [3, 0]]))
    f(x)=x^2*0.0+x^1*-0.0+x^0*0.0
    >>> print(points_to_polynomial([[1, 1], [2, 1], [3, 1]]))
    f(x)=x^2*0.0+x^1*-0.0+x^0*1.0
    >>> print(points_to_polynomial([[1, 3], [2, 3], [3, 3]]))
    f(x)=x^2*0.0+x^1*-0.0+x^0*3.0
    >>> print(points_to_polynomial([[1, 1], [2, 2], [3, 3]]))
    f(x)=x^2*0.0+x^1*1.0+x^0*0.0
    >>> print(points_to_polynomial([[1, 1], [2, 4], [3, 9]]))
    f(x)=x^2*1.0+x^1*-0.0+x^0*0.0
    >>> print(points_to_polynomial([[1, 3], [2, 6], [3, 11]]))
    f(x)=x^2*1.0+x^1*-0.0+x^0*2.0
    >>> print(points_to_polynomial([[1, -3], [2, -6], [3, -11]]))
    f(x)=x^2*-1.0+x^1*-0.0+x^0*-2.0
    >>> print(points_to_polynomial([[1, 5], [2, 2], [3, 9]]))
    f(x)=x^2*5.0+x^1*-18.0+x^0*18.0
    """
    try:
        check = 1
        more_check = 0
        d = coordinates[0][0]
        for j in range(len(coordinates)):
            if j == 0:
                continue
            if d == coordinates[j][0]:
                more_check += 1
                solved = "x=" + str(coordinates[j][0])
                if more_check == len(coordinates) - 1:
                    check = 2
                    break
                elif more_check > 0:
                    check = 3
                else:
                    check = 1

        if len(coordinates) == 1 and d == 0:
            check = 2
            solved = "x=0"
    except Exception:
        check = 3

    if check == 1:
        matrix = []
        x = len(coordinates)

        # put the x and x to the power values in a matrix
        for count_of_line in range(x):
            a = coordinates[count_of_line][0]
            count_line = [a ** (x - (count_in_line + 1)) for count_in_line in range(x)]
            matrix.append(count_line)
        # put the y values into a vector
        vector = [coordinates[count_of_line][1] for count_of_line in range(x)]
        count = 0

        while count < x:
            zahlen = 0
            while zahlen < x:
                if count == zahlen:
                    zahlen += 1
                if zahlen == x:
                    break
                bruch = (matrix[zahlen][count]) / (matrix[count][count])
                for counting_columns, item in enumerate(matrix[count]):
                    # manipulating all the values in the matrix
                    matrix[zahlen][counting_columns] -= item * bruch
                # manipulating the values in the vector
                vector[zahlen] -= vector[count] * bruch
                zahlen += 1
            count += 1

        count = 0
        # make solutions
        solution = []
        while count < x:
            solution.append(vector[count] / matrix[count][count])
            count += 1

        solved = "f(x)="

        for count in range(x):
            remove_e = str(solution[count]).split("E")
            if len(remove_e) > 1:
                solution[count] = remove_e[0] + "*10^" + remove_e[1]
            solved += "x^" + str(x - (count + 1)) + "*" + str(solution[count])
            if count + 1 != x:
                solved += "+"
        return solved

    elif check == 2:
        return solved
    else:
        return "The program cannot work out a fitting polynomial."


if __name__ == "__main__":
    print(points_to_polynomial([]))
    print(points_to_polynomial([[]]))
    print(points_to_polynomial([[1, 0], [2, 0], [3, 0]]))
    print(points_to_polynomial([[1, 1], [2, 1], [3, 1]]))
    print(points_to_polynomial([[1, 3], [2, 3], [3, 3]]))
    print(points_to_polynomial([[1, 1], [2, 2], [3, 3]]))
    print(points_to_polynomial([[1, 1], [2, 4], [3, 9]]))
    print(points_to_polynomial([[1, 3], [2, 6], [3, 11]]))
    print(points_to_polynomial([[1, -3], [2, -6], [3, -11]]))
    print(points_to_polynomial([[1, 5], [2, 2], [3, 9]]))
