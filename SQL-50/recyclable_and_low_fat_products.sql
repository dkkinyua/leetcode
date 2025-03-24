/*
Question:
Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.
*/

SELECT product_id FROM products WHERE products.low_fats = "Y" AND products.recyclable = "Y"
