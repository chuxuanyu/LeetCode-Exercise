class Solution1:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import operator 
        dic={}
        dic_t ={}
        for i in s:
            dic[i] = dic[i] + 1 if i in dic else 1
        for i in t:
            dic_t[i] = dic_t[i] +1 if i in dic_t else 1
            
        return (operator.eq(dic,dic_t))


class Solution2:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic={}
        for i in s:
            dic[i] = dic[i] + 1 if i in dic else 1
            
        for i in t:
            if i in dic:
                dic[i] = dic[i] -1 
            else:
                return False
        
        for key,value in dic.items():
            if value !=0:
                return False
            
        return True
        
        