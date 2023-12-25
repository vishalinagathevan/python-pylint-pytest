import mathamatic
# function call with two arguments with testing.

def test_calc_addition():
    output = mathamatic.calc_addition(2,4)
    assert output == 6  
    
# function call with two arguments with testing.

def test_calc_substraction():
    output = mathamatic.calc_substraction(2, 4)
    assert output == -2  
    
# function call with two arguments with testing. 
    
def test_calc_multiply():
    output = mathamatic.calc_multiply(2,4)
    assert output == 8 
    
# function call with two arguments with testing. 
      
def test_calc_division():
    output = mathamatic.calc_division(2,4)
    assert output == 0.5
    # assert output
       