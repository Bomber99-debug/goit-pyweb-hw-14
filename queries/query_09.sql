SELECT DISTINCT s2.fullname, s.title
FROM grades g
JOIN subjects s ON s.id = g.subject_id
JOIN students s2 ON s2.id = g.student_id
WHERE s2.id = 2
ORDER BY s.title ASC;