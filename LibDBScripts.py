seleccionarTablaNivel = """SELECT
                          *
                          FROM
                          nivel"""
                          
insertarEnTablaResultado = """INSERT IGNORE INTO resultado 
                            (id , 
                            descripcion , 
                            linea_id , 
                            formal , 
                            orden , 
                            audi_user , 
                            audi_fecha , 
                            audi_accion) 
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
                            
dropTabla_MATRICULA_NOMINAL_SiExiste = """DROP TABLE IF EXISTS MATRICULA_NOMINAL"""

crearTablaMatriculaNominal = """CREATE TABLE MATRICULA_NOMINAL 
                                (Alumno_ID INT(10), 
                                DNI INT(10),
                                Apellido_Alumno VARCHAR(100),
                                Nombre_Alumno VARCHAR(100),
                                Sexo VARCHAR(45),
                                Fecha_Nacimiento DATE,
                                Edad INT(10),
                                Curso VARCHAR(45),
                                División VARCHAR(45),
                                Turno CHAR(25),
                                Modalidad VARCHAR(45),
                                Nivel VARCHAR(50),
                                Gestión VARCHAR(45),
                                Supervisión VARCHAR(150),
                                Escuela_ID INT(10),
                                CUE INT(7),
                                subcue INT(2),
                                Número_escuela VARCHAR(6),
                                Anexo INT(10),
                                Número_Anexo VARCHAR(10),
                                Nombre_Escuela VARCHAR(120),
                                Departamento VARCHAR(45),
                                Localidad VARCHAR(45),
                                zona VARCHAR(20),
                                AMBITO VARCHAR(60),
                                Regional VARCHAR(45),
                                latitud FLOAT(45),
                                longitud FLOAT(45))"""

matriculaNominalCicloLectivoActual = """SELECT 
                                        a.id AS 'Alumno_ID', 
                                        p.documento AS 'DNI',
                                        p.apellido AS 'Apellido_Alumno',
                                        p.nombre AS 'Nombre_Alumno',
                                        sex.descripcion AS 'Sexo',
                                        p.fecha_nacimiento AS 'Fecha_Nacimiento',
                                        TIMESTAMPDIFF(YEAR,p.fecha_nacimiento,CURDATE()) AS 'Edad',
                                        c.descripcion AS 'Curso',
                                        d.division AS 'División',
                                        tur.descripcion AS 'Turno', 
                                        mo.descripcion AS 'Modalidad',
                                        n.descripcion AS 'Nivel',
                                        g.descripcion AS 'Gestión',
                                        s.nombre AS 'Supervisión',
                                        e.id AS 'Escuela_ID',
                                        e.cue AS 'CUE',
                                        e.subcue AS 'subcue',
                                        e.numero AS 'Número_escuela',
                                        e.anexo AS 'Anexo',
                                        CONCAT(e.numero,'-',e.anexo) AS 'Número_Anexo',
                                        e.nombre AS 'Nombre_Escuela',
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
                                        Gestión, 
                                        `Supervisión`,
                                        `Número_Anexo`,
                                        Alumno_ID                                        
                                        """
                                        
insertarEnTabla_MATRICULA_NOMINAL = """INSERT INTO MATRICULA_NOMINAL 
                                       (Alumno_ID, 
                                        DNI,
                                        Apellido_Alumno,
                                        Nombre_Alumno,
                                        Sexo,
                                        Fecha_Nacimiento,
                                        Edad,
                                        Curso,
                                        División,
                                        Turno,
                                        Modalidad,
                                        Nivel,
                                        Gestión,
                                        Supervisión,
                                        Escuela_ID,
                                        CUE,
                                        subcue,
                                        Número_escuela,
                                        Anexo,
                                        Número_Anexo,
                                        Nombre_Escuela,
                                        Departamento,
                                        Localidad,
                                        zona,
                                        AMBITO,
                                        Regional,
                                        latitud,
                                        longitud) 
                                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                                        
crearTabalInstitucional = """CREATE TABLE TABLA_INSTITUCIONAL 
                                (
                                Nivel VARCHAR(50),
                                Gestión VARCHAR(45),
                                Supervisión VARCHAR(150),
                                Escuela_ID INT(10),
                                CUE INT(7),
                                subcue INT(2),
                                Número_escuela VARCHAR(6),
                                Anexo INT(10),
                                Número_Anexo VARCHAR(10),
                                Nombre_Escuela VARCHAR(120),
                                Departamento VARCHAR(45),
                                Localidad VARCHAR(45),
                                zona VARCHAR(20),
                                AMBITO VARCHAR(60),
                                Regional VARCHAR(45),
                                latitud FLOAT(45),
                                longitud FLOAT(45),
                                Matrícula INT(10),
                                Masculinos INT(10),
                                Femeninos INT(10),
                                NSNC INT(10) 
                                )"""