DECLARE @FECHA AS DATETIME
SET @FECHA = '20221231'


--codigo para saber si el número de fincore y el nuro de credito18 estén bien 
select nro_fincore,NumerodeCredito18, MontodeDesembolso22,* from [experimentos].[dbo].[copiapruebajuanjose] 
where NumerodeCredito18 <> nro_fincore 
and fechacorte1 = @FECHA
and len(NumerodeCredito18 ) > 6
order by ApellidosyNombresRazonSocial2

--aqui se podrá ver quienes son los socios que presentan estos errores
select distinct ApellidosyNombresRazonSocial2 from [experimentos].[dbo].[copiapruebajuanjose] 
where NumerodeCredito18 <> nro_fincore 
and fechacorte1 = @FECHA
and len(NumerodeCredito18 ) > 6
order by ApellidosyNombresRazonSocial2



SELECT  * FROM experimentos..copiapruebajuanjose
