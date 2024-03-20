#python script that determines if you entered and even or odd number

def main():

  def check_num():
    input_num = int(input('Number to be determined: '))
    if input_num % 2 == 0:
      return 'Even'
    else:
      return 'Odd'
  
    
  print(check_num())

main()