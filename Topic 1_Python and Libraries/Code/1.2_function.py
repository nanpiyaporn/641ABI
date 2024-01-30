# --- 1. function without arguments ---
# def fun():
#     print("Hello ", end="")

# fun()
# print('Jin')    

# fun()
# print('Mark')    

# fun()
# print('Jack')  

## ------ 2. function with arguments
# def fun1(name):
#     print(f"Hello {name}")

# fun1('Jin')

## ------ 3. Function with default value without reture values (void function)
# def fun1(name, greeting = 'Hello'):
#     print(f"{greeting}, {name}")

# x = fun1('Jin', greeting='Good morning')   
# print(x)


## ------ 4. Function with return values (fruitful function)
def add(a, b):
    c = a + b
    return c

rst = add(10, 5)
print(rst)

