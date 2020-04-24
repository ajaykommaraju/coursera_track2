# combine first name and last name 
import re 
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Kommaraju, Ajay"))
print(rearrange_name('Hopper, Grace M.'))