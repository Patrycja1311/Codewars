def to_query_string(data):
    return "&".join(
        f"{k}={v}"
        for k, val in data.items()
        for v in (val if isinstance(val, list) else [val])
    )

