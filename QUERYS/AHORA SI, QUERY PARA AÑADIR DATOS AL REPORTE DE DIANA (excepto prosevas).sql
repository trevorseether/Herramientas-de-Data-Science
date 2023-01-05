
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
-----------------------------ESTO SOLO AÑADE LA DATA QUE NO ES PROSEVA------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
------TENER MUCHO CUIDADO AL EJECUTAR ESTOS CÓDIGO, SOLO SE PUEDE HACER UA VEZ

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
[AÑO],
[NOMBRE_SOCIO],
[DNI],
[MONTO_DESEMBOLSADO],
[META_CUENTAS], ----tendrá nulos
[META_MONTO], ------tendrá nulos
[OFICINA],
[FECHA_REVISION], --también tendrá nulos
[ANALISTA], --------ese también
[EMPRESA2],
[PLANILLA],
[N_funcionario]
)
SELECT 
a.[F#DESEMBOLSO]-----correcto
,a.[FUNCIONARIO] -------correcto
,a.[EMPRESA] ------creo que si
,a.[CONDICIÓN]------------correcto
,datename(month,a.[F#DESEMBOLSO])
,year(a.[F#DESEMBOLSO])
,A.[NOMBRE DEL SOCIO] --AQUI VA EL NOMBRE DEL SOCIO
,A.[DNI]
,A.[MONTO TOTAL PRESTAMO]
,NULL
,NULL
,A.OFICINA --OFICINA
,A.[FECHA DE REVISIÓN]
,A.ANALISTA
,a.[EMPRESA]
,A.[EMPRESA] -------todo check hasta planilla
,0

from reportes_diana..DIANA_DICIEMBRE22 as A
where [ESTADO FINAL] = 'APROBADO'


SELECT * FROM reportes_diana..DIANA_REPORTE ORDER BY FECHA_DESEMBOLSO

----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
-----------------------------ESTO SÍ AÑADE LA DATA DE LAS PROSEVAS----------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------



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
[N_funcionario]
)
SELECT 
a.[FECHA DE DESEMBOLSO]-----correcto
,a.[SEDE] -------correcto
,a.[EMPRESA] ------creo que si
,a.[CONDICIÓN]------------correcto
,datename(month,a.[FECHA DE DESEMBOLSO])
,year(a.[FECHA DE DESEMBOLSO])
,A.[NOMBRE DEL SOCIO] --AQUI VA EL NOMBRE DEL SOCIO
,A.[DNI]
,A.[MONTO TOTAL PRESTAMO]
,NULL
,NULL
,CASE
	WHEN SEDE LIKE '%PROSEVA%' THEN 'SALA PROSEVA'
	WHEN SEDE LIKE 'CAÑETE' THEN 'OFICINA INFORMATIVA'
	ELSE 'OTROS' END--OFICINA
,A.[FECHA DE ENVÍO EXPEDIENTE COMPLETO]
,A.ANALISTA
,a.[EMPRESA]
,A.[EMPRESA] -------todo check hasta planilla
,0

from reportes_diana..prosevas_diana_dic22 as A
where [estado final] = 'APROBADO'
--------------------------------------------------------------------


select * from reportes_diana..prosevas_diana_dic22
where [estado final] = 'APROBADO'