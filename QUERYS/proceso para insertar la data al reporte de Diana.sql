
select * from ANEXOS_RIESGOS..DIANA_COPIA order by FECHA_DESEMBOLSO
delete from ANEXOS_RIESGOS..DIANA_COPIA
where FECHA_DESEMBOLSO between '20220501' and '20220531'
 select * from ANEXOS_RIESGOS..DIANA_COPIA
where FECHA_DESEMBOLSO between '20220501' and '20220531'


select * from ANEXOS_RIESGOS..DIANA_COPIA
where FECHA_DESEMBOLSO between '20220801' and '20220831'
and FUNCIONARIO like '%jerson%'
and (NOMBRE_SOCIO like '%gozzer%'
	or NOMBRE_SOCIO like '%castillo%'
	or NOMBRE_SOCIO like '%anicama%')

update ANEXOS_RIESGOS..DIANA_COPIA
set funcionario = 'MARGARITA CHINGA'

---        select * from ANEXOS_RIESGOS..DIANA_COPIA
where FECHA_DESEMBOLSO = '20220801'
and empresa = 'LIBRE DISPONIBILIDAD'
and NOMBRE_SOCIO = 'GOZZER DAVALOS CHELVY KENIA'
and MONTO_DESEMBOLSADO = 3000
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--SELECT  * FROM Anexos_Riesgos..DIANA_COPIA ORDER BY FECHA_DESEMBOLSO
--delete from ANEXOS_RIESGOS..DIANA_COPIA where FechaCorte1='20220930'

-------------------------------SUPER IMPORTANTE CÓDIGO PARA AÑADIR LA FECHA DE CORTE Y HAGA MATCH
-------------------------------PARA QUE EL CÓDIGO FUNCIONES, NECESITAS EL ANEXO06 DE ESTE MES
ALTER TABLE Anexos_Riesgos..DIANA_OCTUBRE22
ADD FechaCorte1 DATETIME NULL

UPDATE A
SET FechaCorte1 = '20221031' 
FROM Anexos_Riesgos..DIANA_OCTUBRE22 AS A


INSERT INTO ANEXOS_RIESGOS..DIANA_COPIA (
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
[OFICINA], ---------tendrá nulos
[FECHA_REVISION], --también tendrá nulos
[ANALISTA], --------ese también
[EMPRESA2],
[PLANILLA],
[N_funcionario]
)
SELECT 
a.[FechadeDesembolso21]-----correcto
,a.[PROMOTOR] -------correcto
,a.[EMPRESA] ------creo que si
,a.[tipo_afil]------------correcto
,datename(month,a.FechadeDesembolso21)
,year(a.FechadeDesembolso21)
,C.[Socio]
,C.[N_DNI]
,C.[MONT]
,NULL
,NULL
,Null
,Null
,null
,a.[EMPRESA]
,C.[Planilla] -------todo check hasta planilla
,0

from Anexos_Riesgos..DIANA_MAYO22 as C LEFT JOIN [experimentos].[dbo].[copiapruebajuanjose] as a
   on (C.[FINCORE]=A.NumerodeCredito18 and c.FechaCorte1=a.FechaCorte1)


SELECT * FROM Anexos_Riesgos..DIANA_MAYO22 WHERE Funcionario LIKE '%MARGARIT%'
SELECT * FROM Anexos_Riesgos..DIANA_COPIA WHERE FUNCIONARIO LIKE '%MARGARIT%' AND FECHA_DESEMBOLSO BETWEEN '20220501' AND '20220531'


------------------para probar si ha funcionado
--select * from ANEXOS_RIESGOS..DIANA_COPIA
--order by FECHA_DESEMBOLSO
select * from [experimentos].[dbo].[copiapruebajuanjose]
----------------------------------------------------------------------
DELETE FROM ANEXOS_RIESGOS..DIANA_COPIA
WHERE FECHA_DESEMBOLSO IS NULL
-----------------------------------------------------------------
SELECT * FROM ANEXOS_RIESGOS..DIANA_COPIA ORDER BY FECHA_DESEMBOLSO

SELECT COUNT(DISTINCT FECHA_DESEMBOLSO) FROM ANEXOS_RIESGOS..DIANA_COPIA 
WHERE FECHA_DESEMBOLSO > '20220501'
AND OFICINA IS NULL
ORDER BY FECHA_DESEMBOLSO


