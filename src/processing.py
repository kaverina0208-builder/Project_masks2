accepted_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(accepted_list: list, state: str = "EXECUTED") -> list:
    """The function returns a new list of dictionaries containing only those dictionaries whose key 'state'
    matches the specified value"""
    new_list = []
    for element in accepted_list:
        if element.get("state", 0) == state:
            new_list.append(element)
    return new_list


if __name__ == "__main__":
    print(filter_by_state(accepted_list))
    print()


def sort_by_date(accepted_list: list, ascending: bool = True) -> list:
    """The function returns a new list sorted by date"""
    if ascending is True:
        accepted_list.sort(key=lambda x: x.get("date", 0), reverse=True)
    else:
        accepted_list.sort(key=lambda x: x.get("date", 0))
    return accepted_list


if __name__ == "__main__":
    print(sort_by_date(accepted_list))
