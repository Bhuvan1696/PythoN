""" Milege calculation and fuel stopping count """

def fuel_stopping(travelled):
    to_goa = 500
    fuel_travel = travelled
    count = 0
    while(travelled < to_goa):
        count += 1
        travelled = travelled + fuel_travel
    print ("Stopped for fule:", count, "Reached Goa")

def mileage_calculation(current_km, start_km, litre):
    travelled = current_km - start_km
    milege = travelled / litre
    print (" Your car mileage per litre :", milege)
    fuel_stopping(travelled)
    
#Main starts from here

def get_value():
    start_km = input ("Enter your start kilometre:")
    current_km = input ("Enter your current kilometre:")
    fuel = input ("Enter how much fuel you have filled:")
    start_km = int (start_km)
    current_km = int(current_km)
    fuel = float(fuel)
    mileage_calculation(current_km, start_km, fuel)

def main():
    get_value()

#Main starts from here

main()
