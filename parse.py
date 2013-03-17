'''
Challenge #2 from http://adventure.cueup.com/

Andrew Tamura
March 16, 2013

'''

def main():
    parse = Parse('{{[{{{{}}{{}}}[]}[][{}][({[(({{[][()()]}}{[{{{}}}]}))][()]{[[{((()))({}(())[][])}][]()]}{()[()]}]})][]]}{{}[]}}')
    parse.find_mistake()

class Parse():
    original_string = None
    open_tokens = ["{", "[", "("] 
    close_tokens = ["}", "]", ")"]

    def __init__(self, to_be_parsed):
        self.original_string = to_be_parsed

    def is_open_token(self, token):
        if token in self.open_tokens:
            return True

    def is_closed_token(self, token, match):
        token_index = self.open_tokens.index(match)
        if token == self.close_tokens[token_index]:
            return True
        else:
            return False

    def find_mistake(self):
        seen_tokens = []
        for i, val in enumerate(self.original_string):
            if self.is_open_token(val):
                seen_tokens.append(val)
            else:
                try:
                    last_seen = seen_tokens.pop()
                except Exception as e:
                    print i
                    break
                if not self.is_closed_token(val, last_seen):
                    print i
                    break
        
if __name__ == "__main__":
    main()

