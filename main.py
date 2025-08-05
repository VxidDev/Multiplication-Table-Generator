while True:
    try:
        number = int(input('Input a number: '))
        if number > 10 or number < 1:
            raise ValueError()
        break
    except ValueError:
        print('Input must be a number from 1 to 10!')

multiplication = 0

for i in range(1 , 11):
    multiplication += 1
    print(f"{number} * {multiplication} = {number * multiplication}")
