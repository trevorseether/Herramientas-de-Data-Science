DECLARE @FechaCorte datetime
SET @FechaCorte = '20221231'


-------------------------------------------------------
SELECT FechaCorte1, Nro_Fincore, MontodeDesembolso22, TipodeProducto43,'MICROEMPRESA?' as 'CODIGO DE',
case when MontodeDesembolso22 > 20000 and MontodeDesembolso22 <= 300000 then 'PEQUEÑA EMPRESA(15 AL 19)'
		ELSE 'MEDIANA EMPRESA (95 AL 99)' 
		END AS 'TIPO CORRECTO'
FROM experimentos..copiapruebajuanjose
WHERE FechaCorte1 = @FECHACORTE
and TipodeProducto43 in (21,22,23,24,25,29)
and MontodeDesembolso22 > 20000
order by MontodeDesembolso22
---------------------------------------------------------
SELECT FechaCorte1, Nro_Fincore, MontodeDesembolso22, TipodeProducto43,'PEQUEÑA EMPRESA?' as 'CODIGO DE',
CASE WHEN MontodeDesembolso22 <= 20000 THEN 'MICROEMPRESA (21 AL 29)'
	ELSE 'MEDIANA EMPRESA (95 AL 99)' END AS 'TIPO CORRECTO'
FROM experimentos..copiapruebajuanjose
WHERE FechaCorte1 = @FECHACORTE
and TipodeProducto43 in (15,16,17,18,19)
and MontodeDesembolso22 < 20001
AND MontodeDesembolso22 > 0
---------------------------------------------------------
SELECT FechaCorte1, Nro_Fincore, MontodeDesembolso22, TipodeProducto43,'PEQUEÑA EMPRESA?' as 'CODIGO DE'
FROM experimentos..copiapruebajuanjose
WHERE FechaCorte1 = @FECHACORTE
and TipodeProducto43 in (15,16,17,18,19)
and MontodeDesembolso22 > 300000

SELECT FechaCorte1, Nro_Fincore, MontodeDesembolso22, TipodeProducto43,'MEDIANA EMPRESA?' as 'CODIGO DE'
FROM experimentos..copiapruebajuanjose
WHERE FechaCorte1 = @FECHACORTE
and TipodeProducto43 in (95,96,97,98,99)
and MontodeDesembolso22 < 300001




