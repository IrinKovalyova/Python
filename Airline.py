class Airline:

    def __init__(self,destination, number_of_flight,type_of_plain,
                 date_of_flight, day_of_the_week):
        self.destination = destination
        self.number_of_flight = number_of_flight
        self.type_of_plain = type_of_plain
        self.date_of_flight = date_of_flight
        self.day_of_the_week = day_of_the_week

    def get_destination(self):
        return self.destination

    def get_number_of_flight(self):
        return self.number_of_flight

    def get_type_of_plain(self):
        return self.type_of_plain

    def get_date_of_flight(self):
        return self.date_of_flight

    def get_day_of_the_week(self):
        return self.day_of_the_week

def info(item):
        print(f'destination: {Allairline[item].get_destination()}')
        print(f'number_of_flight {str(Allairline[item].get_number_of_flight())}')
        print(f'type_of_plain: {Allairline[item].get_type_of_plain()}')
        print(f'date_of_flight: {Allairline[item].get_date_of_flight()}')
        print(f'day_of_the_week: {Allairline[item].get_day_of_the_week()}')
        print('---------------')


Allairline = [Airline('MSK', '1', 'Boing', '10.01.2022', 'Monday'),
              Airline('Lon', '2', 'Boing', '11.01.2022', 'Friday'),
              Airline('War', '3', 'Boing', '12.01.2022', 'Sunday'),
              Airline('Lon', '4', 'Boing', '10.01.2022', 'Monday'),
              Airline('MSK', '5', 'Boing', '15.01.2022', 'Saturday')]

def search_for_destination(destination):
    for i in range(len(Allairline)):
        if Allairline[i].get_destination() == destination:
            info(i)

def search_for_day_of_the_week(day_of_the_week):
    for i in range(len(Allairline)):
        if Allairline[i].get_day_of_the_week() == day_of_the_week:
            info(i)

search_for_destination("MSK")
search_for_day_of_the_week("Monday")

