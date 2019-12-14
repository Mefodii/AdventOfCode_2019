from math import ceil

INPUT = "I"
OUTPUT = "O"

USED = "U"
PRODUCED = "P"

FUEL = "FUEL"
ORE = "ORE"


###############################################################################
def run_a(input_data):
    reactions = build_reactions(input_data)
    extras = {}
    ore_cost = get_basic_reaction("FUEL", 1, extras, reactions)
    print(ore_cost, extras)
    return [ore_cost]


def run_b(input_data):
    reactions = build_reactions(input_data)
    extras = {}
    fuel_produced = 1620000
    ore_cost = get_basic_reaction("FUEL", fuel_produced, extras, reactions)
    while ore_cost < 1000000000000:
        ore_cost += get_basic_reaction("FUEL", 1, extras, reactions)
        if ore_cost <= 1000000000000:
            fuel_produced += 1
            print(ore_cost, fuel_produced)

    print(fuel_produced)
    return [fuel_produced]


def get_basic_reaction(element_name, qty, extras, reactions):
    reaction = reactions[element_name].get(PRODUCED, None)
    if qty <= 0:
        return 0

    if reaction:
        cost = 0
        produces = reaction[0][OUTPUT][element_name]
        extra = extras.get(element_name, 0)
        repeats = ceil((qty - extra) / produces)

        produced = repeats * produces
        rest = produced - qty + extra
        extras[element_name] = rest

        for chemical, required in reaction[0][INPUT].items():
            cost += get_basic_reaction(chemical, repeats * required, extras, reactions)

        return cost

    return qty


def build_reactions(data):
    reactions = {}
    for line in data:
        inputs, outputs = line.split(" => ")
        inputs = [element.split(" ") for element in inputs.split(", ")]
        outputs = outputs.split(" ")

        reaction = build_reaction(inputs, outputs)

        for chemical in inputs:
            name = chemical[1]

            element = reactions.get(name, get_template_reaction())
            element[USED].append(reaction)
            reactions[name] = element

        name = outputs[1]
        element = reactions.get(name, get_template_reaction())
        element[PRODUCED].append(reaction)
        reactions[name] = element

    # for key, value in reactions.items():
    #     print(key, value)

    return reactions


def build_reaction(inputs, outputs):
    reaction = {INPUT: {},
                OUTPUT: {}}

    for chemical in inputs:
        name = chemical[1]
        qty = chemical[0]
        reaction[INPUT][name] = int(qty)

    name = outputs[1]
    qty = outputs[0]
    reaction[OUTPUT][name] = int(qty)

    return reaction


def get_template_reaction():
    return {USED: [],
            PRODUCED: []}
