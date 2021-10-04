USE [master]
GO

IF EXISTS
(
	SELECT name
	FROM sysdatabases
	WHERE name='educa2'
)
DROP DATABASE [educa]
GO

CREATE DATABASE [educa]
 ON  PRIMARY 
(
	NAME = N'educa_dat',
	FILENAME = N'C:\db\educa_dat.mdf',
	SIZE = 30MB,
	MAXSIZE = 50MB,
	FILEGROWTH = 10MB
)
LOG ON 
(
	NAME = N'educa_log',
	FILENAME = N'C:\db\educa_log.ldf',
	SIZE = 10MB,
	MAXSIZE = UNLIMITED,
	FILEGROWTH = 10%
)
GO

USE educa;
GO

-- ======================================================
-- ELIMINA TABLA
-- ======================================================

IF( EXISTS ( SELECT 1 FROM sys.sysobjects 
	WHERE name='PAGO' and xtype = 'u') )
BEGIN
	DROP TABLE dbo.PAGO;
END;
GO

IF( EXISTS ( SELECT 1 FROM sys.sysobjects 
	WHERE name='MATRICULA' and xtype = 'u') )
BEGIN
	DROP TABLE dbo.MATRICULA;
END;
GO

IF( EXISTS ( SELECT 1 FROM sys.sysobjects 
	WHERE name='CURSO' and xtype = 'u') )
BEGIN
	DROP TABLE dbo.CURSO;
END;
GO

IF( EXISTS ( SELECT 1 FROM sys.sysobjects 
	WHERE name='ALUMNO' and xtype = 'u') )
BEGIN
	DROP TABLE dbo.ALUMNO;
END;
GO

-- ======================================================
-- TABLA ALUMNO
-- ======================================================

CREATE TABLE dbo.ALUMNO
( 
	alu_id               INT  NOT NULL ,
	alu_nombre           varchar(100)  NOT NULL ,
	alu_direccion        varchar(100)  NOT NULL ,
	alu_telefono         varchar(20)  NULL ,
	alu_email            varchar(50)  NULL 	
);
GO

-- ======================================================
-- TABLA CURSO
-- ======================================================

CREATE TABLE dbo.CURSO
( 
	cur_id               INT IDENTITY ( 1,1 ) NOT NULL ,
	cur_nombre           varchar(100)  NOT NULL ,
	cur_vacantes         int  NOT NULL ,
	cur_matriculados     int  NOT NULL ,
	cur_profesor         varchar(100)  NULL ,
	cur_precio           money  NOT NULL 
);
GO


-- ======================================================
-- TABLA MATRICULA
-- ======================================================


CREATE TABLE dbo.MATRICULA
( 
	cur_id               INT  NOT NULL ,
	alu_id               INT  NOT NULL ,
	mat_fecha            datetime  NOT NULL ,
	mat_precio           money  NOT NULL ,
	mat_cuotas           int  NOT NULL ,
	mat_nota             int  NULL 
);
GO


-- ======================================================
-- TABLA PAGO
-- ======================================================

CREATE TABLE dbo.PAGO
( 
	cur_id               INT  NOT NULL ,
	alu_id               INT  NOT NULL ,
	pag_cuota            int  NOT NULL ,
	pag_fecha            datetime  NOT NULL ,
	pag_importe          money  NOT NULL 
);
GO

-- ======================================================
-- RESTRICCIONES DE LA TABLA ALUMNO
-- ======================================================

ALTER TABLE dbo.ALUMNO
	ADD CONSTRAINT PK_ALUMNO 
	PRIMARY KEY CLUSTERED (alu_id ASC);
go

ALTER TABLE dbo.ALUMNO
	ADD CONSTRAINT U_ALUMNO_EMAIL 
	UNIQUE (alu_email  ASC);
go

ALTER TABLE dbo.ALUMNO
	ADD CONSTRAINT U_ALUMNO_NOMBRE 
	UNIQUE (alu_nombre  ASC);
