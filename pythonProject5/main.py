def logged(say_hi,say_goodbye):
    def inter_correct(func):
        def wrapper(*args,**kwargs):
            print(say_hi)
            func(*args,**kwargs)
            print(say_goodbye)
        return wrapper
    return inter_correct

@logged('tg','vk')
def py_c(tg,vk):
    print(f"called{tg,vk}")
py_c('vk_links','tg+linkjs')