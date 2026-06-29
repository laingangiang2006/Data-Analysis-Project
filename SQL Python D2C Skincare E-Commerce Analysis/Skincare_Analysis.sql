# 1. CUSTOMER ANALYSIS

# Top 5 customers by total orders
SELECT c.customer_id, c.customer_name, COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_orders DESC
LIMIT 5;

# Top 5 customers by total spent
SELECT c.customer_id, c.customer_name, ROUND(SUM(o.final_amount), 3) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id DESC
LIMIT 5;

# Customer orders summary
SELECT c.customer_id, c.customer_name, COUNT(o.order_id) AS order_count, ROUND(SUM(o.final_amount), 3)
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id;

# 2. REVENUE ANALYSIS

# Total revenue by month
SELECT DATE_FORMAT(STR_TO_DATE(order_date, '%d-%m-%Y'), '%m-%Y') AS month_year, COUNT(order_id) AS order_count
FROM orders
GROUP BY DATE_FORMAT(STR_TO_DATE(order_date, '%d-%m-%Y'), '%m-%Y')
ORDER BY MIN(STR_TO_DATE(order_date, '%d-%m-%Y'));

# Orders count by status
SELECT order_status, COUNT(order_id) AS 'order_count'
FROM orders
GROUP BY order_status;

# Most used payment methods
SELECT payment_method, COUNT(payment_method) AS total_orders
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC;

# Most used sales channels
SELECT sales_channel, COUNT(order_id) AS order_count
FROM orders
GROUP BY sales_channel
ORDER BY order_count DESC;

# 3. PRODUCT ANALYSIS
# Product stats by category
SELECT category, COUNT(product_id) AS total_products, ROUND(AVG(cost_price), 3) AS avg_cost_price
FROM products
GROUP BY category
ORDER BY avg_cost_price DESC;

# Cheapest product per category
SELECT p.product_id, p.product_name, p.category, p.cost_price
FROM products p
WHERE cost_price = (SELECT MIN(cost_price) FROM products WHERE category = p.category)
ORDER BY p.cost_price;

# Products count by skin concern
SELECT concern, COUNT(product_id) AS product_count
FROM products
GROUP BY concern
ORDER BY product_count DESC;

# Oily and dry skin exfoliation products
SELECT skin_type, COUNT(product_id) AS product_count
FROM products
WHERE concern = 'Exfoliation' AND (skin_type LIKE '%Oily%' OR skin_type LIKE '%Dry%')
GROUP BY skin_type
ORDER BY product_count DESC;

# Affordable acne and exfoliation products
SELECT product_id, product_name, cost_price
FROM products
WHERE cost_price < 300 AND concern = ("Acne Control" OR "Exfolation")
ORDER BY cost_price;

# 4. REVIEW ANALYSIS
# Customer review details
SELECT c.customer_id, c.customer_name, r.review_id, r.product_id, r.order_id, r.rating, r.review_date 
FROM customers c
JOIN reviews r
ON c.customer_id = r.customer_id
ORDER BY c.customer_id;

# Top 5 products by average rating
SELECT product_id, ROUND(AVG(rating), 3) AS avg_rating
FROM reviews
GROUP BY product_id
ORDER BY avg_rating DESC
LIMIT 5;

# Average rating by category
SELECT p.category, ROUND(AVG(r.rating), 3) AS avg_rating
FROM products p
JOIN reviews r
ON p.product_id = r.product_id
GROUP BY p.category
ORDER BY avg_rating DESC;

# 5. RETURN ANALYSIS

# 5 most returned products
SELECT r.product_id, COUNT(o.order_id) AS total_orders
FROM orders o
JOIN returns r
ON o.order_id = r.order_id
WHERE o.order_status = "returned"
GROUP BY r.product_id
HAVING COUNT(o.order_id) >= 5
ORDER BY total_orders DESC;

# Return rate by product
SELECT p.product_id, p.product_name, COUNT(r.return_id) AS product_count
FROM products p
JOIN returns r
ON p.product_id = r.product_id
GROUP BY p.product_id, product_name
ORDER BY product_count;

# Most common return reasons
SELECT return_reason, COUNT(order_id) AS order_count
FROM returns
GROUP BY return_reason
ORDER BY order_count DESC;

# Most common refund statuses
SELECT refund_status, COUNT(order_id) AS order_count
FROM returns
GROUP BY refund_status
ORDER BY order_count DESC;