SELECT g.group_title, s.fullname
FROM students s
JOIN groups g ON g.id = s.group_id
WHERE g.id = 2;