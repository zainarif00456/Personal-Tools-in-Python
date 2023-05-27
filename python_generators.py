def my_gen():
    for i in range(300):
        print(i)
        yield i


if __name__ == '__main__':
    gen = my_gen()
    next(gen)
    next(gen)
    next(gen)
    next(gen)
