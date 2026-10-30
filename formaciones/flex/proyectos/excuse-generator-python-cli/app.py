import random

# Initial excuse
excuse = "The dog eat my homework when I finished"



def generate_excuse():
    # Lists of possible excuse parts
    who = ['the dog', 'my granma', 'his turtle', 'my bird']
    what = ['eat', 'pissed', 'crushed', 'broked']
    when = [
        'before the class',
        'right in time',
        'when I finished',
        'during my lunch',
        'while I was praying'
    ]

    # Generate a random excuse
    return f"{random.choice(who)} {random.choice(what)} my homework {random.choice(when)}"


# Print the generated excuse
excuse = generate_excuse()
print(excuse)
