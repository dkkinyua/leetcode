/*
Question:
Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

*/

SELECT name FROM customer WHERE referee_id IS NULL OR referee_id != 2