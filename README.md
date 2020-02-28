# LoadTruckSelection

This python scripts works upon Selection Stratergy of the Best Load Truck for a given task.
To maximize a courier company profit, the algorithm finds the best available Load Truck.

Given:
  A number of Load Trucks, each having its own properties
      Vehicle Number
      Rate (Price/Km)
      Monthly Rental Cycle (Start date & End date)
      Minimum KM Gurantee Run
      Truck Status (Reached and Unloading, Waiting for new assignment or On the way to its destination)

Criteria:
  Selection stratergy is to utilize each Load Truck to its minimum km run during its cycle.
