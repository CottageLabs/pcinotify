import re

from coarnotify.validate import absolute_uri, Validator

# FIXME: should be in the coarnotify library
def add_rules(validator, rules):
    # FIXME: rules should be a property
    existing = validator.rules()

    def merge_dicts_recursive(dict1, dict2):
        merged = dict1.copy()  # Start with a copy of dict1
        for key, value in dict2.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = merge_dicts_recursive(merged[key], value)
            else:
                merged[key] = value
        return merged

    new_rules = merge_dicts_recursive(existing, rules)
    return Validator(new_rules)

def mailto(obj, email: str):
    absolute_uri(obj, email)
    if not email.startswith("mailto:"):
        raise ValueError("Invalid mailto URI: " + email)
    if re.match(r"mailto:[^@]+@[^@]+\.[^@]+", email) is None:
        raise ValueError("Invalid email address: " + email)
    return True