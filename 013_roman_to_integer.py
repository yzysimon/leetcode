class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rome = 0
        excs = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        if 'IV' in s:
                rome += 4 * s.count('IV')
                s = s.replace('IV', '')                 
        if 'IX' in s:
                rome += 9 * s.count('IX')
                s = s.replace('IX', '')
        if 'XL' in s:
                rome += 40 * s.count('XL')
                s = s.replace('XL', '')  
        if 'XC' in s:
                rome += 90 * s.count('XC')
                s = s.replace('XC', '')
        if 'CD' in s:
                rome += 400 * s.count('CD')
                s = s.replace('CD', '')
        if 'CM' in s:
                rome += 900 * s.count('CM')
                s = s.replace('CM', '')    
        if 'I' in s:
                rome += s.count('I')
        if 'V' in s:
                rome += 5 * s.count('V')
        if 'X' in s:
                rome += 10 * s.count('X')
        if 'L' in s:
                rome += 50 * s.count('L')    
        if 'C' in s:
                rome += 100 * s.count('C') 
        if 'D' in s:
                rome += 500 * s.count('D')
        if 'M' in s:
                rome += 1000 * s.count('M')
                
        return rome