go

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES( 1,'YESENIA VIRHUEZ','LOS OLIVOS','986412345','yesenia@hotmail.com');

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES( 2,'OSCAR ALVARADO FERNANDEZ','MIRAFLORES',NULL,'oscar@gmail.com');

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES( 3,'GLADYS REYES CORTIJO','SAN BORJA','875643562','gladys@hotmail.com');

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES( 4,'SARA RIEGA FRIAS','SAN ISIDRO',NULL,'sara@yahoo.com');

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES( 5,'JHON VELASQUEZ DEL CASTILLO','LOS OLIVOS','78645345','jhon@movistar.com');

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES( 6,'RODRIGUEZ ROJAS, RENZO ROBERT','SURCO','673465235','rrodrigiez@gmail.com');

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES( 7,'CALERO MORALES, EMELYN DALILA','LA MOLINA','896754652','ecalero@peru.com');

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES( 8,'KAREN FUENTES','San Isidro','555-5555','KAFUENTES@HOTMAIL.COM');

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES( 9,'Yamina Ruiz','San Isidro','965-4521','yami_ruiz@gmail.com');

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES(10,'MARIA EULALIA VELASQUEZ TORVISCO','SURCO','6573456','mvelasques@gmail.com');

INSERT INTO ALUMNO (alu_id, alu_nombre, alu_direccion, alu_telefono, alu_email )
VALUES(11,'FIORELLA LIZET VITELLA REYES','SAN BORJA','5468790','fvitela@outlook.com');
GO

-- ======================================================
-- RESTRICCIONES DE LA TABLA CURSO
-- ======================================================

-- CLAVE PRIMARIA

ALTER TABLE dbo.CURSO
	ADD CONSTRAINT pk_curso 
	PRIMARY KEY CLUSTERED (cur_id ASC);
go


-- El nombre del curso es �nico

ALTER TABLE dbo.CURSO
	ADD CONSTRAINT u_curso_nombre 
	UNIQUE (cur_nombre  ASC);
go

-- Vacantes mayor que cero

ALTER TABLE dbo.CURSO
	ADD CONSTRAINT  chk_curso_vacantes
		CHECK  ( cur_vacantes > 0 ); 
go

-- Matriculados mayor o igual que cero, y menor o igual que las vacantes

ALTER TABLE dbo.CURSO
	ADD CONSTRAINT  chk_curso_matriculados
		CHECK  ( cur_matriculados >= 0 AND cur_matriculados <= cur_vacantes ) ;
go

-- Precio mayor que cero
ALTER TABLE dbo.CURSO
	ADD CONSTRAINT  chk_curso_precio
		CHECK  ( cur_precio > 0 );
go


-- Matriculados por defecto es CERO

ALTER TABLE dbo.CURSO
	ADD CONSTRAINT DF_CURSO_MATRICULADOS
		 DEFAULT  0 FOR cur_matriculados
go


-- Insertar Datos

SET IDENTITY_INSERT dbo.Curso ON;
GO

INSERT INTO CURSO(CUR_ID,CUR_NOMBRE,CUR_VACANTES,CUR_PRECIO,CUR_PROFESOR)
VALUES(1,'SQL Server Implementaci�n',24,1000.0,'Gustavo coronel');

INSERT INTO CURSO(cur_id,cur_nombre,cur_vacantes,cur_precio,cur_profesor)
VALUES(2,'SQL Server Administraci�n',24,1000.0,' ');

INSERT INTO CURSO(cur_id,cur_nombre,cur_vacantes,cur_precio,cur_profesor)
VALUES(3,'Inteligencia de Negocios',24,1500.0,'Sergio Matsukawa');

INSERT INTO CURSO(cur_id,cur_nombre,cur_vacantes,cur_precio,cur_profesor)
VALUES(4,'Programaci�n Transact-SQL',24,1200.0,NULL);

INSERT INTO CURSO(cur_id,cur_nombre,cur_vacantes,cur_precio,cur_profesor)
VALUES(5,'Java Fundamentos',24,1600.0,'Gustavo Coronel');

INSERT INTO CURSO(cur_id,cur_nombre,cur_vacantes,cur_precio,cur_profesor)
VALUES(6,'Java Cliente-Servidor',24,1600.0,'Gustavo Coronel');

