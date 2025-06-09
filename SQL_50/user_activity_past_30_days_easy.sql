SELECT DISTINCT(activity_date) as day, COUNT(DISTINCT(user_id)) as active_users
FROM Activity
GROUP BY activity_date
HAVING datediff('2019-07-27', activity_date) < 30
AND activity_date <= '2019-07-27'