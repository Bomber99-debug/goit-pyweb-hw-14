SELECT g.id, s.fullname, s2.title, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects s2 on g.subject_id  = s2.id
WHERE s2.id = 3
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;