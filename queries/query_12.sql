SELECT g2.group_title, s2.fullname, g.grade, g.grade_date
FROM grades g
JOIN subjects s ON s.id = g.subject_id
JOIN students s2 ON s2.id = g.student_id
JOIN groups g2 ON g2.id = s2.group_id
WHERE g2.id = 2 AND s.id = 2 AND g.grade_date = (
    SELECT MAX(g_inner.grade_date)
    FROM grades g_inner
    JOIN students s_inner ON s_inner.id = g_inner.student_id
    JOIN subjects s2_inner ON s2_inner.id = g_inner.subject_id
    WHERE s_inner.group_id = 2 AND s2_inner.id = 2
);