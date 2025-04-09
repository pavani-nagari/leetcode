class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        final_li = []
        for i in range(1,n+1):
            if(i%3 == 0 and i%5==0):
                final_li.append("FizzBuzz")
            elif(i%3 == 0):
                final_li.append("Fizz")
            elif(i%5 == 0):
                final_li.append("Buzz")
            else:
                final_li.append(str(i))
        return final_li
            

