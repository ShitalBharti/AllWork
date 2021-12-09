class FlightReservation:
    def __init__(self):
        print("--------------------Welcome to Flight Reservation-----------------")
        print("************Currently available Flights along with seats are***************")
        self.flight_dict = {'Indigo':{'Seats_avail':35,'Seats_occupied':0},'Air india':{'Seats_avail':40,'Seats_occupied':0},'Kingfisher':{'Seats_avail':45,'Seats_occupied':0}}
        print(self.flight_dict)

    def bookFlight(self):
        fname = input("Enter Flight Name:").capitalize()
        #print(fname)
        if fname in self.flight_dict.keys():
            no_person = int(input("Enter No. of persons:"))
            #seats_dict = self.flight_dict.get(fname)
            #print(seats_dict)
            #for key,value in seats_dict.items():
            for key, value in self.flight_dict.get(fname).items():
                init_seats = value
                if key == 'Seats_avail':
                    if no_person <= value:
                        value -= no_person
                        self.flight_dict.get(fname).update({key:value})
                    else:
                        print("Flight Occupied or Persons greater than available seats! Book another flight or try with less persons!")
                        self.showFlights()
                        break
                else:
                    if value <= init_seats:
                        value += no_person
                        self.flight_dict.get(fname).update({key: value})
                        print("Flight booked! Enjoy Journey!")
                        showf = input("See Available Flights Y/N:")
                        if showf == 'y':
                            self.showFlights()
            #print(self.flight_dict)
            self.continueAgain()
        else:
            print("Flight Name is not present!")
            self.continueAgain()

    def continueAgain(self):
        cont = input("Want to continue Y/N").lower()
        if cont == 'y':
            self.bookFlight()
        else:
            print("Visit Again")

    def showFlights(self):
        print(self.flight_dict)

obj = FlightReservation()
obj.bookFlight()
