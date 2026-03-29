def validate_ingredients(ingredients: str) -> str:
    for ingredient in ingredients.split():
        if ingredient.lower() not in ['fire', 'water', 'earth', 'air']:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
