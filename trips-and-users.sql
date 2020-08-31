# GOAL: Find daily cancellation rate of valid requests.

# Trips             Users
#   Id                  Users_Id
#   Client_Id           Banned
#   Driver_Id           Role
#   City_Id
#   Status

# STEP1: Filter table to only include valid requests.  Make available as a CTE.

# ValidRequests (double join trips to users on Client_Id = Users_id and Driver_Id = Users_Id, Banned like 'no')
#   Id
#   Request_at
#   Client_Banned
#   Driver_Banned

# STEP 2: Count the number of valid requests made each day, and the number that were cancelled.  Implement as subqueries.

# ValidCounts (group by Request_at)
#   Day
#   COUNT(cancelled requests by unbanned)

# CancelledCounts (status like 'cancelled', group by Request_at)
#   Day
#   COUNT(total requests by unbanned)

# STEP 3: Divide number of valid cancelled requests by the total number of valid requests

# Output (join on day, between '2013-10-01' and '2013-10-03')
#   Day
#   Cancellation Rate (rounded to two decimal places)

WITH 
ValidRequests AS (
    SELECT Trips.Id, Trips.Request_at, Trips.Status, U1.Banned Client_Banned, U2.Banned Driver_Banned 
    FROM Trips
    JOIN Users U1 ON Trips.Client_Id = U1.Users_Id
    JOIN Users U2 ON Trips.Driver_Id = U2.Users_Id
    WHERE U1.Banned LIKE 'No' AND U2.Banned LIKE 'No'
)

SELECT ValidCounts.Request_at AS Day, IFNULL( ROUND( CancelledCounts.Cancelled_requests / ValidCounts.Total_requests, 2), 0.00) AS "Cancellation Rate"
FROM (
    SELECT Request_at, COUNT(*) Total_requests 
    FROM ValidRequests 
    GROUP BY Request_at
    ) AS ValidCounts
LEFT JOIN (
    SELECT Request_at, COUNT(*) Cancelled_requests 
    FROM (
        SELECT * 
        FROM ValidRequests 
        WHERE Status LIKE '%ancelled%') AS CancelledRequests 
        GROUP BY Request_at
    ) AS CancelledCounts
ON ValidCounts.Request_at = CancelledCounts.Request_at
WHERE ValidCounts.Request_at BETWEEN "2013-10-01" AND "2013-10-03";