-------------SUPER QUERY PARA UPDATEAR LA COLUMNA OFICINA (NECESARIA PARA PODER INSERTAR DATOS EN LOS REPORTES DE COLOCACIONES)
--UPDATE ANEXOS_RIESGOS..DIANA_COPIA
--SET OFICINA =  
--	CASE
--		WHEN	FUNCIONARIO LIKE '%ALICIA OV%' OR FUNCIONARIO LIKE '%ANDREA BIL%' 
--				OR FUNCIONARIO LIKE '%GIOVANNA H%' OR FUNCIONARIO LIKE '%MARGIORY EL%' 
--				THEN 'SUPERV.1'
--		WHEN	FUNCIONARIO LIKE '%GUSTAVO P%' OR FUNCIONARIO LIKE '%JULY%'	
--				OR FUNCIONARIO LIKE '%DAVID B%' OR FUNCIONARIO LIKE '%KATHERIN R%' 
--				THEN 'SUPERV.2'
--		WHEN	FUNCIONARIO LIKE '%JAQUELINE CHUQUI%' OR FUNCIONARIO LIKE '%LUDHIANA C%' 
--				OR FUNCIONARIO LIKE '%ROSA M%' OR FUNCIONARIO LIKE '%ROXANA Q%' 
--				OR FUNCIONARIO LIKE '%YOBANA LAU%' 
--				THEN 'SUPERV.3'
--		WHEN	FUNCIONARIO LIKE '%PROSEVA%' 
--				THEN FUNCIONARIO
--		WHEN	FUNCIONARIO LIKE '%CAÑETE%' 
--				THEN FUNCIONARIO
--		WHEN	EMPRESA LIKE '%ÑIA MECANICA Y CON%' OR EMPRESA LIKE '%TIVA DE AHORRO Y CREDITO ATLANT%' 
--				OR  EMPRESA LIKE '%IGM CONTRATISTAS GENERALE%' OR EMPRESA LIKE '%JPGB SERVICIOS%' 
--				OR EMPRESA LIKE '%PROMOCION DE SERVICIOS VARIOS%' OR EMPRESA LIKE '%RECUPERACIONES FINANCIERAS S%'
--				OR EMPRESA LIKE '%SERVICIOS DE RECUPERACIONES Y COBRANZAS S%'
--				OR EMPRESA LIKE '%PROGENERE%' 
--				THEN 'ADMINISTRATIVO'
--		WHEN	EMPRESA LIKE '%LIBRE D%' 
--				then 'LD'
--		WHEN	FUNCIONARIO LIKE '%JONATHAN ESTRADA%' OR FUNCIONARIO LIKE '%ANTHONY OSO%'
--				OR FUNCIONARIO LIKE '%ANTHONNY OSO%' OR FUNCIONARIO LIKE '%ANTONY OSO%'
--				OR FUNCIONARIO LIKE '%KELLY HUAM%' OR FUNCIONARIO LIKE '%JIMN MEN%' 
--				OR FUNCIONARIO LIKE '%FIGARI VEGA%' OR FUNCIONARIO LIKE '%CESAR M%'
--				OR FUNCIONARIO LIKE '%JORGE AR%' OR FUNCIONARIO LIKE '%JOSE SAN%' OR FUNCIONARIO LIKE '%JOSÉ SAN%'
--				OR FUNCIONARIO LIKE '%LUIS BUSTA%' OR FUNCIONARIO LIKE '%VICTOR FARF%'
--				OR FUNCIONARIO LIKE '%ALEJANDRO HUA%' OR FUNCIONARIO LIKE '%DAYANA CH%'
--				OR FUNCIONARIO LIKE '%MILTON JU%' OR FUNCIONARIO LIKE '%YESENIA PO%'
--				OR FUNCIONARIO LIKE '%ALEXANDER GAR%' OR FUNCIONARIO LIKE '%DENNIS T%'
--				OR FUNCIONARIO LIKE '%FRANK L%' OR FUNCIONARIO LIKE '%JEAN B%'
--				OR FUNCIONARIO LIKE '%JESSICA SOLORZA%' OR FUNCIONARIO LIKE '%JONATHAN SEGAMA%'		
--				OR FUNCIONARIO LIKE '%MARVIL RISCO%' OR FUNCIONARIO LIKE '%PAMELA GARCIA%'		
--				OR FUNCIONARIO LIKE '%WILLIAMS TRAUCO%' OR FUNCIONARIO LIKE '%SALVADOR TORRES%'
--				OR EMPRESA LIKE '%MICROEMPRESA%'		
--				THEN 'MICROEMPRESA' END
--WHERE OFICINA IS NULL

--AND FECHA_DESEMBOLSO >= '20220501'



---------------------------------------------
SELECT *, OFICINA FROM ANEXOS_RIESGOS..DIANA_COPIA
WHERE OFICINA IS NULL
ORDER BY FECHA_DESEMBOLSO
---------------------------------------------







select * from  ANEXOS_RIESGOS..DIANA_COPIA where FECHA_DESEMBOLSO >= '20220701' order by FECHA_DESEMBOLSO, NOMBRE_SOCIO

update ANEXOS_RIESGOS..DIANA_COPIA
set funcionario = 'ROXANA QUISPE'
WHERE FUNCIONARIO LIKE 'ROXANA QUISPE CHAVEZ'

SELECT DISTINCT FUNCIONARIO FROM ANEXOS_RIESGOS..DIANA_COPIA
ORDER BY FUNCIONARIO