def hello(name=None):
    name = name if name is not None else "Stranger"
    return f"Howdy {name}"
