SELECT t.fullname, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN subjects s ON s.id = g.subject_id
JOIN teachers t ON t.id = s.teacher_id
WHERE t.id = 2
GROUP BY t.fullname;