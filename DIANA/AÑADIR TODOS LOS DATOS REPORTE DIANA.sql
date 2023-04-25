
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
-----------------------------ESTO SOLO AÑADE LA DATA QUE NO ES PROSEVA------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
------TENER MUCHO CUIDADO AL EJECUTAR ESTOS CÓDIGO, SOLO SE PUEDE HACER UA VEZ

---creando una nueva base de datos para mantener el orden, orden, orden, orden, orden, orden, orden, orden, orden, orden, orden
--select *
--into reportes_diana..DIANA_REPORTE
--from ANEXOS_RIESGOS..DIANA_COPIA2

/* -- CODIGO PARA AÑADIR COLUMNAS SI ES QUE HACE FALTA
ALTER TABLE reportes_diana..DIANA_REPORTE
ADD [FECHA_CORTE] DATETIME NULL
*/

----CÓDIGO PARA ASIGNAR FECHA A ESAS COLUMNAS,
--- SE TIENE QUE ARREGLAR LOS DATOS PORQUE DIANA ES COJUDA
update reportes_diana..diana_MARZO23
set [FECHA REVISION] = [FECHA DESEMBOLSO]
WHERE [FECHA REVISION] IS NULL
AND [FECHA DESEMBOLSO] IS NOT NULL

update reportes_diana..diana_MARZO23
set [FECHA DESEMBOLSO] = [FECHA REVISION]
WHERE [FECHA DESEMBOLSO] IS NULL
AND [FECHA REVISION] IS NOT NULL



SELECT * FROM reportes_diana..diana_MARZO23

--CON ESTO REVISAS LAS FECHAS
SELECT * FROM reportes_diana..diana_MARZO23
WHERE ([FECHA REVISION] IS NULL
OR [FECHA DESEMBOLSO] IS NULL
OR [FECHA DESEMBOLSO] IS NULL)

-----------------------------------------------------------
--------PROCEDEMOS A INSERTAR TODOS MENOS PROSEVA----------
-----------------------------------------------------------
DECLARE @FECHACORTE AS DATETIME
SET @FECHACORTE = '20230331'-------------------------------------------------------NO OLVIDAR PONER LA FECHA DEL MES


INSERT INTO reportes_diana..DIANA_REPORTE (
[FECHA_DESEMBOLSO],----check
[FUNCIONARIO],----check
[EMPRESA],
[CONDICION],
[MESES],
[AÑO],
[NOMBRE_SOCIO],
[DNI],
[MONTO_DESEMBOLSADO],
[META_CUENTAS], ----tendrá nulos
[META_MONTO], ------tendrá nulos
[OFICINA], --ACTUALMENTE NULL
[FECHA_REVISION], --también tendrá nulos
[ANALISTA], --------ese también
[EMPRESA2],
[PLANILLA],
[N_funcionario],
[ESTADO FINAL],
[CANAL OFICINA],
[PRODUCTO],
FECHA_CORTE
)
SELECT 
a.[FECHA DESEMBOLSO]-----correcto
,a.[FUNCIONARIO/SEDE] -------correcto
,a.[EMPRESA] ------creo que si
,a.[CONDICION]------------correcto
,datename(month,a.[FECHA DESEMBOLSO])
,year(a.[FECHA DESEMBOLSO])
,A.[SOCIO] --AQUI VA EL NOMBRE DEL SOCIO
,A.[DOC (DNI/CE/RUC)]
,A.[MONTO  PRESTAMO]
,NULL --META CUENTAS
,NULL --META MONTO
,A.[CANAL OFICINA] -- ANTERIORMENTE A.OFICINA
,A.[FECHA REVISION]
,A.ANALISTA
,A.[EMPRESA]
,A.[EMPRESA] -------todo check hasta planilla
,0
,A.[ESTADO FINAL]
,A.[CANAL OFICINA]
,A.[PRODUCTO]
,@FECHACORTE


from reportes_diana..DIANA_MARZO23 as A
--where [ESTADO FINAL] = 'APROBADO'

----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
-----------------------------ESTO SÍ AÑADE LA DATA DE LAS PROSEVAS----------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------

DECLARE @FECHACORTE AS DATETIME
SET @FECHACORTE = '20230331'-------------------------------------------------------NO OLVIDAR PONER LA FECHA DEL MES

INSERT INTO reportes_diana..DIANA_REPORTE (
[FECHA_DESEMBOLSO],----check
[FUNCIONARIO],----check
[EMPRESA],
[CONDICION],
[MESES],
[AÑO],
[NOMBRE_SOCIO],
[DNI],
[MONTO_DESEMBOLSADO],
[META_CUENTAS], ----tendrá nulos
[META_MONTO], ------tendrá nulos
[OFICINA],
[FECHA_REVISION], 
[ANALISTA], 
[EMPRESA2],
[PLANILLA],
[N_funcionario],
[ESTADO FINAL],
[CANAL OFICINA],
[PRODUCTO],
FECHA_CORTE
)
SELECT 
a.[FECHA DESEMBOLSO]-----correcto
,a.[FUNCIONARIO/SEDE] -------correcto
,a.[EMPRESA] ------creo que si
,a.[CONDICION]------------correcto
,datename(month,a.[FECHA DESEMBOLSO])
,year(a.[FECHA DESEMBOLSO])
,A.[SOCIO] --AQUI VA EL NOMBRE DEL SOCIO
,A.[DOC (DNI/CE/RUC)]
,A.[MONTO PRESTAMO]
,NULL
,NULL
,CASE
	WHEN [FUNCIONARIO/SEDE] LIKE '%PROSEVA%' THEN 'SALA PROSEVA'
	WHEN [FUNCIONARIO/SEDE] LIKE '%CAÑETE%' THEN 'OFICINA INFORMATIVA'
	ELSE 'OTROS' END--OFICINA
,A.[FECHA REVISION]
,A.ANALISTA
,a.[EMPRESA]
,A.[EMPRESA] -------todo check hasta planilla
,0
,A.[ESTADO FINAL]
,A.[CANAL OFICINA]
,A.[PRODUCTO]
,@FECHACORTE

from reportes_diana..prosevas_diana_MAR23 as A
--where [estado final] = 'APROBADO'
--and sede like '%piura%'

--------------------------------------------------------------------

