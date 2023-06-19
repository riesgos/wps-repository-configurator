def pluralize(count, singular, explicit_plural=None):
    if count == 1:
        return f"{count} {singular}"
    plural = explicit_plural or (singular + "s")
    return f"{count} {plural}"
