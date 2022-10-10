
# * zip()
# ? Make an iterator that aggregates elements from each of the iterables
# ? Returns an iterator of tuples, where the i-th tuple contains the i-th element
# ? from each of the argument sequences or iterables.
# ? The iterator stops when the shortest input iterable is exhausted.

first_zip = zip([1, 2, 3], [4, 5, 6])
print(first_zip)  # prints a ZIP OBJECT

print(list(first_zip))  # [(1, 4), (2, 5), (3, 6)]

print(dict(first_zip))  # {1: 4, 2: 5, 3: 6}

# * Student Grades Example

midterms = [89, 45, 72]
finals = [100, 101, 94]
students = ['bob', ' bibo', 'chad']

# ? List Comprehension Solution
final_grades = [max(pair) for pair in zip(midterms, finals)]
student_grades = dict(zip(students, final_grades))
print(student_grades)

# ? Dictionary Comprehension Solution
final_grades2 = {pair[0]: max(pair[1], pair[2])
                 for pair in zip(students, midterms, finals)}
print(final_grades2)


# ? Map / Lambda Solution
final_grades_3 = zip(
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)
print(dict(final_grades_3))
