select * from Anexos_Riesgos..anx06_20221031 ORDER BY [Apellidos y Nombres / Razón Social 2/]
select * from cabecera where FechaCorte1 = '20221031' ORDER BY ApellidosyNombresRazonSocial2



-------------------------------------todo esto para la tabla cabecera
-----------------------------------------------------------------REPROGRAMADOS PARA LA CABECERA----------------------------------------
select Reprogramados52,* from cabecera
select * from Anexos_Riesgos..anx06_20220831
[Saldo Capital de Créditos Reprogramados 52/]

--ALTER TABLE Cabecera
--DROP COLUMN Reprogramados52

--ALTER TABLE Cabecera
--add Reprogramados52 float

update a
set a.Reprogramados52 = b.[Saldo Capital de Créditos Reprogramados 52/]

from cabecera a
join Anx06_20220131 AS b on (a.[NumerodeCredito18] = b.[Numero de Crédito 18/] and a.FechaCorte1 = '20220131')
WHERE A.FechaCorte1 = '20220131'
  

SELECT SUM([Saldo Capital de Créditos Reprogramados 52/]) AS 'SUMA REPROGRAMADOS' FROM Anx06_20220131
SELECT SUM(Reprogramados52) as 'SUMA REPROGRAMADOS' FROM Cabecera where FechaCorte1 = '20220131'
--------------------------------------------------------------REPROGRAMADOS DE EL ANEXO 06-00000000-------------------------------------
--ALTER TABLE experimentos..copiapruebajuanjose
--DROP COLUMN Reprogramados52

--ALTER TABLE experimentos..copiapruebajuanjose
--add Reprogramados52 float
DECLARE @FECHA VARCHAR(100)
SET @FECHA = '20220131'

update a
set a.Reprogramados52 = b.[Saldo Capital de Créditos Reprogramados 52/]

from experimentos..copiapruebajuanjose a
join Anx06_20220131 AS b on (a.[Nro_Fincore] = b.[Nro Prestamo _Fincore] and a.FechaCorte1 = @FECHA) ---AQUI HAY OTRO PARA CAMBIAR
WHERE A.FechaCorte1 = @FECHA

SELECT SUM([Saldo Capital de Créditos Reprogramados 52/]) AS 'SUMA REPROGRAMADOS' FROM Anx06_20220131 -------AQUI HAY UNO PARA CAMBIAR
SELECT SUM(Reprogramados52) as 'SUMA REPROGRAMADOS' FROM experimentos..copiapruebajuanjose where FechaCorte1 = @FECHA

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------AHORA LA COLUMNA DE REFINANCIADO TXT-----------------------------------------------------------------
------- PARA LA CABECERA
SELECT REFINANCIADO AS 'ETIQUETA ANX06' , COUNT(Refinanciado) AS 'CONTEO' FROM experimentos..copiapruebajuanjose WHERE FechaCorte1 = '20221031' GROUP BY REFINANCIADO
SELECT REFINANCIADO AS 'ETIQUETA CABECERA' , COUNT(Refinanciado) AS 'CONTEO' FROM CABECERA WHERE FechaCorte1 = '20221031' GROUP BY REFINANCIADO
SELECT [Refinanciado TXT] AS 'ETIQUETA', COUNT([Refinanciado TXT]) AS 'CONTEO' FROM ANX06_20221031 GROUP BY [Refinanciado TXT]

--SELECT *, [Refinanciado TXT], [Capital Refinanciado 28/], [Saldo de colocaciones (créditos directos) 24/] FROM ANX06_20220930
--SELECT SUM([Capital Refinanciado 28/]) FROM ANX06_20220930
--SELECT SUM([Saldo de colocaciones (créditos directos) 24/]) FROM ANX06_20220930 WHERE [Refinanciado TXT] = 'REFINANCIADO'

--SELECT DISTINCT CapitalRefinanciado28 FROM experimentos..copiapruebajuanjose

DECLARE @FECHA VARCHAR(100)
SET @FECHA = '20220131'

update a
set a.Refinanciado = b.[Refinanciado TXT]

from Cabecera a
join anx06_20220131 b on (a.NumerodeCredito18 = b.[Numero de Crédito 18/] and a.FechaCorte1 = @FECHA) ---FECHA PARA CAMBIAR
WHERE A.FechaCorte1 = @FECHA



--SELECT REFINANCIADO AS 'ETIQUETA ANX06' , COUNT(Refinanciado) AS 'CONTEO' FROM experimentos..copiapruebajuanjose WHERE FechaCorte1 = @FECHA GROUP BY REFINANCIADO
SELECT REFINANCIADO AS 'ETIQUETA CABECERA' , COUNT(Refinanciado) AS 'CONTEO' FROM CABECERA WHERE FechaCorte1 = @FECHA GROUP BY REFINANCIADO
SELECT [Refinanciado TXT] AS 'ETIQUETA', COUNT([Refinanciado TXT]) AS 'CONTEO' FROM ANX06_20220131 GROUP BY [Refinanciado TXT] ----AQUI HAY FECHA PARA CAMBIAR

----------------------------------------------------------------------------------------------------
--------------------------------------------PARA EL ANEXO06-----------------------------------------
----------------------------------------------------------------------------------------------------
DECLARE @FECHA VARCHAR(100)
SET @FECHA = '20220131'

update a
set a.Refinanciado = b.[Refinanciado TXT]

from experimentos..copiapruebajuanjose a
join anx06_20220131 b on (a.NumerodeCredito18 = b.[Numero de Crédito 18/] and a.FechaCorte1 = @FECHA) ---FECHA PARA CAMBIAR
WHERE A.FechaCorte1 = @FECHA


SELECT REFINANCIADO AS 'ETIQUETA ANX06' , COUNT(Refinanciado) AS 'CONTEO' FROM experimentos..copiapruebajuanjose WHERE FechaCorte1 = @FECHA GROUP BY REFINANCIADO
--SELECT REFINANCIADO AS 'ETIQUETA de cabecera' , COUNT(Refinanciado) AS 'CONTEO' FROM Cabecera WHERE FechaCorte1 = @FECHA GROUP BY REFINANCIADO
SELECT [Refinanciado TXT] AS 'ETIQUETA', COUNT([Refinanciado TXT]) AS 'CONTEO' FROM ANX06_20220131 GROUP BY [Refinanciado TXT] ----AQUI HAY FECHA PARA CAMBIAR







UPDATE A SET
A.NUEVO_PROMOTOR=B.NUEVO_PROMOTOR,
--A.TipodeProducto43=B.TipodeProducto43,
--A.TipodeCredito19=B.TipodeCredito19,
a.NUEVA_PLANILLA=B.NUEVA_PLANILLA,
A.ADMINISTRADOR=B.ADMINISTRADOR
--SELECT A.NumerodeCredito18,A.Monedadelcredito17,A.PROMOTOR,A.NUEVO_PROMOTOR,B.NUEVO_PROMOTOR,a.TipodeProducto43,b.TipodeProducto43 
FROM experimentos..copiapruebajuanjose A 
JOIN #BASE1 B ON (A.Nro_Fincore=B.Nro_Fincore AND A.NumerodeCredito18=B.NumerodeCredito18 AND A.Monedadelcredito17=B.Mone)
WHERE A.FechaCorte1='20221031'
