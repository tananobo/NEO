class NEODatabase:
    def __init__(self, neos, approaches):

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
        return self.neos_dict.get(designation)

    def get_neo_by_name(self, name):
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
            if filters.get('hazardous'):
                if approach.neo.hazardous != filters['hazardous']:
                    continue
            yield approach
