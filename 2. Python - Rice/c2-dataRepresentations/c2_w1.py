# Concacenating strings .format()

country = "Poland"
city = "Wroclaw"
street = "Hallera"
building = "100"
flat = "14"

print("Country: {}, city: {}, street: {}, building: {},\
 flat: {}".format(country,city,street,building,flat))

print("{0} mieszkam w {0}, mieszkam w {0}, mieszkam tu tu tu: {1}".format(country, city))
print("----\n")

name1 = "Sanpierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:<15} {1:<5}".format(name1, age1)
# ^ centered
# < left aligned
# > right aligned
line2 = "{0:^15} {1:>5}".format(name2, age2)
print(line1)
print(line2)

print("----\n")

num = 3.283663293
output = "{0:<10.5f} {0:.2f}".format(num)
print(output)


def echo(call, repeats):
    """
    Echo the string call to the console repeats number of time
    Each echo should be on a separate line
    """
    for i in repeats:
        print(call)


# Tests
echo("Hello", 5)
echo("Goodbye", 3)