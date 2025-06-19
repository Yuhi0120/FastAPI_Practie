def get_full_name(first: str, last: str):
    full = first.title() + " " + last.title()
    return full
    
print(get_full_name("john", "doe"))