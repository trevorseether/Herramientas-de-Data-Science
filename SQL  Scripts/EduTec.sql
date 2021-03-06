USE [master]
GO

IF EXISTS
(
	SELECT name
	FROM sysdatabases
	WHERE name='EduTec'
)
DROP DATABASE [EduTec]
GO

CREATE DATABASE [EduTec]
 ON  PRIMARY 
(
	NAME = N'EduTec_dat',
	FILENAME = N'C:\db\EduTec_dat.mdf',
	SIZE = 30MB,
	MAXSIZE = 50MB,
	FILEGROWTH = 10MB
)
LOG ON 
(
	NAME = N'EduTec_log',
	FILENAME = N'C:\db\EduTec_log.ldf',
	SIZE = 10MB,
	MAXSIZE = UNLIMITED,
	FILEGROWTH = 10%
)
GO
USE [EduTec]
GO
/****** Object:  Table [dbo].[Tarifa]    Script Date: 03/26/2020 17:14:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Tarifa](
	[IdTarifa] [char](1) NOT NULL,
	[PreTarifa] [money] NOT NULL,
	[Descripcion] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[IdTarifa] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[Tarifa] ([IdTarifa], [PreTarifa], [Descripcion]) VALUES (N'A', 200.0000, N'Herramientas de Oficina')
INSERT [dbo].[Tarifa] ([IdTarifa], [PreTarifa], [Descripcion]) VALUES (N'B', 250.0000, N'SoftWare de Desarrollo - Basico')
INSERT [dbo].[Tarifa] ([IdTarifa], [PreTarifa], [Descripcion]) VALUES (N'C', 300.0000, N'SoftWare de Desarrollo - Intermedio/Avanzado')
INSERT [dbo].[Tarifa] ([IdTarifa], [PreTarifa], [Descripcion]) VALUES (N'D', 350.0000, N'Sistemas Operativos - Intermedio/Avanzado')
INSERT [dbo].[Tarifa] ([IdTarifa], [PreTarifa], [Descripcion]) VALUES (N'E', 350.0000, N'Administradores de Bases de Datos')
/****** Object:  Table [dbo].[Profesor]    Script Date: 03/26/2020 17:14:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Profesor](
	[IdProfesor] [char](4) NOT NULL,
	[ApeProfesor] [varchar](30) NOT NULL,
	[NomProfesor] [varchar](30) NOT NULL,
	[DirProfesor] [varchar](50) NULL,
	[TelProfesor] [varchar](12) NULL,
	[EmailProfesor] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[IdProfesor] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P001', N'Valencia Morales', N'Pedro Hugo', N'Magdalena', N'None', N'hugovm@terra.com.pe')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P002', N'Coronel Castillo', N'Eric Gustavo', N'Los Olivos', N'None', N'gcoronel@uni.edu.pe')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P003', N'Diaz Vilela', N'Pedro Pablo', N'Rimac', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P004', N'Matsukawa Maeda', N'Sergio', N'Bella Vista', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P005', N'Bustamante Gutierrez', N'Cesar Augusto', N'Lince', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P006', N'Henostroza Macedo', N'Guino', N'Los Olivos', N'None', N'guino@telematic.edu.pe')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P007', N'Flores Manco', N'Julio Enrrique', N'Los Olivos', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P008', N'Bardon Mayta', N'Julio Cesar', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P009', N'Allauca Paucar', N'Juan Jose', N'Los Olivos', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P010', N'Serna Jherry', N'Jose Luis', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P011', N'Chuco Barrera', N'Raul', N'Rimac', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P012', N'Alegre Mendoza', N'Jose', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P013', N'Quispe Tineo', N'Cesar', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P014', N'Ramirez Salvador', N'Julio', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P015', N'Chuquin Espinoza', N'Willian', N'Lince', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P016', N'Rosas Ayala', N'Dario', N'Rimac', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P017', N'Rodriguez Villacorta', N'Manuel', N'Lima', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P018', N'Zegarra Zavaleta', N'Tereza', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P019', N'Guzman Azcurra', N'Manuel', N'Rimac', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P020', N'Zegarra Zavaleta', N'Daniel', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P021', N'Cueva Contreras', N'Martin', N'Rimac', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P022', N'Lostaunau Navarro', N'Alberto', N'Lima', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P023', N'Condor Ortiz', N'Saul', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P024', N'Ganoza Zelada', N'David', N'Comas', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P025', N'Fabian Avila', N'Dionicio', N'Comas', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P026', N'Quintana Saenz', N'Jorge', N'Rimac', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P027', N'Yupanqui Villegas', N'Juan', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P028', N'Yupanqui Villegas', N'Julio', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P029', N'Alcantara Cerna', N'Violeta', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P030', N'Oceda Samaniego', N'Cesar Miguel', N'San Miguel', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P031', N'Becerra Flores', N'Ursula', N'San Miguel', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P032', N'Marcelo Villalobos', N'Marvin', N'Lince', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P033', N'Narvaez Garcia', N'Victor', N'Lima', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P034', N'Reynoso Zarate', N'Jose', N'Los Olivos', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P035', N'Suarez Valenzuela', N'Misael', N'Lima', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P036', N'Carrasco Muñoz', N'Joel', N'', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P037', N'Salcedo Martinez', N'Percy', N'Lima', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P038', N'Vasquez Valenzuela', N'Javier', N'Comas', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P039', N'Herrera Huanca', N'Javier', N'Comas', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P040', N'Marcelo Villalobos', N'Ricardo', N'SMP', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P041', N'Quiroz Villon', N'Edgar', N'Rimac', N'None', N'None')
INSERT [dbo].[Profesor] ([IdProfesor], [ApeProfesor], [NomProfesor], [DirProfesor], [TelProfesor], [EmailProfesor]) VALUES (N'P042', N'Veliz', N'Fortumato', N'La Molina', N'None', N'None')
/****** Object:  Table [dbo].[Parametro]    Script Date: 03/26/2020 17:14:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Parametro](
	[Campo] [varchar](10) NOT NULL,
	[Contador] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Campo] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[Parametro] ([Campo], [Contador]) VALUES (N'Anno', 2013)
INSERT [dbo].[Parametro] ([Campo], [Contador]) VALUES (N'IdAlumno', 31)
INSERT [dbo].[Parametro] ([Campo], [Contador]) VALUES (N'IdCurso', 12)
INSERT [dbo].[Parametro] ([Campo], [Contador]) VALUES (N'IdProfesor', 43)
INSERT [dbo].[Parametro] ([Campo], [Contador]) VALUES (N'NroCiclo', 5)
/****** Object:  Table [dbo].[Ciclo]    Script Date: 03/26/2020 17:14:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Ciclo](
	[IdCiclo] [char](7) NOT NULL,
	[FecInicio] [datetime] NULL,
	[FecTermino] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[IdCiclo] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2012-01', CAST(0x00009FD900000000 AS DateTime), CAST(0x00009FFD00000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2012-02', CAST(0x00009FFD00000000 AS DateTime), CAST(0x0000A01F00000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2012-03', CAST(0x0000A02A00000000 AS DateTime), CAST(0x0000A04D00000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2012-04', CAST(0x0000A05200000000 AS DateTime), CAST(0x0000A07600000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2012-05', CAST(0x0000A07700000000 AS DateTime), CAST(0x0000A09600000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2012-06', CAST(0x0000A0A000000000 AS DateTime), CAST(0x0000A0BD00000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2012-07', CAST(0x0000A0C300000000 AS DateTime), CAST(0x0000A0E100000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2012-08', CAST(0x0000A0E200000000 AS DateTime), CAST(0x0000A10300000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2012-09', CAST(0x0000A10500000000 AS DateTime), CAST(0x0000A12500000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2013-01', CAST(0x0000A14200000000 AS DateTime), CAST(0x0000A16600000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2013-02', CAST(0x0000A16900000000 AS DateTime), CAST(0x0000A18700000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2013-03', CAST(0x0000A18900000000 AS DateTime), CAST(0x0000A1AB00000000 AS DateTime))
INSERT [dbo].[Ciclo] ([IdCiclo], [FecInicio], [FecTermino]) VALUES (N'2013-04', CAST(0x0000A1AC00000000 AS DateTime), CAST(0x0000A1CC00000000 AS DateTime))
/****** Object:  Table [dbo].[Alumno]    Script Date: 03/26/2020 17:14:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Alumno](
	[IdAlumno] [char](5) NOT NULL,
	[ApeAlumno] [varchar](30) NOT NULL,
	[NomAlumno] [varchar](30) NOT NULL,
	[DirAlumno] [varchar](50) NULL,
	[TelAlumno] [varchar](12) NULL,
	[EmailAlumno] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[IdAlumno] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0001', N'Donayre Mena', N'Christian', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0002', N'Ortiz Rodriguez', N'Freddy', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0003', N'Silva Mejia', N'Ruth Ketty', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0004', N'Melendez Noriega', N'Liliana', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0005', N'Huerta Leon', N'Silvia', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0006', N'Carranza Fuentes', N'Maria Elena', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0007', N'Prado Castro', N'Gabriela', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0008', N'Atuncar Mesias', N'Juan', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0009', N'Aguilar Zavala', N'Patricia Elena', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0010', N'Rodruigez Trujillo', N'Rubén Eduardo', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0011', N'Canales Ruiz', N'Gino Leonel', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0012', N'Ruiz Quispe', N'Edgar', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0013', N'PanduroTerrazas', N'Omar', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0014', N'Zita Padilla', N'Peter Wilmer', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0015', N'Ternero Ubillús', N'Luis', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0016', N'Rivera García', N'Raúl Joel', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0017', N'Pomar García', N'Ana', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0018', N'Palomares Venegas', N'Mercedes', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0019', N'Ruiz Venegaz', N'Luis Alberto', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0020', N'Tejada Bernal', N'Janet', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0021', N'Sotelo Canales', N'Juan Carlos', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0022', N'LLosa Montalvan', N'Karla', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0023', N'Galarza Torres', N'Hugo', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0024', N'Valverde Jaramillo', N'Saul', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0025', N'Cipriano Avila', N'Roxana', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0026', N'Rodriguez Quispe', N'Luis Alberto', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0027', N'Huerta Leon', N'Marco Antonio', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0028', N'Ortiz Fuentes', N'Ana María', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0029', N'Rivera Jaramillo', N'Martha', NULL, NULL, NULL)
INSERT [dbo].[Alumno] ([IdAlumno], [ApeAlumno], [NomAlumno], [DirAlumno], [TelAlumno], [EmailAlumno]) VALUES (N'A0030', N'Bustamante Campos', N'Guino', NULL, NULL, NULL)
/****** Object:  Table [dbo].[Empleado]    Script Date: 03/26/2020 17:14:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Empleado](
	[IdEmpleado] [char](6) NOT NULL,
	[Password] [char](6) NOT NULL,
	[ApeEmpleado] [varchar](30) NOT NULL,
	[NomEmpleado] [varchar](30) NOT NULL,
	[Cargo] [varchar](25) NOT NULL,
	[DirEmpleado] [varchar](50) NULL,
	[TelEmpleado] [varchar](12) NULL,
	[EmailEmpleado] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[IdEmpleado] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[Empleado] ([IdEmpleado], [Password], [ApeEmpleado], [NomEmpleado], [Cargo], [DirEmpleado], [TelEmpleado], [EmailEmpleado]) VALUES (N'acampo', N'acampo', N'Campos Huapaya', N'Alberto', N'Jefe de Seguridad', NULL, NULL, NULL)
INSERT [dbo].[Empleado] ([IdEmpleado], [Password], [ApeEmpleado], [NomEmpleado], [Cargo], [DirEmpleado], [TelEmpleado], [EmailEmpleado]) VALUES (N'beteta', N'beteta', N'Beteta Bustamante', N'Cesar', N'Gerente General', NULL, NULL, NULL)
INSERT [dbo].[Empleado] ([IdEmpleado], [Password], [ApeEmpleado], [NomEmpleado], [Cargo], [DirEmpleado], [TelEmpleado], [EmailEmpleado]) VALUES (N'jmanrr', N'jmanrr', N'Manrique Diaz', N'José Luis', N'Coordinador Academico', NULL, NULL, NULL)
INSERT [dbo].[Empleado] ([IdEmpleado], [Password], [ApeEmpleado], [NomEmpleado], [Cargo], [DirEmpleado], [TelEmpleado], [EmailEmpleado]) VALUES (N'jramir', N'jramir', N'Ramirez Salvador', N'Julio Cesar', N'Administrador General', NULL, NULL, NULL)
INSERT [dbo].[Empleado] ([IdEmpleado], [Password], [ApeEmpleado], [NomEmpleado], [Cargo], [DirEmpleado], [TelEmpleado], [EmailEmpleado]) VALUES (N'lcastr', N'lcastr', N'Castro Escobar', N'Lidia Rosa', N'Secretaria General', NULL, NULL, NULL)
INSERT [dbo].[Empleado] ([IdEmpleado], [Password], [ApeEmpleado], [NomEmpleado], [Cargo], [DirEmpleado], [TelEmpleado], [EmailEmpleado]) VALUES (N'psalce', N'psalce', N'Salcedo Banderas', N'Percy', N'Gerente Ventas', NULL, NULL, NULL)
/****** Object:  Table [dbo].[Curso]    Script Date: 03/26/2020 17:14:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Curso](
	[IdCurso] [char](4) NOT NULL,
	[IdTarifa] [char](1) NOT NULL,
	[NomCurso] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[IdCurso] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C001', N'A', N'Windows 8')
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C002', N'B', N'MS Visual Basic.Net - Fundamentos')
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C003', N'C', N'MS Visual Basic.Net - Bases de Datos')
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C004', N'C', N'MS Visual Basic.Net - Componentes')
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C005', N'B', N'Modelamiento de Datos')
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C006', N'C', N'Diseño de Sistemas con UML')
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C007', N'C', N'Taller de Sistemas')
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C008', N'C', N'SQL Server IV - BI')
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C009', N'B', N'SQL Server I')
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C010', N'C', N'SQL Server II - Programación')
INSERT [dbo].[Curso] ([IdCurso], [IdTarifa], [NomCurso]) VALUES (N'C011', N'C', N'SQL Server III - Administracion')
/****** Object:  Table [dbo].[CursoProgramado]    Script Date: 03/26/2020 17:14:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[CursoProgramado](
	[IdCursoProg] [int] IDENTITY(1,1) NOT NULL,
	[IdCurso] [char](4) NOT NULL,
	[IdCiclo] [char](7) NOT NULL,
	[IdProfesor] [char](4) NULL,
	[Vacantes] [tinyint] NOT NULL,
	[PreCursoProg] [money] NOT NULL,
	[Horario] [varchar](24) NOT NULL,
	[Activo] [bit] NULL,
	[Matriculados] [tinyint] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[IdCursoProg] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
SET IDENTITY_INSERT [dbo].[CursoProgramado] ON
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (1, N'C001', N'2012-01', N'P003', 10, 200.0000, N'Lu y Mi 19-22 Horas', 1, 10)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (2, N'C002', N'2012-01', N'P002', 10, 250.0000, N'Mi y Vi 19-22 Horas', 1, 10)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (3, N'C003', N'2012-01', N'P005', 10, 300.0000, N'Ma y Ju 19-22 Horas', 1, 10)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (4, N'C004', N'2012-01', N'P001', 10, 300.0000, N'Ju y Sa 19-22 Horas', 1, 10)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (5, N'C005', N'2012-01', N'P001', 10, 250.0000, N'Lu y Mi 19-22 Horas', 1, 10)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (6, N'C006', N'2012-01', N'P002', 20, 300.0000, N'Ma y Ju 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (7, N'C007', N'2012-01', N'P004', 20, 300.0000, N'Mi y Vi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (8, N'C008', N'2012-01', N'P004', 20, 300.0000, N'Ma y Ju 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (9, N'C009', N'2012-01', N'P002', 20, 250.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (10, N'C010', N'2012-01', N'P002', 20, 300.0000, N'Ju y Sa 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (11, N'C011', N'2012-01', N'P002', 20, 300.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (12, N'C001', N'2012-02', N'P003', 10, 200.0000, N'Lu y Mi 19-22 Horas', 1, 10)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (13, N'C002', N'2012-02', N'P002', 10, 250.0000, N'Mi y Vi 19-22 Horas', 1, 10)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (14, N'C003', N'2012-02', N'P005', 10, 300.0000, N'Ma y Ju 19-22 Horas', 0, 10)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (15, N'C004', N'2012-02', N'P001', 10, 300.0000, N'Ju y Sa 19-22 Horas', 1, 10)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (16, N'C005', N'2012-02', N'P001', 10, 250.0000, N'Lu y Mi 19-22 Horas', 1, 10)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (17, N'C006', N'2012-02', N'P002', 20, 300.0000, N'Ma y Ju 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (18, N'C007', N'2012-02', N'P004', 20, 300.0000, N'Mi y Vi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (19, N'C008', N'2012-02', N'P004', 20, 300.0000, N'Ma y Ju 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (20, N'C009', N'2012-02', N'P002', 20, 250.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (21, N'C010', N'2012-02', N'P002', 20, 300.0000, N'Ju y Sa 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (22, N'C011', N'2012-02', N'P002', 20, 300.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (23, N'C001', N'2012-03', N'P003', 20, 200.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (24, N'C002', N'2012-03', N'P002', 20, 250.0000, N'Mi y Vi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (25, N'C003', N'2012-03', N'P005', 20, 300.0000, N'Ma y Ju 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (26, N'C004', N'2012-03', N'P001', 20, 300.0000, N'Ju y Sa 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (27, N'C005', N'2012-03', N'P001', 20, 250.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (28, N'C006', N'2012-03', N'P002', 20, 300.0000, N'Ma y Ju 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (29, N'C007', N'2012-03', N'P004', 20, 300.0000, N'Mi y Vi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (30, N'C008', N'2012-03', N'P004', 20, 300.0000, N'Ma y Ju 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (31, N'C009', N'2012-03', N'P002', 20, 250.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (32, N'C010', N'2012-03', N'P002', 20, 300.0000, N'Ju y Sa 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (33, N'C011', N'2012-03', N'P002', 20, 300.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (34, N'C001', N'2012-04', N'P003', 20, 200.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (35, N'C002', N'2012-04', N'P002', 20, 250.0000, N'Mi y Vi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (36, N'C003', N'2012-04', N'P005', 20, 300.0000, N'Ma y Ju 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (37, N'C004', N'2012-04', N'P001', 20, 300.0000, N'Ju y Sa 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (38, N'C005', N'2012-04', N'P001', 20, 250.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (39, N'C006', N'2012-04', N'P002', 20, 300.0000, N'Ma y Ju 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (40, N'C007', N'2012-04', N'P004', 20, 300.0000, N'Mi y Vi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (41, N'C008', N'2012-04', N'P004', 20, 300.0000, N'Ma y Ju 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (42, N'C009', N'2012-04', N'P002', 20, 250.0000, N'Lu y Mi 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (43, N'C010', N'2012-04', N'P002', 20, 300.0000, N'Ju y Sa 19-22 Horas', 1, 0)
INSERT [dbo].[CursoProgramado] ([IdCursoProg], [IdCurso], [IdCiclo], [IdProfesor], [Vacantes], [PreCursoProg], [Horario], [Activo], [Matriculados]) VALUES (44, N'C011', N'2012-04', N'P002', 20, 300.0000, N'Lu y Mi 19-22 Horas', 1, 0)
SET IDENTITY_INSERT [dbo].[CursoProgramado] OFF
/****** Object:  Table [dbo].[Matricula]    Script Date: 03/26/2020 17:14:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Matricula](
	[IdCursoProg] [int] NOT NULL,
	[IdAlumno] [char](5) NOT NULL,
	[FecMatricula] [datetime] NOT NULL,
	[ExaParcial] [real] NULL,
	[ExaFinal] [real] NULL,
	[Promedio] [real] NULL,
	[Subsanacion] [bit] NULL,
	[ExaSub] [real] NULL,
PRIMARY KEY CLUSTERED 
(
	[IdCursoProg] ASC,
	[IdAlumno] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (1, N'A0001', CAST(0x00009FCD00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (1, N'A0002', CAST(0x00009FCD00000000 AS DateTime), 10, 14, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (1, N'A0003', CAST(0x00009FCD00000000 AS DateTime), 13, 15, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (1, N'A0004', CAST(0x00009FCD00000000 AS DateTime), 9, 11, 10, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (1, N'A0005', CAST(0x00009FCD00000000 AS DateTime), 15, 19, 17, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (1, N'A0006', CAST(0x00009FCE00000000 AS DateTime), 11, 13, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (1, N'A0007', CAST(0x00009FCE00000000 AS DateTime), 7, 9, 8, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (1, N'A0008', CAST(0x00009FCE00000000 AS DateTime), 13, 15, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (1, N'A0009', CAST(0x00009FCE00000000 AS DateTime), 17, 19, 18, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (1, N'A0010', CAST(0x00009FCE00000000 AS DateTime), 12, 16, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (2, N'A0011', CAST(0x00009FCD00000000 AS DateTime), 14, 16, 15, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (2, N'A0012', CAST(0x00009FCD00000000 AS DateTime), 12, 14, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (2, N'A0013', CAST(0x00009FCD00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (2, N'A0014', CAST(0x00009FCD00000000 AS DateTime), 9, 11, 10, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (2, N'A0015', CAST(0x00009FCD00000000 AS DateTime), 8, 10, 9, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (2, N'A0016', CAST(0x00009FCE00000000 AS DateTime), 12, 16, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (2, N'A0017', CAST(0x00009FCE00000000 AS DateTime), 11, 13, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (2, N'A0018', CAST(0x00009FCE00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (2, N'A0019', CAST(0x00009FCE00000000 AS DateTime), 14, 16, 15, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (2, N'A0020', CAST(0x00009FCE00000000 AS DateTime), 13, 15, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (3, N'A0021', CAST(0x00009FCD00000000 AS DateTime), 9, 11, 10, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (3, N'A0022', CAST(0x00009FCD00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (3, N'A0023', CAST(0x00009FCD00000000 AS DateTime), 11, 13, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (3, N'A0024', CAST(0x00009FCD00000000 AS DateTime), 10, 16, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (3, N'A0025', CAST(0x00009FCD00000000 AS DateTime), 5, 17, 11, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (3, N'A0026', CAST(0x00009FCE00000000 AS DateTime), 9, 15, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (3, N'A0027', CAST(0x00009FCE00000000 AS DateTime), 14, 16, 15, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (3, N'A0028', CAST(0x00009FCE00000000 AS DateTime), 13, 17, 15, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (3, N'A0029', CAST(0x00009FCE00000000 AS DateTime), 15, 19, 17, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (3, N'A0030', CAST(0x00009FCE00000000 AS DateTime), 18, 14, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (4, N'A0001', CAST(0x00009FCD00000000 AS DateTime), 13, 15, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (4, N'A0003', CAST(0x00009FCD00000000 AS DateTime), 10, 16, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (4, N'A0005', CAST(0x00009FCD00000000 AS DateTime), 16, 12, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (4, N'A0007', CAST(0x00009FCD00000000 AS DateTime), 14, 12, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (4, N'A0009', CAST(0x00009FCD00000000 AS DateTime), 18, 12, 15, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (4, N'A0011', CAST(0x00009FCE00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (4, N'A0013', CAST(0x00009FCE00000000 AS DateTime), 12, 16, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (4, N'A0015', CAST(0x00009FCE00000000 AS DateTime), 10, 16, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (4, N'A0017', CAST(0x00009FCE00000000 AS DateTime), 11, 15, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (4, N'A0019', CAST(0x00009FCE00000000 AS DateTime), 9, 15, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (5, N'A0002', CAST(0x00009FCD00000000 AS DateTime), 12, 14, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (5, N'A0004', CAST(0x00009FCD00000000 AS DateTime), 15, 13, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (5, N'A0006', CAST(0x00009FCD00000000 AS DateTime), 12, 16, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (5, N'A0008', CAST(0x00009FCD00000000 AS DateTime), 8, 14, 11, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (5, N'A0010', CAST(0x00009FCD00000000 AS DateTime), 11, 15, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (5, N'A0012', CAST(0x00009FCE00000000 AS DateTime), 13, 15, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (5, N'A0014', CAST(0x00009FCE00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (5, N'A0016', CAST(0x00009FCE00000000 AS DateTime), 17, 19, 18, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (5, N'A0018', CAST(0x00009FCE00000000 AS DateTime), 13, 11, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (5, N'A0020', CAST(0x00009FCE00000000 AS DateTime), 12, 16, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (12, N'A0001', CAST(0x00009FCD00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (12, N'A0002', CAST(0x00009FCD00000000 AS DateTime), 10, 14, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (12, N'A0003', CAST(0x00009FCD00000000 AS DateTime), 13, 15, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (12, N'A0004', CAST(0x00009FCD00000000 AS DateTime), 9, 11, 10, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (12, N'A0005', CAST(0x00009FCD00000000 AS DateTime), 15, 19, 17, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (12, N'A0006', CAST(0x00009FCE00000000 AS DateTime), 11, 13, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (12, N'A0007', CAST(0x00009FCE00000000 AS DateTime), 7, 9, 8, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (12, N'A0008', CAST(0x00009FCE00000000 AS DateTime), 13, 15, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (12, N'A0009', CAST(0x00009FCE00000000 AS DateTime), 17, 19, 18, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (12, N'A0010', CAST(0x00009FCE00000000 AS DateTime), 12, 16, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (13, N'A0011', CAST(0x00009FCD00000000 AS DateTime), 14, 16, 15, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (13, N'A0012', CAST(0x00009FCD00000000 AS DateTime), 12, 14, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (13, N'A0013', CAST(0x00009FCD00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (13, N'A0014', CAST(0x00009FCD00000000 AS DateTime), 9, 11, 10, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (13, N'A0015', CAST(0x00009FCD00000000 AS DateTime), 8, 10, 9, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (13, N'A0016', CAST(0x00009FCE00000000 AS DateTime), 12, 16, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (13, N'A0017', CAST(0x00009FCE00000000 AS DateTime), 11, 13, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (13, N'A0018', CAST(0x00009FCE00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (13, N'A0019', CAST(0x00009FCE00000000 AS DateTime), 14, 16, 15, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (13, N'A0020', CAST(0x00009FCE00000000 AS DateTime), 13, 15, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (14, N'A0021', CAST(0x00009FCD00000000 AS DateTime), 9, 11, 10, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (14, N'A0022', CAST(0x00009FCD00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (14, N'A0023', CAST(0x00009FCD00000000 AS DateTime), 11, 13, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (14, N'A0024', CAST(0x00009FCD00000000 AS DateTime), 10, 16, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (14, N'A0025', CAST(0x00009FCD00000000 AS DateTime), 5, 17, 11, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (14, N'A0026', CAST(0x00009FCE00000000 AS DateTime), 9, 15, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (14, N'A0027', CAST(0x00009FCE00000000 AS DateTime), 14, 16, 15, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (14, N'A0028', CAST(0x00009FCE00000000 AS DateTime), 13, 17, 15, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (14, N'A0029', CAST(0x00009FCE00000000 AS DateTime), 15, 19, 17, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (14, N'A0030', CAST(0x00009FCE00000000 AS DateTime), 18, 14, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (15, N'A0001', CAST(0x00009FCD00000000 AS DateTime), 13, 15, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (15, N'A0003', CAST(0x00009FCD00000000 AS DateTime), 10, 16, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (15, N'A0005', CAST(0x00009FCD00000000 AS DateTime), 16, 12, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (15, N'A0007', CAST(0x00009FCD00000000 AS DateTime), 14, 12, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (15, N'A0009', CAST(0x00009FCD00000000 AS DateTime), 18, 12, 15, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (15, N'A0011', CAST(0x00009FCE00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (15, N'A0013', CAST(0x00009FCE00000000 AS DateTime), 12, 16, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (15, N'A0015', CAST(0x00009FCE00000000 AS DateTime), 10, 16, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (15, N'A0017', CAST(0x00009FCE00000000 AS DateTime), 11, 15, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (15, N'A0019', CAST(0x00009FCE00000000 AS DateTime), 9, 15, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (16, N'A0002', CAST(0x00009FCD00000000 AS DateTime), 12, 14, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (16, N'A0004', CAST(0x00009FCD00000000 AS DateTime), 15, 13, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (16, N'A0006', CAST(0x00009FCD00000000 AS DateTime), 12, 16, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (16, N'A0008', CAST(0x00009FCD00000000 AS DateTime), 8, 14, 11, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (16, N'A0010', CAST(0x00009FCD00000000 AS DateTime), 11, 15, 13, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (16, N'A0012', CAST(0x00009FCE00000000 AS DateTime), 13, 15, 14, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (16, N'A0014', CAST(0x00009FCE00000000 AS DateTime), 15, 17, 16, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (16, N'A0016', CAST(0x00009FCE00000000 AS DateTime), 17, 19, 18, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (16, N'A0018', CAST(0x00009FCE00000000 AS DateTime), 13, 11, 12, 0, NULL)
INSERT [dbo].[Matricula] ([IdCursoProg], [IdAlumno], [FecMatricula], [ExaParcial], [ExaFinal], [Promedio], [Subsanacion], [ExaSub]) VALUES (16, N'A0020', CAST(0x00009FCE00000000 AS DateTime), 12, 16, 14, 0, NULL)
/****** Object:  Default [DF__CursoProg__Vacan__09DE7BCC]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[CursoProgramado] ADD  DEFAULT ((20)) FOR [Vacantes]
GO
/****** Object:  Default [DF__CursoProg__Activ__0AD2A005]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[CursoProgramado] ADD  DEFAULT ((1)) FOR [Activo]
GO
/****** Object:  Default [DF__CursoProg__Matri__0BC6C43E]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[CursoProgramado] ADD  DEFAULT ((0)) FOR [Matriculados]
GO
/****** Object:  Default [DF__Matricula__FecMa__145C0A3F]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[Matricula] ADD  DEFAULT (getdate()) FOR [FecMatricula]
GO
/****** Object:  Default [DF__Matricula__Subsa__15502E78]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[Matricula] ADD  DEFAULT ((0)) FOR [Subsanacion]
GO
/****** Object:  ForeignKey [FK__Curso__IdTarifa__24927208]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[Curso]  WITH CHECK ADD FOREIGN KEY([IdTarifa])
REFERENCES [dbo].[Tarifa] ([IdTarifa])
GO
/****** Object:  ForeignKey [FK__CursoProg__IdCic__25869641]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[CursoProgramado]  WITH CHECK ADD FOREIGN KEY([IdCiclo])
REFERENCES [dbo].[Ciclo] ([IdCiclo])
GO
/****** Object:  ForeignKey [FK__CursoProg__IdCur__267ABA7A]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[CursoProgramado]  WITH CHECK ADD FOREIGN KEY([IdCurso])
REFERENCES [dbo].[Curso] ([IdCurso])
GO
/****** Object:  ForeignKey [FK__CursoProg__IdPro__276EDEB3]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[CursoProgramado]  WITH CHECK ADD FOREIGN KEY([IdProfesor])
REFERENCES [dbo].[Profesor] ([IdProfesor])
GO
/****** Object:  ForeignKey [FK__Matricula__IdAlu__29572725]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[Matricula]  WITH CHECK ADD FOREIGN KEY([IdAlumno])
REFERENCES [dbo].[Alumno] ([IdAlumno])
GO
/****** Object:  ForeignKey [FK__Matricula__IdCur__286302EC]    Script Date: 03/26/2020 17:14:12 ******/
ALTER TABLE [dbo].[Matricula]  WITH CHECK ADD FOREIGN KEY([IdCursoProg])
REFERENCES [dbo].[CursoProgramado] ([IdCursoProg])
GO
