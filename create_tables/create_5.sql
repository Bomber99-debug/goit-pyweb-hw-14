DROP TABLE IF EXISTS grades;
CREATE TABLE IF NOT EXISTS grades (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	student_id INTEGER NOT NULL,
	subject_id INTEGER NOT NULL,
	grade INTEGER CHECK(grade >= 1 AND grade <= 100),
	grade_date DATE
	CHECK (
		grade_date IS NULL
		OR
		(date(grade_date) IS NOT NULL)
	),
	CHECK(
		(grade IS NOT NULL AND grade_date IS NOT NULL)
		OR
		(grade IS NULL AND grade_date IS NULL)
		),
	FOREIGN KEY (student_id) REFERENCES students (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
	,
	FOREIGN KEY (subject_id) REFERENCES subjects (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);