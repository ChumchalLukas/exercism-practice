"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    all_wagons = list(args)

    return all_wagons


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # locomotive:
    locomotive_place = each_wagons_id.index(1)
    locomotive = each_wagons_id[locomotive_place]
    
    del each_wagons_id[locomotive_place]

    # wagons - 1., 2.
    wagons = each_wagons_id[0:2]

    del each_wagons_id[0:2]

    return [locomotive, *missing_wagons, *each_wagons_id, *wagons]



def add_missing_stops(orientation, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    # all stops together:
    stops_all = list(kwargs.values())

    # add stops - orientation:
    orientation["stops"] = stops_all

    return orientation

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    # pack all dictionaries:
    route_information_all = {**route, **more_route_information}

    return route_information_all
    
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return list(map(list, zip(*wagons_rows)))
