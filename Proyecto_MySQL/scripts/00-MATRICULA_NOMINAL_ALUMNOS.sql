-- MATRICULA_NOMINAL_ALUMNOS

SELECT 
a.id AS 'Alumno_ID',
p.documento AS 'DNI',
p.apellido AS 'Apellido',
p.nombre AS 'Nombre',
sex.descripcion AS 'Sexo',
p.fecha_nacimiento AS 'Fecha Nacimiento',
TIMESTAMPDIFF(YEAR,p.fecha_nacimiento,CURDATE()) AS 'Edad',
c.descripcion AS 'Curso',
d.division AS 'Division',
tur.descripcion AS 'Turno', 
mo.descripcion AS 'Modalidad',
n.descripcion AS 'Nivel',
g.descripcion AS 'Gestion',
s.nombre AS 'Supervisión',
e.id AS 'ID_escuela',
e.cue AS 'CUE',
e.subcue AS 'subcue',
e.numero AS 'Numero_escuela',
e.anexo AS 'Anexo',
CONCAT(e.numero,'-',e.anexo) AS 'Número_Anexo',
e.nombre AS 'Escuela',
dep.descripcion AS 'Departamento',
l.descripcion AS 'Localidad',
z.descripcion AS 'zona',
amb.descripcion AS 'AMBITO',
reg.descripcion AS 'Regional',
coor.Lat AS 'latitud',
coor.`Long` AS 'longitud'
FROM escuela e
LEFT JOIN ambito amb ON e.ambito_id = amb.id 
-- join nivel ni ON ni.id=e.nivel_id 
JOIN division d ON d.escuela_id = e.id  AND d.fecha_baja IS NULL 
JOIN alumno_division ad ON ad.division_id = d.id AND ad.ciclo_lectivo = 2022  AND ad.fecha_hasta IS NULL  
JOIN alumno a ON a.id = ad.alumno_id 
JOIN persona p ON p.id=a.persona_id 
JOIN curso c ON c.id = d.curso_id 
JOIN nivel n ON n.id = e.nivel_id 
JOIN dependencia g ON g.id = e.dependencia_id 
LEFT JOIN localidad l ON e.localidad_id = l.id 
LEFT JOIN departamento dep ON l.departamento_id = dep.id
LEFT JOIN supervision s ON s.id=e.supervision_id 
LEFT JOIN zona z ON z.id = e.zona_id 
LEFT JOIN sexo sex ON sex.id = p.sexo_id 
LEFT JOIN regional reg ON reg.id = e.regional_id 
LEFT JOIN modalidad mo ON mo.id = d.modalidad_id 
LEFT JOIN turno tur ON tur.id = d.turno_id
LEFT JOIN coordenada coor ON coor.escuela_id = e.id

WHERE
e.fecha_cierre IS NULL
-- AND n.id IN ('3 , 4')
-- AND c.id IN ('1' , '14')
-- AND p.documento = '49582759'
 
group by g.id , e.nivel_id , a.id
ORDER BY
n.id, 
Gestion, 
`Supervisión`,
`Número_Anexo`,
Alumno_ID	