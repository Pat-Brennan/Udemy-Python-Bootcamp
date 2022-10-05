
# * Filter!
# ? Syntax: filter(lambda: boolean logic, iterable)

# ? There is a lambda for each value in the iterable
# ? Returns filter object which can be converted into other iterables
# ? The object contains only the values that return true to the lambda
# ? Similar to MAP!

people = ['Danny Devito', 'Captain Planet', 'Doc Oc', 'Chris Pratt']

d_names = list(filter(lambda x: x[0] == 'D', people))
print(d_names)

# * Twitter Example

users = [
    {'username': 'A1hunk', 'tweets': ["I'm hunkalicious!"]},
    {'username': 'Bill_murry', 'tweets': []},
    {'username': 'Jaba49ers', 'tweets': ["Look!", "It's the Jaba!"]},
    {'username': 'Shadow_fall_69', 'tweets': ["I'm going down!"]},
    {'username': 'eeeeee', 'tweets': ['eeeee', 'eeee', 'eeeeeeeee']}
]

# ? Find inactive users with length
inactive_users = list(filter(lambda u: len(u['tweets']) == 0, users))
print(inactive_users)

# ? Find with empty array
inactive_users = list(filter(lambda u: u['tweets'] == [], users))
print(inactive_users)

# ? Those that have tweets are TRUE those do NOT are FALSE
inactive_users = list(filter(lambda u: not u['tweets'], users))
print(inactive_users)

# * Combining Map and Filter

names = ['Jahovah', 'Percy Heath', 'Pat']

usernames = list(map(lambda user: user['username'].upper(),
                      filter(lambda u: not u['tweets'], users)))
print(usernames)

# * Why not just use list comprehension?

bad_users = [
    f'The users that have not tweeted are... {user}' for user in users if not user['tweets']]
print(bad_users)
