def validate_schema(instance, schema):
    import jsonschema

    # If it's a Response object → convert
    if hasattr(instance, "json"):
        instance = instance.json()

    jsonschema.validate(instance=instance, schema=schema)