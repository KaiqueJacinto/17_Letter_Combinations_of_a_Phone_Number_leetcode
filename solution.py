class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letras = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        saida = []
        len_str = len(str(digits))
        if digits != '':
            for i in letras[int(digits[0])-2]:
                if len_str >1:
                    for j in letras[int(digits[1])-2]:
                        if len_str > 2:
                            for k in letras[int(digits[2])-2]:
                                if len_str > 3:
                                    for l in letras[int(digits[3])-2]:
                                        saida.append(i+j+k+l)
                                else:
                                    saida.append(i+j+k)
                        else:
                            saida.append(i+j)
                else:
                    saida.append(i)
        return saida