INSERT INTO CURSO(CUR_ID,CUR_NOMBRE,CUR_VACANTES,CUR_PRECIO,CUR_PROFESOR)
VALUES(7,'GESTION DE PROYECTOS',24,2200.0,'RICARDO MARCELO');
GO

SET IDENTITY_INSERT dbo.Curso OFF;
GO


-- ======================================================
-- RESTRICCIONES DE LA TABLA MATRICULA
-- ======================================================

ALTER TABLE dbo.MATRICULA
	ADD CONSTRAINT PK_MATRICULA 
	PRIMARY KEY CLUSTERED (cur_id ASC,alu_id ASC);
go

ALTER TABLE dbo.MATRICULA
	ADD CONSTRAINT FK_MATRICULA_CURSO 
	FOREIGN KEY (cur_id) 
	REFERENCES dbo.CURSO(cur_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION;
GO

ALTER TABLE dbo.MATRICULA
	ADD CONSTRAINT FK_MATRICULA_ALUMNO 
	FOREIGN KEY (alu_id) 
	REFERENCES dbo.ALUMNO(alu_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION;
go


ALTER TABLE dbo.MATRICULA
	ADD CONSTRAINT  CHK_MATRICULA_PRECIO
		CHECK  ( MAT_PRECIO > 0.0 );
go

ALTER TABLE dbo.MATRICULA
	ADD CONSTRAINT  CHK_MATRICULA_CUOTAS
		CHECK  ( MAT_CUOTAS > 0 );
go

ALTER TABLE dbo.MATRICULA
	ADD CONSTRAINT  CHK_MATRICULA_NOTA
		CHECK  ( (MAT_NOTA = NULL) OR (MAT_NOTA BETWEEN 0 AND 20) );
go




SET DATEFORMAT DMY
GO

DECLARE @ANIO VARCHAR(10);
SET @ANIO =  cast(year(getdate()) as varchar);

INSERT INTO dbo.MATRICULA ( cur_id, alu_id, mat_fecha, mat_precio, mat_cuotas, mat_nota ) 
VALUES(1, 5,'15-04-' + @ANIO +' 10:30',800.0,1,15);

INSERT INTO dbo.MATRICULA ( cur_id, alu_id, mat_fecha, mat_precio, mat_cuotas, mat_nota ) 
VALUES(1, 3,'16-04-' + @ANIO +' 11:45',1000.0,2,18);

INSERT INTO dbo.MATRICULA ( cur_id, alu_id, mat_fecha, mat_precio, mat_cuotas, mat_nota ) 
VALUES(1, 4,'18-04-' +@ANIO +' 08:33',1200.0,3,12);

INSERT INTO dbo.MATRICULA ( cur_id, alu_id, mat_fecha, mat_precio, mat_cuotas, mat_nota ) 
VALUES(2, 1,'15-04-' + @ANIO +' 12:33',800.0,1,16);

INSERT INTO dbo.MATRICULA ( cur_id, alu_id, mat_fecha, mat_precio, mat_cuotas, mat_nota ) 
VALUES(2, 2,'01-05-' + @ANIO +' 15:34',1000.0,2,10);

INSERT INTO dbo.MATRICULA ( cur_id, alu_id, mat_fecha, mat_precio, mat_cuotas, mat_nota ) 
VALUES(2, 3,'03-05-' + @ANIO +' 16:55',1300.0,3,14);

INSERT INTO dbo.MATRICULA ( cur_id, alu_id, mat_fecha, mat_precio, mat_cuotas, mat_nota ) 
VALUES(2, 4,'04-05-' + @ANIO +' 17:00',400.0,1,18);

INSERT INTO dbo.MATRICULA ( cur_id, alu_id, mat_fecha, mat_precio, mat_cuotas, mat_nota ) 
VALUES(2, 5,'06-05-' + @ANIO +' 13:12',750.0,1,17);

INSERT INTO dbo.MATRICULA ( cur_id, alu_id, mat_fecha, mat_precio, mat_cuotas, mat_nota ) 
VALUES(3, 7,'02-06-' + @ANIO +' 13:12',950.0,2,15);

GO


-- ======================================================
-- Actualizar la columna matriculados en la tabla curso
-- ======================================================

UPDATE dbo.CURSO
SET cur_matriculados = (
	SELECT COUNT(*) FROM dbo.MATRICULA
	WHERE dbo.MATRICULA.cur_id = dbo.CURSO.cur_id );
GO

-- ======================================================
-- RESTRICCIONES EN LA TABLA PAGO
-- ======================================================

-- Clave Primaria

ALTER TABLE dbo.PAGO
	ADD CONSTRAINT PK_PAGO 
	PRIMARY KEY CLUSTERED (cur_id ASC,alu_id ASC,pag_cuota ASC);
go

-- Clave For�nea

ALTER TABLE dbo.PAGO
	ADD CONSTRAINT FK_PAGO_MATRICULA 
	FOREIGN KEY (cur_id,alu_id) 
	REFERENCES dbo.MATRICULA(cur_id,alu_id)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
go

-- Cargar Datos

set dateformat dmy
go

declare @anio varchar(10)
set @anio = cast(year(getdate()) as varchar)
insert into dbo.PAGO values(1,3,1,'16-04-' + @anio,500)
insert into dbo.PAGO values(1,3,2,'16-05-' + @anio,500)
insert into dbo.PAGO values(1,4,1,'18-04-' + @anio,400)
insert into dbo.PAGO values(1,4,2,'18-05-' + @anio,400)
insert into dbo.PAGO values(2,1,1,'15-04-' + @anio,800)
insert into dbo.PAGO values(2,2,1,'01-05-' + @anio,500)
insert into dbo.PAGO values(2,3,1,'03-05-' + @anio,430)
insert into dbo.PAGO values(2,3,2,'03-06-' + @anio,430)
insert into dbo.PAGO values(2,4,1,'04-05-' + @anio,400)
insert into dbo.PAGO values(2,5,1,'06-05-' + @anio,750)
go


-- ======================================================
-- FIN
-- ======================================================

-- ======================================================
-- TABLA MATRICULA
-- ======================================================

USE EDUCA;
GO

CREATE TABLE dbo.NUEVOS_ALUMNOS(
	alu_nombre VARCHAR(100) NOT NULL,
	alu_direccion VARCHAR(100) NOT NULL,
	alu_telefono VARCHAR(20) NULL,
	alu_email VARCHAR(50) NULL
);
GO


INSERT INTO dbo.NUEVOS_ALUMNOS(alu_nombre,alu_direccion, alu_telefono, alu_email)
VALUES( 'YESENIA VIRHUEZ','LA MOLINA','897678567','yesenia@hotmail.com');
go

INSERT INTO dbo.NUEVOS_ALUMNOS(alu_nombre,alu_direccion, alu_telefono, alu_email)
VALUES( 'GLADYS REYES CORTIJO','SAN MIGUEL','456879023','gladys@hotmail.com')
go

INSERT INTO dbo.NUEVOS_ALUMNOS(alu_nombre,alu_direccion, alu_telefono, alu_email) 
VALUES( 'GABRIEL FLORES ARROYO','SAN MIGUEL','435679456','gabriel@gmail.com')
go

INSERT INTO dbo.NUEVOS_ALUMNOS(alu_nombre,alu_direccion, alu_telefono, alu_email) 
VALUES( 'LUIS ROJAS CASTRO','LOS OLIVOS','546784768','lrojas@hotmail.com')
go

INSERT INTO dbo.NUEVOS_ALUMNOS(alu_nombre,alu_direccion, alu_telefono, alu_email) 
VALUES( 'WILLY SANCHEZ CACHAY','SAN ISIDRO','345879567','wsanchez@gmail.com')
go

INSERT INTO dbo.NUEVOS_ALUMNOS(alu_nombre,alu_direccion, alu_telefono, alu_email) 
VALUES( 'SANDRA SOLER GARCIA','SURCO','967435672','ssoler@gmail.com')
go

select * from dbo.NUEVOS_ALUMNOS;
go
select * from dbo.ALUMNO
select * from dbo.CURSO
select * from dbo.MATRICULA
select * from dbo.PAGO
go
