Select Employees.FirstName, 

From Orders  o, 

Join O.EmployeeID on Employees.EmployeeID,  
group by Employee.FirstName; 
