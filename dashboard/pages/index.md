---
title: Sakila BI Report
---

# DVD Rental Analysis

## 1. Top 5 Customers
Who are our top 5 customers by total spend?

```sql top_customers
SELECT 
    c.first_name || ' ' || c.last_name AS customer_name,
    SUM(p.amount) AS total_spend
FROM sakila.customer AS c
JOIN sakila.payment AS p ON c.customer_id = p.customer_id
GROUP BY customer_name
ORDER BY total_spend DESC
LIMIT 5
```

<BarChart 
    data={top_customers}
    x=customer_name
    y=total_spend
    title="Top 5 Customers by Spend"
    color=skyblue
    swapXY=true
/>




---

## 2. Revenue per Category
Which movie genres bring in the most money?

```sql category_revenue
SELECT 
    c.name AS category_name,
    SUM(p.amount) AS total_revenue
FROM sakila.category AS c
JOIN sakila.film_category AS fc ON c.category_id = fc.category_id
JOIN sakila.film AS f ON fc.film_id = f.film_id
JOIN sakila.inventory AS i ON f.film_id = i.film_id
JOIN sakila.rental AS r ON i.inventory_id = r.inventory_id
JOIN sakila.payment AS p ON r.rental_id = p.rental_id
GROUP BY category_name
ORDER BY total_revenue DESC
```


<BarChart
data={category_revenue}
x=category_name
y=total_revenue
title="Total Revenue per Category"
color=lightgreen
/>




---

## 3. Most Prolific Actors
Which actors have starred in the most movies?

```sql top_actors
SELECT 
    a.first_name || ' ' || a.last_name AS actor_name,
    COUNT(fa.film_id) AS number_of_movies
FROM sakila.actor AS a
JOIN sakila.film_actor AS fa ON a.actor_id = fa.actor_id
GROUP BY actor_name
ORDER BY number_of_movies DESC
LIMIT 10
```



<BarChart
data={top_actors}
x=actor_name
y=number_of_movies
title="Top 10 Actors by Number of Movies"
color=blue
/>