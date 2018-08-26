# 装饰器初探

def me(func):
    prefix = 'my name is '
    def name(*args, **kwargs):
        print(prefix + 'bao')
        func(*args, **kwargs)
    return name
@me
def age(age, sex="女"):
    print(str(age)+'岁，性别是'+ sex)

# info = me(age)
# age(23, '男')

def man(name):
    def show_bao(func):
        prefix = 'my name is '
        def my_name(*args, **kwargs):
            print(prefix+name)
            func(*args, **kwargs)
        return my_name
    return show_bao

@man('tu tu')

def tu_tu(age, sex="女"):
    print(str(age)+' year old and gender is ' + sex)

tu_tu(2.5, 'girl')

