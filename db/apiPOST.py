import requests
import json
import re

# Define the API endpoint URL
api_url = 'https://ayntjhpql2.execute-api.ap-southeast-2.amazonaws.com/admin'


def parse_recipe(lines):
    """
    Parse a pair of lines from the recipes file into a dictionary with 'name' and 'ingredients'.
    """
    if len(lines) < 2:
        return None

    name_line = lines[0].strip()
    ingredients = lines[1].strip()

    # Remove the 'recipe_' prefix and any numbers following it from the name
    match = re.match(r'recipe_\d+:\s*(.*)', name_line)
    if match:
        name = match.group(1).strip()
    else:
        name = name_line

    return {
        "name": name,
        "ingredients": ingredients
    }


def post_recipes(file_path):
    """
    Read recipes from a file and post each to the API.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Process recipes in pairs of lines
    for i in range(0, len(lines), 2):
        recipe_lines = lines[i:i+2]
        recipe = parse_recipe(recipe_lines)
        if recipe:
            response = requests.post(api_url, json=recipe)

            # Check if the request was successful
            if response.status_code == 201:
                print(f"Successfully posted recipe: {recipe['name']}")
            else:
                print(
                    f"Failed to post recipe: {recipe['name']}. Status code: {response.status_code}. Response: {response.text}")


# Path to the text file containing the recipes
file_path = './db/recipes.txt'
post_recipes(file_path)
