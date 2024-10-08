def compute_completeness(data, criteria):

    results = {}

    for crit in criteria.keys():
        path = criteria[crit]
        val = 0
        for object in data:
            for field in path:
                #for field in subpath:
                    try:
                        object = object[field]
                        if field == path[-1]:
                            val = val + 1
                    except KeyError:
                        val = val + 0
                        break
        results[crit] = val

    return results