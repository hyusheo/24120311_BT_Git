print("Hello Github")
def la_so_nguyen_to (n):
  if(n<2) : return False
    for i in range (n):
      if n % i == 0 : return False;
    return True
