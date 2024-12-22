import functools

def validate(func):
    '''
    Add corresponded arguments and implementation here. 
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      cnt = 0
      for i in args:
        if isinstance(i, int)  and 0 <= i <= 256:
          cnt += 1
            
      if cnt == 3:
        return func(*args, **kwargs)
      else:
          return 'Function call is not valid!'
             
             
    return wrapper
     

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"

print(set_pixel(0, 127, 300))
print(set_pixel(0,127,250))