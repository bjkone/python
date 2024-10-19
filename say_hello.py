def manage_types():
    s = "hello world"
    print(f" s is of type {type(s)} and has value {s}")
    i = 15
    print(f" i is of type {type(i)} and has value {i}")
    f = 5.5
    print(f" f is of type {type(f)} and has value {f}")
    b = True
    print(f" b is of type {type(b)} and has value {b}")
    l = [1, 2, 3]
    print(f" l is of type {type(l)} and has value {l}")
    d = {"a": 1, "b": 2}
    print(f" d is of type {type(d)} and has value {d}")
    t = (1, 2, 3)
    print(f" t is of type {type(t)} and has value {t}")
    e = {1, 2, 3}
    print(f" e is of type {type(e)} and has value {e}")
    g = frozenset({1, 2, 3})
    print(f" g is of type {type(g)} and has value {g}")
    m = memoryview(b"hello")
    print(f" m is of type {type(m)} and has value {m}")
    a = bytearray(b"hello")
    print(f" a is of type {type(a)} and has value {a}")
    z = b"hello"
    print(f" z is of type {type(z)} and has value {z}")
    y = range(5)
    print(f" y is of type {type(y)} and has value {y}")


def test_control_flow(_v):
    if _v < 2:
        print(f"{_v} < 2")
    elif _v == 2:
        print(f"{_v} == 2")
    else:
        print(f"{_v} > 2")


def test_loops():
    for i in range(5):
        print(i)
    print("----Done---")
    for i in range(5, 10):
        print(i)
    print("----Done---")
    for i in range(0, 10, 2):
        print(i)
    print("----Done---")
    for i in range(10, 0, -1):
        print(i)
    print("----Done---")
    for i in range(5):
        if i == 2:
            break
        print(i)
    print("----Done---")
    for i in range(5):
        if i == 2:
            continue
        print(i)
    print("----Done---")
    for i in range(5):
        pass


def test_while():
    """
    Demonstrates the use of while loops. The first loop iterates while `i` is
    less than 5, printing the value of `i` and incrementing it by 1 each time.
    The second loop is an infinite while loop that prints and increments `i`
    until it reaches 10, at which point it breaks out of the loop.
    """
    i = 0
    while i < 5:
        print(i)
        i += 1
    print("----Done---")
    while True:
        if i is None:
            raise ValueError("i is None")
        if i == 10:
            break
        print(i)
        i += 1


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class CustomPerson:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        self._age = value

    def greetings(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


def test_comprehension():
    s = {i: i * 2 for i in range(5)}
    print(s)

    k = [i for i in range(5)]
    print(k)

    l = [i for i in range(5) if i % 2 == 0]
    print(l)

    t = (i for i in range(5))
    print(t)
    for i in t:
        print(i)


def test_read_file():
    try:
        with open("test.txt", "r") as f:
            if f is not None:
                print(f.read())
            else:
                raise FileNotFoundError("File not found")
    except FileNotFoundError as e:
        print(e)


def test_write_file():
    try:
        with open("test.txt", "w") as f:
            if f is not None:
                f.write("Hello, World!")
            else:
                raise FileNotFoundError("File not found")
    except FileNotFoundError as e:
        print(e)


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("custom decorator!")


# manage_types()
# test_control_flow(3)
# test_loops()
# test_while()

""" person = Person("John", 30)
print(person.name)
print(person.age)
print(person) """

""" custom_person = CustomPerson("John", 30)
print(custom_person.greetings()) """

# test_comprehension()
# test_write_file()
# test_read_file()
say_hello()
