
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
-----------------------------ESTO SOLO A�ADE LA DATA QUE NO ES PROSEVA------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
------TENER MUCHO CUIDADO AL EJECUTAR ESTOS C�DIGO, SOLO SE PUEDE HACER UA VEZ

---creando una nueva base de datos para mantener el orden, orden, orden, orden, orden, orden, orden, orden, orden, orden, orden
--select *
--into reportes_diana..DIANA_REPORTE
--from ANEXOS_RIESGOS..DIANA_COPIA2


INSERT INTO reportes_diana..DIANA_REPORTE (
[FECHA_DESEMBOLSO],----check
[FUNCIONARIO],----check
[EMPRESA],
[CONDICION],
[MESES],
[A�O],
[NOMBRE_SOCIO],
[DNI],
[MONTO_DESEMBOLSADO],
[META_CUENTAS], ----tendr� nulos
[META_MONTO], ------tendr� nulos
[OFICINA],
[FECHA_REVISION], --tambi�n tendr� nulos
[ANALISTA], --------ese tambi�n
[EMPRESA2],
[PLANILLA],
[N_funcionario]
)
SELECT 
a.[F#DESEMBOLSO]-----correcto
,a.[FUNCIONARIO] -------correcto
,a.[EMPRESA] ------creo que si
,a.[CONDICI�N]------------correcto
,datename(month,a.[F#DESEMBOLSO])
,year(a.[F#DESEMBOLSO])
,A.[NOMBRE DEL SOCIO] --AQUI VA EL NOMBRE DEL SOCIO
,A.[DNI]
,A.[MONTO TOTAL PRESTAMO]
,NULL
,NULL
,A.OFICINA --OFICINA
,A.[FECHA DE REVISI�N]
,A.ANALISTA
,a.[EMPRESA]
,A.[EMPRESA] -------todo check hasta planilla
,0

from reportes_diana..DIANA_DICIEMBRE22 as A
where [ESTADO FINAL] = 'APROBADO'


SELECT * FROM reportes_diana..DIANA_REPORTE ORDER BY FECHA_DESEMBOLSO

----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
-----------------------------ESTO S� A�ADE LA DATA DE LAS PROSEVAS----------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------



INSERT INTO reportes_diana..DIANA_REPORTE (
[FECHA_DESEMBOLSO],----check
[FUNCIONARIO],----check
[EMPRESA],
[CONDICION],
[MESES],
[A�O],
[NOMBRE_SOCIO],
[DNI],
[MONTO_DESEMBOLSADO],
[META_CUENTAS], ----tendr� nulos
[META_MONTO], ------tendr� nulos
[OFICINA],
[FECHA_REVISION], 
[ANALISTA], 
[EMPRESA2],
[PLANILLA],
[N_funcionario]
)
SELECT 
a.[FECHA DE DESEMBOLSO]-----correcto
,a.[SEDE] -------correcto
,a.[EMPRESA] ------creo que si
,a.[CONDICI�N]------------correcto
,datename(month,a.[FECHA DE DESEMBOLSO])
,year(a.[FECHA DE DESEMBOLSO])
,A.[NOMBRE DEL SOCIO] --AQUI VA EL NOMBRE DEL SOCIO
,A.[DNI]
,A.[MONTO TOTAL PRESTAMO]
,NULL
,NULL
,CASE
	WHEN SEDE LIKE '%PROSEVA%' THEN 'SALA PROSEVA'
	WHEN SEDE LIKE 'CA�ETE' THEN 'OFICINA INFORMATIVA'
	ELSE 'OTROS' END--OFICINA
,A.[FECHA DE ENV�O EXPEDIENTE COMPLETO]
,A.ANALISTA
,a.[EMPRESA]
,A.[EMPRESA] -------todo check hasta planilla
,0

from reportes_diana..prosevas_diana_dic22 as A
where [estado final] = 'APROBADO'
--------------------------------------------------------------------


select * from reportes_diana..prosevas_diana_dic22
where [estado final] = 'APROBADO'