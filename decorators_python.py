
def greet(fx):
    def mfx():
        print("GOOD MORNING")
        fx()
        print("DECORATED")
    return mfx

@greet
def hello():
    print("Hello")

hello()
