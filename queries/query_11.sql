SELECT DISTINCT ROUND(AVG(g.grade))
FROM grades g
JOIN subjects s ON s.id = g.subject_id
JOIN teachers t ON t.id = s.teacher_id
JOIN students s2 ON s2.id = g.student_id
WHERE s2.id = 3 AND t.id = 3;