SELECT s.title, t.fullname
FROM subjects s
JOIN teachers t ON s.teacher_id = t.id
WHERE t.id = 2;