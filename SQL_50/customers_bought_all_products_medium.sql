SELECT customer_id
FROM Customer c
GROUP BY customer_id
HAVING COUNT(DISTINCT(product_key)) = (SELECT COUNT(product_key) FROM Product)