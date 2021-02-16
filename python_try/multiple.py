def multiple(data):
    if data <= 1:
        return data
    else:
        return data * multiple(data -1)

print(multiple(5))