SELECT H.hacker_id, H.name, SUM(score) as total_score
FROM Hackers H INNER JOIN
(SELECT hacker_id, MAX(score) as score 
 FROM Submissions 
 GROUP BY challenge_id, hacker_id) max_score 
 On H.hacker_id = max_score.hacker_id
 GROUP BY H.hacker_id, H.name
HAVING total_score > 0
ORDER BY total_score DESC, H.hacker_id;
