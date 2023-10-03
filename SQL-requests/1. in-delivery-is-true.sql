/**
PostgreSQL не очень любит заглавные буквы
Пришлось всё страшно экранировать 
**/

SELECT c.login, COUNT(*)
    FROM "Couriers" AS c
    INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE "inDelivery" = true
GROUP BY c.login; 
