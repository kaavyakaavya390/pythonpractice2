from new_package import module2

def func3():
    print("from new package -> module3")
    print(f"from module3...")
    module2.func2()
