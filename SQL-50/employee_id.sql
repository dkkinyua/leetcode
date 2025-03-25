/*
Question:
Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Return the result table in any order.

Approach:
We need to replace the unique_id of an employee in the Employees table with the corresponding unique_id in the employeeUNI table. If an employee doesn't have a unique_id, we return NULL.
We'd use a LEFT JOIN because we are including all the employees who have and don't have a unique_id.

*/

SELECT employeeUNI.unique_id, employees.name FROM employees LEFT JOIN employeeUNI ON employees.id = employeeUNI.id