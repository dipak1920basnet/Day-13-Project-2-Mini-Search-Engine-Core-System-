def validate_query(query):

    if not query or not query.strip():
        raise ValueError("Query cannot be empty")
    
    if len(query) > 100:
        raise ValueError("Query too long")
    
    return True
