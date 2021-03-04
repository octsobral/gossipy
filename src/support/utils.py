

def str_to_bool(s: str):
    if type(s) == str:
        b = s.lower()
        if b == 'true':
            return True
        elif b == 'false':
            return False
    elif type(s) == bool:
        return s