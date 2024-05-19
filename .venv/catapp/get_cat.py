import random
from django.db import models
from .models import Cat, RarityProbability
def get_random_cat():
    # Get the total number of rarity probabilities
    total_probabilities = RarityProbability.objects.aggregate(total=models.Sum('probability'))['total']

    # Select a random number between 0 and the total probability
    random_number = random.uniform(0, total_probabilities)

    # Iterate through the rarity probabilities and select a cat based on the random number
    cumulative_probability = 0
    for rarity_probability in RarityProbability.objects.all():
        cumulative_probability += rarity_probability.probability
        if random_number <= cumulative_probability:
            # Get a random cat with the selected rarity
            return Cat.objects.filter(rarity=rarity_probability.rarity).order_by('?').first()

    # Default case if no matching rarity is found
    return None