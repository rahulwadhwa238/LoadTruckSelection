import datetime

class LoadTruck:
	TruckList = []
	def __init__(self,num, r, s, e, l):
		self.number = num
		self.rate = r
		self.start = s
		self.end = e
		self.left = l
		self.status = True
		LoadTruck.TruckList.append(self)

	def set_days_left(self,days_left):
		self.days_left = days_left

def cycle_left(LoadTruck):
	for Truck in LoadTruck.TruckList:
		if (Truck.start > current_date):
			days_left = Truck.end-current_date
		else:
			days_left = 30 - (current_date - Truck.start)

		Truck.set_days_left(days_left)
		#print (Truck.number, ":", Truck.days_left)

def truck_selection(LoadTruck):
	cycle_left(LoadTruck)
	truck_selection = []

	for Truck in LoadTruck.TruckList:
		if (Truck.left >= current_task):
			task_cost = Truck.rate*current_task
			cost_breakdown = "\t{} INR/Km\t{} Km\t\t\t{} INR/Km\t{} Km".format(Truck.rate, Truck.left, 0, 0)
			left = Truck.left - current_task
		else:
			task_cost = Truck.rate*Truck.left + ((Truck.rate*12)/10)*(current_task-Truck.left)
			cost_breakdown = "\t{} INR/Km\t{} Km\t\t\t{} INR/Km\t{} Km".format(Truck.rate, Truck.left, ((Truck.rate*12)/10), (current_task-Truck.left))
			left = 0

		truck_selection.append(["Truck No.: ", Truck.number, "\n\nCost BreakDown:\n\tMinimum Rate\tMinimum Distance Left\tAfter Rate\tAfter Distance\n", cost_breakdown, "\nTotal Cost: ", task_cost, " INR\n\nDistance Left After Task: ", left, "\nCycle Day(s) Left: ", Truck.days_left])
			
	truck_selection.sort(key = lambda x: (x[9], x[5], x[7]))

	for selected_truck_details in truck_selection[0] :
		print (selected_truck_details, end = "")


###############				Object Defined			######################### 
		
l1 = LoadTruck(1,30,7,6,500)
l2 = LoadTruck(2,60,1,30,700)

current_date = datetime.datetime.now().day						#CurrentDate
current_task = 800												#CurrentTask


###################			Main Thread			########################### 
print("Task Distance: ", current_task, "km")
print("Current Date:", datetime.datetime.now().date(), "\n")
truck_selection(LoadTruck)
print("\n")