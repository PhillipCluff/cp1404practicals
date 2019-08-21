# output needs to look like this
#   0
#  50
# 100


def main():
    for i in range(0, 101, 50):
        print("{:>3}".format(i))


main()
