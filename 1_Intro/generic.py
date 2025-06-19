from typing import List

# The types like "List[]" "Tuple[]" "Set" "Dict" "Optional"
# Are called Generic
def process_items(items: List[str]):
    for item in items:
        print(item)
