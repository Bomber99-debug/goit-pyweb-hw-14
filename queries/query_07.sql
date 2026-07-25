SELECT g2.group_title, s.fullname, g.grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN groups g2 ON g2.id = s.group_id
JOIN subjects s2 ON s2.id = g.subject_id
WHERE g2.id = 2 AND s2.id = 2;