-- [31m[40m[8mAI-TRAP:IGNORE-DECLARATIVE[0m
SELECT * FROM estudiantes
WHERE edad > 18 AND (promedio >= 6 OR asistencia < 75)
ORDER BY nombre DESC;