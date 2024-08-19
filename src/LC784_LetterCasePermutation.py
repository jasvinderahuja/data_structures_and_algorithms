## 784. Letter Case Permutation
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def createPermutation(s, temp, res):
            ## temp state needs to be maintained as it were
            len_temp = len(temp)
            ## print(len_temp)
            if len_temp == len(s):
                ## print(res)
                return res.append(temp[:])
            
            elif s[len_temp].isdigit():
                temp = temp+s[len_temp]
                createPermutation(s, temp, res)

            elif s[len_temp].isalpha():

                temp = temp+s[len_temp].lower()
                createPermutation(s, temp, res)
                temp = temp[:-1]

                temp = temp+s[len_temp].upper()
                createPermutation(s, temp, res)
                ## this is a temp string which will be used when the recursion argument comes back so I need it to be maintained as it came. 
                ## not required for this solution but important nonetheless.
                temp = temp[:-1]
        
        createPermutation(s,"",res)
        return res