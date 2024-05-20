def cakes(recipe, available):
    cakes_possible = []
    
    for ingredient, amount_needed in recipe.items():
        if ingredient in available:
            cakes_possible.append(available[ingredient] // amount_needed)
        else:
            return 0
    return min(cakes_possible)