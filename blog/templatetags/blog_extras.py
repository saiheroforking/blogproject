from django import template

# Step 1: Create Library instance
register = template.Library()

# Step 2: Register filter
@register.filter
def word_count(text):
    """
    Returns number of words in a text
    """
    if not text:
        return 0
    return len(text.split())
