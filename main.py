  #TASK ONE
def f(a,b):
    return a**b
a=map(f,[5,7,10],[3,3,3])
print(list(a))

    #Second variant
Triple=list(map(lambda x:x**3,[5,7,10]))
print(Triple)

        #TASK TWO
def i_am_top(func):
    def wrapper(*args,**kwargs):
        print('Nice to meet you!')
        func(*args,**kwargs)
    return wrapper

def im_down(func):
    def wrapper(*args,**kwargs):
        print('Goodbye')
        func(*args,**kwargs)
    return wrapper



def py_c(hi_msg,bye_msg):
    def inner_decorator(func):
        def wrapper(*args,**kwargs):
            print(hi_msg)
            func(*args,**kwargs)
            print(bye_msg)
        return wrapper
    return inner_decorator
@i_am_top
@py_c(" ","  ")
def get_names(v,a,y,p):
    print(f'Users {v},{a},{y},{p}')

get_names('Vlad','Anthony','Yaroslav','Polina')
@im_down
def get_too(func):
    print(f"{func}")
get_too("See you soon")


        #TASK THREE
def top(func):
    def wrapper(*args,**kwargs):
        print('Hello again!!!')
        func(*args,**kwargs)
    return wrapper


def py(hi_msg,bye_msg):
    def inner_decorator(func):
        def wrapper(*args,**kwargs):
            print(hi_msg)
            func(*args,**kwargs)
            print(bye_msg)
        return wrapper
    return inner_decorator

def im_here(func):
    def wrapper(*args,**kwargs):
        print('Open only for this users')
        func(*args,**kwargs)
    return wrapper


@top
@py(" ","  ")
def get_names(v,n,j,p,i):
    print(f'Users {v},{n},{p},{j},{i}')

get_names("Vlad","Nikita","Polina","Julia","Ilya")



#b=[{"Vlad":"name_less_then_5_OPEN"},{"Nikita":"name_more_then_5_CLOSED"},{"Polina":"name_more_then_CLOSED"},{"Julia":"name_more_then_5_CLOSED"},{"Ilya":"name_less_then_5_OPEN"}]
#filter(lambda x : x["name"]== "name_less_then_5_OPEN",b)
#print(b)


#players=[("Vlad","name_less_then_5_OPEN"),("Nikita","name_more_then_5_CLOSED"),("Polina","name_more_then_CLOSED"),("Julia","name_more_then_5_CLOSED"),("Ilya","name_less_then_5_OPEN")]
#print(any(less_5=="name_less_then_5_OPEN" for _, less_5 in players))


coders = ['Vlad', 'Nikita', 'Polina', 'Julia','Ilya']
filtered = [x for x in coders if len(x)<5]
print(filtered)


@im_here
def get_too(func):
    print(f"{func}")
get_too(" ")



            #TASK FOR