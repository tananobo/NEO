"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""

class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the¥
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches
        self.neos_dict = {}
        for neo in self._neos:
            self.neos_dict[neo.designation] = neo
            if neo.name:
                self.neos_dict[neo.name] = neo

        for approache in self._approaches:
            des = approache._designation
            approache.neo = self.neos_dict[des]
            self.neos_dict[des].approaches.append(approache)

    def get_neo_by_designation(self, designation):

        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        return self.neos_dict.get(designation)

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        return self.neos_dict.get(name)

    def query(self, filters={}):
        for approach in self._approaches:
            if filters.get('distance_min'):
                if approach.distance < filters['distance_min']:
                    continue
            if filters.get('distance_max'):
                if approach.distance > filters['distance_max']:
                    continue
            if filters.get('velocity_min'):
                if approach.velocity < filters['velocity_min']:
                    continue
            if filters.get('velocity_max'):
                if approach.velocity > filters['velocity_max']:
                    continue
            if filters.get('date'):
                if approach.time.date() != filters['date']:
                    continue
            if filters.get('start_date'):
                if approach.time.date() < filters['start_date']:
                    continue
            if filters.get('end_date'):
                if approach.time.date() > filters['end_date']:
                    continue
            if filters.get('diameter_min'):
                if not (approach.neo.diameter >= filters['diameter_min']):
                    continue
            if filters.get('diameter_max'):
                if not (approach.neo.diameter <= filters['diameter_max']):
                    continue
            if filters.get('hazardous') is not None:
                if approach.neo.hazardous != filters['hazardous']:
                    continue
            yield approach

            