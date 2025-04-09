class Solution:
    def myAtoi(self, s: str) -> int:
        su = ""
        new_char = s.strip()
        flag = 0
        print(new_char)
        if(new_char.startswith('+')):
            new_char = new_char[1:]
        elif(new_char.startswith('-')):
            su += new_char[0]
            new_char = new_char[1:]
        for i in new_char:
            print("yes")
            if  i=='0' and flag==0:
                continue
            elif i in ("0123456789"):
                flag = 1
                su += i
            else:
                if(i not in ("0123456789") and su==""):
                    return 0
                break
        if (su=="+" or su=="-" or su==""):
            return 0
        if(int(su)>math.pow(2,31)-1):
            return (int(math.pow(2,31)-1))
        if(int(su)<math.pow(-2,31)):
            return int(math.pow(-2,31))
        return int(su)
        