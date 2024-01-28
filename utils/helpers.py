def find_key(data, target_key):
    """
    Recursive search for target_key in the JSON data.

    Input:
        - data: The parsed response data, dictionary or list.
        - target_key: The key to search for in the JSON data.

    Output:
        - True: If the key is found in the JSON data.
        - False: The key is not found in the JSON data.
    """
    
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                return True
            elif find_key(value, target_key):
                return True
    elif isinstance(data, list):
        for item in data:
            if find_key(item, target_key):
                return True
    return False