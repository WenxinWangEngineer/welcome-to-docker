-- output 4 columns of the total number of the access and is_preview combination views
SELECT 
    -- SUM() + [CASE WHEN (condition1 AND/OR condition2 ...) THEN 1 ELSE 0 END] to count the number instead of COUNT() 
    -- for complex situations w/o subquery/CTE[Common Table Expression]
    SUM(CASE WHEN is_preview = 0 AND access = 'Wifi' THEN 1 ELSE 0 END) AS total_wifi_non_preview,
    SUM(CASE WHEN is_preview = 1 AND access = 'Wifi' THEN 1 ELSE 0 END) AS total_wifi_preview,
    SUM(CASE WHEN is_preview = 0 AND access = 'Mobile' THEN 1 ELSE 0 END) AS total_mobile_non_preview,
    SUM(CASE WHEN is_preview = 1 AND access = 'Mobile' THEN 1 ELSE 0 END) AS total_mobile_preview,
FROM fill_valid_user_table
WHERE country = 'United States' AND is_useful = 1 AND date = '20230210';


-- get the group by 
SELECT location, SUM(chunk_of_data)
FROM fill_valid_user_table
WHERE date > today() - 7        -- No need to use HAVING unless for aggregation
GROUP BY location               -- WHERE clause has to be in front of GROUP BY clause
ORDER BY SUM(chunk_of_data) DESC
LIMIT 10
;


-- SIMPLE SELECT 
SELECT path, data_size_new
FROM tabale_view_valid_users
WHERE asda = 'asda' AND aerra = 'asfz'
ORDER BY data_size_new
LIMIT 10
;