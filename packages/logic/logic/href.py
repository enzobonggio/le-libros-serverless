def code_from_href(href):
    parts = str(href).split('/')
    filtered_parts = filter(lambda part: len(part) > 0, parts)
    return list(filtered_parts)[-1].lower()
