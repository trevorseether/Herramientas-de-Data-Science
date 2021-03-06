USE [master]
GO
IF EXISTS
(
	SELECT name
	FROM sysdatabases
	WHERE name='rh'
)
DROP DATABASE rh
GO
/****** Object:  Database [rh]    Script Date: 16/05/2021 8:08:14 p. m. ******/
CREATE DATABASE [rh]
 ON  PRIMARY 
( NAME = N'rh_dat', FILENAME = N'C:\db\rh_dat.mdf' , SIZE = 30720KB , MAXSIZE = 51200KB , FILEGROWTH = 10240KB )
 LOG ON 
( NAME = N'rh_log', FILENAME = N'C:\db\rh_log.ldf' , SIZE = 10240KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO
USE [rh]
GO
/****** Object:  UserDefinedFunction [dbo].[utf_planilla]    Script Date: 16/05/2021 8:08:14 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[utf_planilla] ( )
RETURNS @planilla TABLE
(
	Codigo int primary key not null,
	Nombre varchar(50) not null,
	[Plan actual] money not null,
	[Plan proyectada] money not null
)
AS
BEGIN
	INSERT INTO @planilla
		SELECT
			d.iddepartamento as codido,
			d.nombre as nombre,
			SUM(e.sueldo) as "planilla actual",
			cast(SUM(e.sueldo * 1.15) as money) as "planilla proyectada"
		FROM dbo.departamento as d
		JOIN dbo.empleado as e
		ON d.iddepartamento = e.iddepartamento
		GROUP BY d.iddepartamento, d.nombre;
	RETURN;
END;
GO
/****** Object:  Table [dbo].[empleado]    Script Date: 16/05/2021 8:08:14 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[empleado](
	[idempleado] [char](5) NOT NULL,
	[apellido] [varchar](50) NOT NULL,
	[nombre] [varchar](50) NOT NULL,
	[fecingreso] [smalldatetime] NOT NULL,
	[email] [varchar](50) NULL,
	[telefono] [varchar](20) NULL,
	[idcargo] [char](3) NOT NULL,
	[iddepartamento] [int] NOT NULL,
	[sueldo] [money] NOT NULL,
	[comision] [money] NULL,
	[jefe] [char](5) NULL,
 CONSTRAINT [pk_empleado] PRIMARY KEY CLUSTERED 
(
	[idempleado] ASC
)
)
GO
/****** Object:  UserDefinedFunction [dbo].[uif_empleados]    Script Date: 16/05/2021 8:08:14 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[uif_empleados] ( @iddepartamento int )
RETURNS TABLE
AS
RETURN
SELECT idempleado, apellido, nombre
FROM dbo.empleado
WHERE iddepartamento = @iddepartamento;
GO
/****** Object:  Table [dbo].[cargo]    Script Date: 16/05/2021 8:08:14 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cargo](
	[idcargo] [char](3) NOT NULL,
	[nombre] [varchar](50) NOT NULL,
	[sueldo_min] [money] NOT NULL,
	[sueldo_max] [money] NOT NULL,
 CONSTRAINT [pk_cargo] PRIMARY KEY CLUSTERED 
(
	[idcargo] ASC
)
)
GO
/****** Object:  Table [dbo].[control]    Script Date: 16/05/2021 8:08:14 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[control](
	[parametro] [varchar](20) NOT NULL,
	[valor] [varchar](20) NOT NULL,
 CONSTRAINT [pk_control] PRIMARY KEY CLUSTERED 
(
	[parametro] ASC
)
)
GO
/****** Object:  Table [dbo].[departamento]    Script Date: 16/05/2021 8:08:14 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[departamento](
	[iddepartamento] [int] NOT NULL,
	[nombre] [varchar](100) NOT NULL,
	[idubicacion] [char](3) NOT NULL,
 CONSTRAINT [pk_departamento] PRIMARY KEY CLUSTERED 
(
	[iddepartamento] ASC
)
)
GO
/****** Object:  Table [dbo].[ubicacion]    Script Date: 16/05/2021 8:08:14 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ubicacion](
	[idubicacion] [char](3) NOT NULL,
	[ciudad] [varchar](50) NOT NULL,
	[direccion] [varchar](100) NOT NULL,
 CONSTRAINT [pk_ubicacion] PRIMARY KEY CLUSTERED 
(
	[idubicacion] ASC
)
)
GO
INSERT [dbo].[cargo] ([idcargo], [nombre], [sueldo_min], [sueldo_max]) VALUES (N'C01', N'Gerente General', 15000.0000, 50000.0000)
INSERT [dbo].[cargo] ([idcargo], [nombre], [sueldo_min], [sueldo_max]) VALUES (N'C02', N'Gerente', 10000.0000, 15000.0000)
INSERT [dbo].[cargo] ([idcargo], [nombre], [sueldo_min], [sueldo_max]) VALUES (N'C03', N'Empleado', 7000.0000, 10000.0000)
INSERT [dbo].[cargo] ([idcargo], [nombre], [sueldo_min], [sueldo_max]) VALUES (N'C04', N'Analista', 5000.0000, 7000.0000)
INSERT [dbo].[cargo] ([idcargo], [nombre], [sueldo_min], [sueldo_max]) VALUES (N'C05', N'Vendedor', 3000.0000, 5000.0000)
INSERT [dbo].[cargo] ([idcargo], [nombre], [sueldo_min], [sueldo_max]) VALUES (N'C06', N'Oficinista', 1500.0000, 3000.0000)
INSERT [dbo].[cargo] ([idcargo], [nombre], [sueldo_min], [sueldo_max]) VALUES (N'C07', N'Programador', 2500.0000, 6000.0000)
INSERT [dbo].[cargo] ([idcargo], [nombre], [sueldo_min], [sueldo_max]) VALUES (N'C08', N'Investigador', 6000.0000, 8000.0000)
INSERT [dbo].[cargo] ([idcargo], [nombre], [sueldo_min], [sueldo_max]) VALUES (N'C09', N'Digitador', 1000.0000, 1500.0000)
INSERT [dbo].[cargo] ([idcargo], [nombre], [sueldo_min], [sueldo_max]) VALUES (N'C10', N'Anfitriona', 1300.0000, 1800.0000)
GO
INSERT [dbo].[control] ([parametro], [valor]) VALUES (N'Cargo', N'10')
INSERT [dbo].[control] ([parametro], [valor]) VALUES (N'Departamento', N'107')
INSERT [dbo].[control] ([parametro], [valor]) VALUES (N'Empleado', N'22')
INSERT [dbo].[control] ([parametro], [valor]) VALUES (N'Empresa', N'PeruDev')
INSERT [dbo].[control] ([parametro], [valor]) VALUES (N'Ubicacion', N'4')
GO
INSERT [dbo].[departamento] ([iddepartamento], [nombre], [idubicacion]) VALUES (100, N'Gerencia', N'U01')
INSERT [dbo].[departamento] ([iddepartamento], [nombre], [idubicacion]) VALUES (101, N'Contabilidad', N'U01')
INSERT [dbo].[departamento] ([iddepartamento], [nombre], [idubicacion]) VALUES (102, N'Investigacion', N'U03')
INSERT [dbo].[departamento] ([iddepartamento], [nombre], [idubicacion]) VALUES (103, N'Ventas', N'U01')
INSERT [dbo].[departamento] ([iddepartamento], [nombre], [idubicacion]) VALUES (104, N'Operaciones', N'U01')
INSERT [dbo].[departamento] ([iddepartamento], [nombre], [idubicacion]) VALUES (105, N'Sistemas', N'U04')
INSERT [dbo].[departamento] ([iddepartamento], [nombre], [idubicacion]) VALUES (106, N'Recursos Humanos', N'U04')
INSERT [dbo].[departamento] ([iddepartamento], [nombre], [idubicacion]) VALUES (107, N'Finanzas', N'U01')
GO
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0001', N'Coronel', N'Gustavo', CAST(N'2000-04-01T00:00:00' AS SmallDateTime), N'gcoronelc@gmail.com', N'996-664-457', N'C01', 100, 25000.0000, NULL, NULL)
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0002', N'Fernandez', N'Claudia', CAST(N'2000-05-01T00:00:00' AS SmallDateTime), N'cfernandez@perudev.com', N'9345-8365', N'C03', 100, 8000.0000, NULL, N'E0001')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0003', N'Matsukawa', N'Sergio', CAST(N'2000-04-01T00:00:00' AS SmallDateTime), N'smatsukawa@perudev.com', N'9772-8369', N'C02', 102, 15000.0000, NULL, N'E0001')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0004', N'Diaz', N'Mariela', CAST(N'2000-04-10T00:00:00' AS SmallDateTime), N'mdiaz@hotmail.com', N'8654-6734', N'C06', 102, 1800.0000, NULL, N'E0003')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0005', N'Martinez', N'Roberto', CAST(N'2000-04-05T00:00:00' AS SmallDateTime), N'rmartinez@perudev.com', NULL, N'C08', 102, 9000.0000, 500.0000, N'E0003')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0006', N'Espinoza', N'Miguel', CAST(N'2000-04-06T00:00:00' AS SmallDateTime), N'mespinoza@perudev.com', N'', N'C08', 102, 7500.0000, 500.0000, N'E0003')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0007', N'Ramos', N'Vanessa', CAST(N'2002-04-06T00:00:00' AS SmallDateTime), N'vramos@yahoo.com', N'9456-3456', N'C08', 102, 7000.0000, 500.0000, N'E0003')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0008', N'Flores', N'Julio', CAST(N'2000-04-01T00:00:00' AS SmallDateTime), N'jflores@perudev.com', NULL, N'C07', 102, 3500.0000, 1000.0000, N'E0003')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0009', N'Marcelo', N'Ricardo', CAST(N'2000-04-01T00:00:00' AS SmallDateTime), N'rmarcelo@perudev.com', N'9936-2966', N'C02', 101, 15000.0000, NULL, N'E0001')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0010', N'Barrios', N'Guisella', CAST(N'2001-01-15T00:00:00' AS SmallDateTime), N'gbarrios@desarrollasoftware.com', N'9023-4512', N'C03', 101, 8000.0000, NULL, N'E0009')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0011', N'Cuellar', N'Lucy', CAST(N'2003-02-18T00:00:00' AS SmallDateTime), N'lcuellar@perudev.com', NULL, N'C06', 101, 2000.0000, NULL, N'E0009')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0012', N'Valencia', N'Hugo', CAST(N'2000-05-01T00:00:00' AS SmallDateTime), N'hvalencia@perudev.pe', N'9732-5601', N'C02', 105, 18000.0000, NULL, N'E0001')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0013', N'Veliz', N'Fortunato', CAST(N'2000-05-05T00:00:00' AS SmallDateTime), N'fveliz@perudev.pe', N'9826-7603', N'C04', 105, 6000.0000, NULL, N'E0012')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0014', N'Aguero', N'Octavio', CAST(N'2000-05-15T00:00:00' AS SmallDateTime), N'oaguero@perudev.pe', NULL, N'C07', 105, 3000.0000, 300.0000, N'E0012')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0015', N'Rosales', N'Cesar', CAST(N'2003-03-15T00:00:00' AS SmallDateTime), N'crosales@perudev.com', NULL, N'C07', 105, 2500.0000, 300.0000, N'E0012')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0016', N'Villarreal', N'Nora', CAST(N'2000-05-01T00:00:00' AS SmallDateTime), N'nvillarreal@soporte.pe', N'9371-3641', N'C02', 103, 15000.0000, NULL, N'E0001')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0017', N'Romero', N'Alejandra', CAST(N'2000-05-03T00:00:00' AS SmallDateTime), N'aromero@perudev.com', N'8345-9526', N'C03', 103, 7500.0000, NULL, N'E0016')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0018', N'Valdiviezo', N'Jennifer', CAST(N'2000-06-12T00:00:00' AS SmallDateTime), N'jvaldiviezo@perudev.com', N'9263-5172', N'C06', 103, 2000.0000, NULL, N'E0016')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0019', N'Muchotrigo', N'Omar', CAST(N'2000-05-12T00:00:00' AS SmallDateTime), N'omuchotrigo@perudev.com', N'9963-5542', N'C05', 103, 3500.0000, 500.0000, N'E0016')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0020', N'Baltazar', N'Victor', CAST(N'2000-05-18T00:00:00' AS SmallDateTime), N'vbaltazar@perudev.com', N'9893-4433', N'C05', 103, 3000.0000, 800.0000, N'E0016')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0021', N'Castillo', N'Ronald', CAST(N'2001-05-18T00:00:00' AS SmallDateTime), N'rcastillo@perudev.com', N'9234-3487', N'C05', 103, 3000.0000, 800.0000, N'E0016')
INSERT [dbo].[empleado] ([idempleado], [apellido], [nombre], [fecingreso], [email], [telefono], [idcargo], [iddepartamento], [sueldo], [comision], [jefe]) VALUES (N'E0022', N'Espilco', N'Luis', CAST(N'2002-04-17T00:00:00' AS SmallDateTime), N'lespilco@perudev.com', N'9554-3456', N'C05', 103, 3000.0000, 300.0000, N'E0016')
GO
INSERT [dbo].[ubicacion] ([idubicacion], [ciudad], [direccion]) VALUES (N'U01', N'Lima', N'Av. Benavides 534 - Miraflores')
INSERT [dbo].[ubicacion] ([idubicacion], [ciudad], [direccion]) VALUES (N'U02', N'Trujillo', N'Calle Primavera 1235 - Cercado')
INSERT [dbo].[ubicacion] ([idubicacion], [ciudad], [direccion]) VALUES (N'U03', N'Arequipa', N'Av. Central 2517 - Cercado')
INSERT [dbo].[ubicacion] ([idubicacion], [ciudad], [direccion]) VALUES (N'U04', N'Lima', N'Av. La Marina 3456 - San Miguel')
GO
ALTER TABLE [dbo].[departamento]  WITH CHECK ADD  CONSTRAINT [fk_departamento_ubicacion] FOREIGN KEY([idubicacion])
REFERENCES [dbo].[ubicacion] ([idubicacion])
GO
ALTER TABLE [dbo].[departamento] CHECK CONSTRAINT [fk_departamento_ubicacion]
GO
ALTER TABLE [dbo].[empleado]  WITH CHECK ADD  CONSTRAINT [fk_empleado_cargo] FOREIGN KEY([idcargo])
REFERENCES [dbo].[cargo] ([idcargo])
GO
ALTER TABLE [dbo].[empleado] CHECK CONSTRAINT [fk_empleado_cargo]
GO
ALTER TABLE [dbo].[empleado]  WITH CHECK ADD  CONSTRAINT [fk_empleado_departamento] FOREIGN KEY([iddepartamento])
REFERENCES [dbo].[departamento] ([iddepartamento])
GO
ALTER TABLE [dbo].[empleado] CHECK CONSTRAINT [fk_empleado_departamento]
GO
ALTER TABLE [dbo].[empleado]  WITH CHECK ADD  CONSTRAINT [fk_empleado_empleado] FOREIGN KEY([jefe])
REFERENCES [dbo].[empleado] ([idempleado])
GO
ALTER TABLE [dbo].[empleado] CHECK CONSTRAINT [fk_empleado_empleado]
GO
USE [master]
GO
ALTER DATABASE [rh] SET  READ_WRITE 
GO
