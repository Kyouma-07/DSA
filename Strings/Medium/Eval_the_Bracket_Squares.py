class Eval_Bracket_SQ:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        mp = dict(knowledge)

        result = []
        i = 0

        while i < len(s):

            if s[i] == '(':
                i += 1

                key = []

                #reading until ')'
                while s[i] != ')':
                     key.append(s[i])
                     i += 1
                key = ''.join(key)

                #replacing key with org value:
                if key in mp:
                    result.append(mp[key])
                    i += 1
                else:
                    result.append('?')
                    i += 1
            
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)