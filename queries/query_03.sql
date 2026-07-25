SELECT g2.id, g2.group_title, s2.title, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN groups g2 ON s.group_id = g2.id
JOIN subjects s2 on g.subject_id  = s2.id
WHERE s2.id = 1
GROUP BY g2.id
ORDER BY avg_grade DESC;