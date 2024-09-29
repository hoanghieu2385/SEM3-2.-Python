class Vehicle():
    def __init__(self, name, year, company, seat_num) -> None:
        self.name = name
        self.year = year
        self.company = company
        self.seat_num = seat_num
    
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.year
    def set_name(self, year):
        self.year = year
    
    def get_name(self):
        return self.company
    def set_name(self, company):
        self.company = company
    
    def get_name(self):
        return self.seat_num
    def set_name(self, seat_num):
        self.seat_num = seat_num
    
    def start(self):
        print(f"Vehicle: {self.name} - {self.year} - {self.company} - {self.seat_num} - is start")
            
    def run(self):
        print(f"Vehicle: {self.name} - {self.year} - {self.company} - {self.seat_num} - is running")
        
    def stop(self):
        print(f"Vehicle: {self.name} - {self.year} - {self.company} - {self.seat_num} - is stop")