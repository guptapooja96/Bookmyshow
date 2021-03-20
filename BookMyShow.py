#difference
class BookMyShow:
    available=10

    def __init__(self,name):
        self.name=name

    def book(self,required):

        self.required=required
        print(self.required," tickets requested by ",self.name)

        if(self.required <= BookMyShow.available):
            print("trying to a book a ticket...")
            BookMyShow.available-=self.required
            print(self.name," ",self.required,"tickets booked successfully")

        else:
            print("Sorry ",self.required," tickets are not available")

        print("Available tickets now ",BookMyShow.available)


user1=BookMyShow("User1")
user1.book(5)

user2=BookMyShow("user2")
user2.book(7)


