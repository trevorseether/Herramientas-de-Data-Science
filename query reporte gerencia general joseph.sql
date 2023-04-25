use experimentos

go
--select * from Cabecera where FechaCorte1='20200630'

/********************************************************************************************************************/
/******************************************************vista total************************************************/
/********************************************************************************************************************/
--Declare @fecha datetime
--set @fecha='20200531'

--select * from Anexos_Riesgos..Cabecera where FechaCorte1='20200531'
--41
--39
--16
--45
--34
---GENERO
select a.Genero4,count(1) from (select CodigoSocio7,c.Genero4,count(1)nro from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c
WHERE 
c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0
group by CodigoSocio7,c.Genero4)a
group by a.Genero4
--O
--F
--M
--TIPO DE CREDITO
select 
case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end TxtTipoCredito
,sum(Saldodecolocacionescreditosdirectos24)Saldo,count(1) cantidad

from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
group by case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end

--09
--08
--10
--13
--12
-------
--saldo de cartera bruta clasificada()
--SALDO TOTAL
--92651183.7600
--REGISTROS - 9091

/*select SUM(C.Saldodecolocacionescreditosdirectos24)
from Cabecera c WHERE c.FechaCorte1='20201130' and c.Saldodecolocacionescreditosdirectos24>0
--SALDO_VIGENTE(INCLUYE CARTERA VENCIDA)
--78445950.2700
--8952
select SUM(C.Saldodecolocacionescreditosdirectos24)
from Cabecera c WHERE c.FechaCorte1='20201130' and c.Saldodecolocacionescreditosdirectos24>0
AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)*/
		/*
		--36178536.0500
		select SUM(C.Saldodecolocacionescreditosdirectos24)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210930' and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND ISNULL(C.CapitalRefinanciado28,0) = 0
		AND ISNULL(C.CapitalenCobranzaJudicial30,0) = 0
		AND C.DiasdeMora33=0*/
		
		select SUM(C.CapitalVigente26) as 'vigente'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		
		select SUM(C.CapitalRefinanciado28) as 'refinanciado'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		
		select SUM(C.CapitalVencido29) as 'vencido'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		
		select SUM(C.CapitalenCobranzaJudicial30) as 'judicial'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		
		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.CapitalVencido29)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
		--and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND C.DiasdeMora33>=0
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end 
		order by Tramos
		--select 
		--SUM(C.Saldodecolocacionescreditosdirectos24)
		--from Cabecera c WHERE c.FechaCorte1='20200630' and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		--AND C.DiasdeMora33<>0

		


-----------------------
--NUMERO DE TOTAL DE CREDITO
--9091
select COUNT(C.NumerodeCredito18) AS 'Número de créditos'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0
--233

----NUMERO DE CREDITOS DESEMBOLSADO DURANTE EL PERIODO QUITANDO LOS REFINANCIADOS
select COUNT(C.FechadeDesembolso21) as 'desembolsados durante el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%'
AND ISNULL(C.CapitalRefinanciado28,0) = 0

----------
--MONTO DESEMBOLSADO DE LOS CREDITO
--2350355.6500

select 
SUM(C.MontodeDesembolso22) as 'Monto de los Créditos dutante el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' AND 
C.FechaCorte1=EOMONTH(FechadeDesembolso21)  and 
c.Saldodecolocacionescreditosdirectos24>0
--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%'
AND ISNULL(C.CapitalRefinanciado28,0) = 0


---------
--SOCIOS
--
--SOCIOS NUEVOS
select 
--*
sum(case when (c.TIPO like '%NVO%' or c.tipo_afil like '%nvo%') then 1 else 0 end ) AS 'Nuevos durante el periodo'--,
--sum(case when c.TIPO_afil like '%NVO%' then 0 else 1 end )
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
--233

---socios totales 
select 
count(distinct c.NumerodeDocumento10) as 'SOCIOS'
--sum(case when c.TIPO_afil like '%NVO%' then 1 else 0 end )--,
--sum(case when c.TIPO_afil like '%NVO%' then 0 else 1 end )
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' --AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
--------------------------------

-----MONTO SOLES
select  sum(C.MontodeDesembolso22) as 'Prestamos en soles'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
c.Monedadelcredito17='01'
--AND (UPPER(isnull(C.TIPO_afil,'XX')) NOT LIKE '%REF%')
AND ISNULL(C.CapitalRefinanciado28,0) = 0


-----saldo en monto DOLARES
select sum(ISNULL(C.MontodeDesembolso22,0))
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
c.Monedadelcredito17='02'
--AND (UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%')
AND ISNULL(C.CapitalRefinanciado28,0) = 0


------------------------------------------------------------------
/*******************************************************************************************************************************/
/****************************************//****vista DXP******//***************************************************************************************/
/*********************************************************************************************************************************/
---GENERO

select a.Genero4,count(CodigoSocio7) from (select CodigoSocio7,c.Genero4,count(1)nro from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c
WHERE 
c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0  AND c.TipodeProducto43 IN (34,39,35,36)
group by CodigoSocio7,c.Genero4)a
group by a.Genero4
order by Genero4 desc

--O
--F
--M
--TIPO DE CREDITO
select 
case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end TxtTipoCredito
,sum(Saldodecolocacionescreditosdirectos24)Saldo,count(1) cantidad

from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (34,39,35,36)
group by case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end


--select c.TipodeCredito19,count(1) 
--from Cabecera c WHERE c.FechaCorte1='20200531' and c.Saldodecolocacionescreditosdirectos24>0
--group by TipodeCredito19
--09
--08
--10
--13
--12
-------
--saldo de cartera bruta clasificada()
--SALDO TOTAL
--92651183.7600
--REGISTROS - 9091
/*
select SUM(C.Saldodecolocacionescreditosdirectos24)
from Cabecera c WHERE c.FechaCorte1='20210331' and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (34,39)
--SALDO_VIGENTE(INCLUYE CARTERA VENCIDA)
--78445950.2700
--8952
select SUM(C.Saldodecolocacionescreditosdirectos24)
from Cabecera c WHERE c.FechaCorte1='20210331' and c.Saldodecolocacionescreditosdirectos24>0
--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
AND ISNULL(C.CapitalRefinanciado28,0) = 0
AND ISNULL(C.CapitalenCobranzaJudicial30,0) = 0
AND TipodeProducto43 IN (34,39)


*/
/*saldos vigente, refinanciado, judicial, vencido*/

select SUM(C.CapitalVigente26) as 'Capital Vigente'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (34,39,35,36)

		select SUM(C.CapitalRefinanciado28) as 'Capital Refinanciado'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (34,39,35,36)

		select SUM(C.CapitalVencido29) as 'Capital Vencido' 
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (34,39,35,36)

		select SUM(C.CapitalenCobranzaJudicial30) as 'Capital en Cobranza Judicial'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (34,39,35,36)
		---------------------------------------------------------
		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.CapitalVencido29)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
		--and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND C.DiasdeMora33>=0 AND TipodeProducto43 IN (34,39,35,36)
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end 
		order by Tramos
/*saldos vigente, refinanciado, judicial, vencido*/

/*
		/*--------VIGENTE-----------*/
		--36178536.0500
		select SUM(C.Saldodecolocacionescreditosdirectos24)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210531' and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND ISNULL(C.CapitalRefinanciado28,0) = 0
		AND ISNULL(C.CapitalenCobranzaJudicial30,0) = 0
		AND C.DiasdeMora33=0
		AND TipodeProducto43 IN (34,39,35)

		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.Saldodecolocacionescreditosdirectos24)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210531' and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND ISNULL(C.CapitalRefinanciado28,0) = 0
		AND ISNULL(C.CapitalenCobranzaJudicial30,0) = 0
		AND C.DiasdeMora33<>0
		AND TipodeProducto43 IN (34,39,35)
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end 


*/


-----------------------
--NUMERO TOTAL DE CREDITO----
--9091
select COUNT(C.NumerodeCredito18) as 'Número de Créditos'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' and
 c.Saldodecolocacionescreditosdirectos24>0 AND 
 TipodeProducto43 IN (34,39,35,36) --and UPPER(TIPO_afil) NOT like '%REF%'
--233

------NUMERO DE CREDITOS DESEMBOLSADOS-------
select COUNT(C.NumerodeCredito18) AS '# desembolsados durante el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (34,39,35,36)
--AND UPPER(isnull(TIPO_afil,'xx')) NOT like '%REF%'
AND ISNULL(C.CapitalRefinanciado28,0) = 0

----------
--MONTO DESEMBOLSADO DE LOS CREDITO
--2350355.6500
select SUM(C.MontodeDesembolso22) as 'monto durante el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (34,39,35,36) 
--and UPPER(isnull(TIPO_afil,'XX')) NOT like '%REF%'
AND ISNULL(C.CapitalRefinanciado28,0) = 0

--SALDO CASTIGADO
--1864854.9200
select SUM(ISNULL(C.SaldosdeCreditosCastigados38,0))
from anexos_riesgos..Cabecera c WHERE c.FechaCorte1='20221231' 
and c.Saldodecolocacionescreditosdirectos24=0
AND TipodeProducto43 IN (34,39,35,36)

---------
--SOCIOS
--
--SOCIOS NUEVOS
select 
sum(case when c.TIPO like '%NVO%' then 1 else 0 end ) as 'socios nuevos'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (34,39,35,36)

------NUMERO DE SOCIO TOTAL-------
select 
COUNT(DISTINCT NumerodeDocumento10) as 'total socios'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' 
--AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (34,39,35,36)


-----SALDO DE MONTO EN SOLES-------
select sum(ISNULL(C.MontodeDesembolso22,0))
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (34,39,35,36) AND 
c.Monedadelcredito17='01' 
--and UPPER(ISNULL(TIPO_afil,'xx')) NOT like '%REF%'
AND ISNULL(C.CapitalRefinanciado28,0) = 0

-----SALDO DE MONTO EN DOLARES-------
select sum(C.MontodeDesembolso22)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (34,39,35,36) and 
c.Monedadelcredito17='02' 
--AND (UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%')
AND ISNULL(C.CapitalRefinanciado28,0) = 0


---------------------------------*-------------------------------------------
-----------------------------------------------------------------------------
---------------------------HIPOTECARIO---------------------------------------

--SELECT * FROM Cabecera C WHERE C.FechaCorte1='20200531' AND TipodeProducto43=16
--41
--39--DXP
--16
--45
--34--DXP

---GENERO
select a.Genero4,count(1) from (select CodigoSocio7,c.Genero4,count(1)nro from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c
WHERE 
c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0  AND TipodeProducto43 IN (41,45)
group by CodigoSocio7,c.Genero4)a
group by a.Genero4
order by Genero4 desc --orden descendente
--O
--F
--M
--TIPO DE CREDITO
select 
case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end TxtTipoCredito
,sum(Saldodecolocacionescreditosdirectos24)Saldo,count(1) cantidad

from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (41,45)
group by case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end


--select c.TipodeCredito19,count(1) 
--from Cabecera c WHERE c.FechaCorte1='20200531' and c.Saldodecolocacionescreditosdirectos24>0
--group by TipodeCredito19
--09
--08
--10
--13
--12
-------
--saldo de cartera bruta clasificada()
--SALDO TOTAL
--92651183.7600
--REGISTROS - 9091
/*
select SUM(C.Saldodecolocacionescreditosdirectos24)
from Cabecera c WHERE c.FechaCorte1='20210228' and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (41,45)
--SALDO_VIGENTE(INCLUYE CARTERA VENCIDA)
--78445950.2700
--8952
select SUM(C.Saldodecolocacionescreditosdirectos24)
from Cabecera c WHERE c.FechaCorte1='20210228' and c.Saldodecolocacionescreditosdirectos24>0
AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
AND TipodeProducto43 IN (41,45)


*/
/*saldos vigente, refinanciado, judicial, vencido*/

		select SUM(C.CapitalVigente26) as 'Capital vigente'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (41,45)

		select SUM(C.CapitalRefinanciado28) as 'Capital Refinanciado'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (41,45)

		select SUM(C.CapitalVencido29) as 'Capital Vencido' 
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (41,45)

		select SUM(C.CapitalenCobranzaJudicial30) as 'Cobranza judicial'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (41,45)
		--------------------------------------------------
		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.CapitalVencido29)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
		--and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND C.DiasdeMora33>=0  AND TipodeProducto43 IN (41,45)
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end
		order by Tramos

/*saldos vigente, refinanciado, judicial, vencido*/

		--36178536.0500
		select SUM(C.Saldodecolocacionescreditosdirectos24) as 'Saldo de Colocaciones de creditos directos'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210531' and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		and isnull(c.CapitalRefinanciado28,0) = 0
		and isnull(CapitalenCobranzaJudicial30,0) = 0
		AND C.DiasdeMora33=0 AND TipodeProducto43 IN (41,45)

		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.Saldodecolocacionescreditosdirectos24)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210531' and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		and isnull(c.CapitalRefinanciado28,0) = 0
		and isnull(CapitalenCobranzaJudicial30,0) = 0
		AND C.DiasdeMora33<>0 AND TipodeProducto43 IN (41,45)
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end
		order by Tramos





-----------------------
--NUMERO DE CREDITO
--9091
select COUNT(C.TipodeProducto43) as 'N de créditos'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' and
 c.Saldodecolocacionescreditosdirectos24>0 AND 
 TipodeProducto43 IN (41,45)
--233

select COUNT(C.TipodeProducto43)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (41,45) 
--AND UPPER(TIPO_afil) NOT LIKE '%REF%'
and isnull(CapitalRefinanciado28,0) = 0

----------
--MONTO DESEMBOLSADO DE LOS CREDITO
--2350355.6500
select SUM(C.MontodeDesembolso22)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE 
c.FechaCorte1='20221231' AND 
C.FechaCorte1=EOMONTH(FechadeDesembolso21)  and 
c.Saldodecolocacionescreditosdirectos24>0 
--AND UPPER(isnull(TIPO_afil,'xx')) NOT LIKE '%REF%' 
and isnull(CapitalRefinanciado28,0) = 0
and TipodeProducto43 IN (45,41)


--SALDO CASTIGADO
--1864854.9200
select SUM(ISNULL(C.SaldosdeCreditosCastigados38,0))
from anexos_riesgos..Cabecera c WHERE c.FechaCorte1='20221231'   and c.Saldodecolocacionescreditosdirectos24=0
AND TipodeProducto43 IN (45,41)

---------
--SOCIOS
--
--SOCIOS NUEVOS
select 
sum(case when c.tipo like '%NVO%' then 1 else 0 end )
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' AND 
C.FechaCorte1=EOMONTH(FechadeDesembolso21)  and 
c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (45,41)

--348
------------ nro de socios activos
select 
COUNT(DISTINCT NumerodeDocumento10) as 'socios activos'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' 
--AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (41,45)


-----saldo en monto 
select sum(ISNULL(C.MontodeDesembolso22,0))
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20211031' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (41,45) AND 
c.Monedadelcredito17='01'


select *
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20211031' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (41,45) AND 
c.Monedadelcredito17='01'
----NOTA TODOS LOS CREDITO DESEMBOLSADO EN HIPOTECARIO SON REFINANCIADOS
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------TIPO DE PRODUCTO 16 (VISTA GARANTIA)------------------------------------------------

--SELECT * FROM Cabecera C WHERE C.FechaCorte1='20200531' AND TipodeProducto43=16
--41
--39--DXP
--16
--45
--34--DXP

---GENERO

select a.Genero4,count(1) from (select CodigoSocio7,c.Genero4,count(1)nro from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c
WHERE 
c.FechaCorte1='20210831' and 
c.Saldodecolocacionescreditosdirectos24>0  AND TipodeProducto43 IN (16)
group by CodigoSocio7,c.Genero4)a
group by a.Genero4

--O
--F
--M
--TIPO DE CREDITO
select 
case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end TxtTipoCredito
,sum(Saldodecolocacionescreditosdirectos24)Saldo,count(1) cantidad

from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210831' and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (16)
group by case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end


--select c.TipodeCredito19,count(1) 
--from Cabecera c WHERE c.FechaCorte1='20200531' and c.Saldodecolocacionescreditosdirectos24>0
--group by TipodeCredito19
--09
--08
--10
--13
--12
-------
--saldo de cartera bruta clasificada()
--SALDO TOTAL
--92651183.7600
--REGISTROS - 9091

select SUM(C.Saldodecolocacionescreditosdirectos24)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20200630' and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (16)
--SALDO_VIGENTE(INCLUYE CARTERA VENCIDA)
--78445950.2700
--8952
select SUM(C.Saldodecolocacionescreditosdirectos24)
from Cabecera c WHERE c.FechaCorte1='20200630' and c.Saldodecolocacionescreditosdirectos24>0
AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
AND TipodeProducto43 IN (16)



/*saldos vigente, refinanciado, judicial, vencido*/

		select SUM(C.CapitalVigente26)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210831' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (16)

		select SUM(C.CapitalRefinanciado28)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210831' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (16)

		select SUM(C.CapitalVencido29)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210831' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (16)

		select SUM(C.CapitalenCobranzaJudicial30)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210831' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (16)

		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.CapitalVencido29)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210731' 
		--and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND C.DiasdeMora33>=0  AND TipodeProducto43 IN (16)
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end 

/*saldos vigente, refinanciado, judicial, vencido*/



		--36178536.0500
		select SUM(C.Saldodecolocacionescreditosdirectos24)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210531' and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		and ISNULL(CapitalRefinanciado28,0) = 0
		and ISNULL(CapitalenCobranzaJudicial30,0) = 0
		AND C.DiasdeMora33=0 AND TipodeProducto43 IN (16)

		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.Saldodecolocacionescreditosdirectos24)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210531' and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		and ISNULL(CapitalRefinanciado28,0) = 0
		and ISNULL(CapitalenCobranzaJudicial30,0) = 0
		AND C.DiasdeMora33<>0 AND TipodeProducto43 IN (16)
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end 





--REFINANCIADOS
--51471.6300
--2108175.8100
--93
select SUM(C.Saldodecolocacionescreditosdirectos24)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20210531' 
and c.Saldodecolocacionescreditosdirectos24>0
--AND UPPER(isnull(C.TIPO_afil,'xx'))  LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
and ISNULL(CapitalRefinanciado28,0) <> 0
and ISNULL(CapitalenCobranzaJudicial30,0) = 0
AND TipodeProducto43 IN (16)
 
 --SELECT TIPO_afil,* FROM Cabecera WHERE FechaCorte1='20200630' AND TipodeProducto43=16
--SALDO JUDICIAL
--12097057.6800
--46

select SUM(ISNULL(C.Saldodecolocacionescreditosdirectos24,0))
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20210531' 
and c.Saldodecolocacionescreditosdirectos24>0 
--AND UPPER(isnull(SITUAC,'xx')) LIKE '%JU%'
and ISNULL(CapitalenCobranzaJudicial30,0) <> 0
AND TipodeProducto43 IN (16)
--SITUACION
--AC
--NULL
--OB
--JU
-----------------------
--NUMERO DE CREDITO
--9091
select COUNT(C.NumerodeCredito18)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20210831' and
 c.Saldodecolocacionescreditosdirectos24>0 AND 
 TipodeProducto43 IN (16)
--233
select 
COUNT(C.NumerodeCredito18)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210831' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (16) 
--AND UPPER(isnull(TIPO_afil,'XX')) NOT LIKE '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

----------
--MONTO DESEMBOLSADO DE LOS CREDITO
--2350355.6500
select SUM(C.MontodeDesembolso22)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE 
c.FechaCorte1='20210831' AND 
C.FechaCorte1=EOMONTH(FechadeDesembolso21)  and 
c.Saldodecolocacionescreditosdirectos24>0 
--AND UPPER(isnull(TIPO_afil,'XX')) NOT LIKE '%REF%' 
and ISNULL(CapitalRefinanciado28,0) = 0
AND TipodeProducto43 IN (16)

--SALDO CASTIGADO
--1864854.9200
select SUM(ISNULL(C.SaldosdeCreditosCastigados38,0))
from Cabecera c WHERE c.FechaCorte1='20210531'   
and c.Saldodecolocacionescreditosdirectos24=0
AND TipodeProducto43 IN (16)

---------
--SOCIOS
--
--SOCIOS NUEVOS
select 
sum(case when c.TIPO_afil like '%NVO%' then 1 else 0 end )
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20210831' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (16)

select 
COUNT(DISTINCT CodigoSocio7)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20210831' 
--AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (16)


-----saldo en monto 
select sum(ISNULL(C.MontodeDesembolso22,0))
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210831' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (16) AND 
c.Monedadelcredito17='01'
--AND (UPPER(isnull(C.TIPO_afil,'XX')) NOT LIKE '%REF%')
and ISNULL(CapitalRefinanciado28,0) = 0

----NOTA TODOS LOS CREDITO DESEMBOLSADO EN HIPOTECARIO SON REFINANCIADOS
--MONTO EN DOLARES
select sum(ISNULL(C.MontodeDesembolso22,0))
from Cabecera c WHERE c.FechaCorte1='20210731' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (16) AND 
c.Monedadelcredito17='02'
--AND (UPPER(isnull(C.TIPO_afil,'XX')) NOT LIKE '%REF%')
and ISNULL(CapitalRefinanciado28,0) = 0


SELECT * FROM Cabecera  C WHERE FechaCorte1='20210630' AND TipodeProducto43=16
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)

/************************************LIBRE DISPONIBILIDAD**********************************/
/************************************LIBRE DISPONIBILIDAD**********************************/
/************************************LIBRE DISPONIBILIDAD**********************************/
/************************************LIBRE DISPONIBILIDAD**********************************/
/************************************LIBRE DISPONIBILIDAD**********************************/

---GENERO

select a.Genero4,count(1) from (select CodigoSocio7,c.Genero4,count(1)nro from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c
WHERE 
c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0  AND TipodeProducto43 IN (30,33)
group by CodigoSocio7,c.Genero4)a
group by a.Genero4
order by Genero4 desc


--O
--F
--M
--TIPO DE CREDITO
select 
case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end TxtTipoCredito
,sum(Saldodecolocacionescreditosdirectos24)Saldo,count(1) cantidad

from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (30,33)
group by case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end





/*saldos vigente, refinanciado, judicial, vencido*/

		select SUM(C.CapitalVigente26) as 'Capital Vigente'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (30,33)

		select SUM(C.CapitalRefinanciado28) as 'Capital Refinanciado'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (30,33)

		select SUM(C.CapitalVencido29) as 'Capital Vencido'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (30,33)

		select SUM(C.CapitalenCobranzaJudicial30) as 'Cobranza Judicial'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (30,33)
-------------------------------------------------
		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.CapitalVencido29)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
		--and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND C.DiasdeMora33>=0  AND TipodeProducto43 IN (30,33)
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end 
		order by Tramos

/*saldos vigente, refinanciado, judicial, vencido*/

		
--SITUACION
--AC
--NULL
--OB
--JU
-----------------------
--NUMERO DE CREDITO
--9091
select COUNT(C.NumerodeCredito18) as 'Número de créditos'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' and
 c.Saldodecolocacionescreditosdirectos24>0 AND 
 TipodeProducto43 IN (30,33) --and UPPER(TIPO_afil) NOT like '%REF%'
--233
select COUNT(C.NumerodeCredito18) as 'N desembolsados durnte el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (30,33) 
--and UPPER(isnull(TIPO_afil,'xx')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0


----------
--MONTO DESEMBOLSADO DE LOS CREDITO
--2350355.6500
select SUM(C.MontodeDesembolso22) as 'desembolsados durante el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (30,33) 
--and UPPER(isnull(TIPO_afil,'XX')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

--SALDO CASTIGADO
--1864854.9200
select SUM(ISNULL(C.SaldosdeCreditosCastigados38,0))
from anexos_riesgos..Cabecera c WHERE c.FechaCorte1='20210630'   and c.Saldodecolocacionescreditosdirectos24=0
AND TipodeProducto43 IN (30,33)

---------
--SOCIOS
--
--SOCIOS NUEVOS
select 
FechaCorte1,sum(case when (c.TIPO_afil like '%NVO%' or c.TIPO like '%nvo%') then 1 else 0 end ) as 'nuevos(tomar fecha más reciente)'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1<='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21) 
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (30,33)
group by FechaCorte1
order by FechaCorte1


select 
COUNT(DISTINCT CodigoSocio7) as 'socios'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' 
--AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (30,33)


-----saldo en monto 
select sum(ISNULL(C.MontodeDesembolso22,0))
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (30,33) AND 
c.Monedadelcredito17='01' 
--and UPPER(ISNULL(TIPO_afil,'xx')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0


select sum(C.MontodeDesembolso22)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20210630' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (34,39) and 
c.Monedadelcredito17='02' 
--AND (UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%')
and ISNULL(CapitalRefinanciado28,0) = 0


/************************MICROEMPRESA***********************************/
/************************MICROEMPRESA***********************************/
/************************MICROEMPRESA***********************************/
/************************MICROEMPRESA***********************************/
/************************MICROEMPRESA***********************************/
/************************MICROEMPRESA***********************************/
---GENERO

select a.Genero4,count(1) from (select CodigoSocio7,c.Genero4,count(1)nro from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c
WHERE 
c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0  AND TipodeProducto43 IN (21,23,22,24,29)
group by CodigoSocio7,c.Genero4)a
group by a.Genero4
order by Genero4 desc

--O
--F
--M
--TIPO DE CREDITO
select 
case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end TxtTipoCredito
,sum(Saldodecolocacionescreditosdirectos24)Saldo,count(1) cantidad

from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (21,23,22,24,29)
group by case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end


--select c.TipodeCredito19,count(1) 
--from Cabecera c WHERE c.FechaCorte1='20200531' and c.Saldodecolocacionescreditosdirectos24>0
--group by TipodeCredito19
--09
--08
--10
--13
--12
------


/*saldos vigente, refinanciado, judicial, vencido*/

		select SUM(C.CapitalVigente26) as 'Capital vigente'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (21,23,22,24,29)

		select SUM(C.CapitalRefinanciado28) as 'Capital refinanciado'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (21,23,22,24,29)

		select SUM(C.CapitalVencido29) as 'Capital vencido'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (21,23,22,24,29)

		select SUM(C.CapitalenCobranzaJudicial30) as 'Cobranza judicial'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (21,23,22,24,29)
		-----------------------------------------------
		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.CapitalVencido29)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
		--and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND C.DiasdeMora33>=0  AND TipodeProducto43 IN (21,23,22,24,29)
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end 
		order by Tramos asc
/*saldos vigente, refinanciado, judicial, vencido*/


--SITUACION
--AC
--NULL
--OB
--JU
-----------------------
--NUMERO DE CREDITO
--9091

select COUNT(C.NumerodeCredito18) as 'Número de Créditos'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' and
 c.Saldodecolocacionescreditosdirectos24>0 AND 
 TipodeProducto43 IN (21,23,22,24,29) --and UPPER(TIPO_afil) NOT like '%REF%'
--233

select COUNT(C.NumerodeCredito18) as 'desembolsados durante el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (21,23,22,24,29)
--and UPPER(isnull(TIPO_afil,'xx')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

----------
--MONTO DESEMBOLSADO DE LOS CREDITO
--2350355.6500
select SUM(C.MontodeDesembolso22) as 'desembolsado durante el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (21,23,22,24,29)
--and UPPER(isnull(TIPO_afil,'XX')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

--SALDO CASTIGADO
--1864854.9200
select SUM(ISNULL(C.SaldosdeCreditosCastigados38,0)) as 'castigados'
from anexos_riesgos..Cabecera c WHERE c.FechaCorte1='20210630'   and c.Saldodecolocacionescreditosdirectos24=0
AND TipodeProducto43 IN (21,23,22,24,29)

---------
--SOCIOS
--
--SOCIOS NUEVOS
select 
FechaCorte1,sum(case when (c.TIPO_afil like '%NVO%' or c.TIPO_afil like '%nuev%') then 1 else 0 end ) 
as 'socios (tomar último mes)'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1<='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (21,23,22,24,29)
group by FechaCorte1
order by FechaCorte1


select 
COUNT(DISTINCT NumerodeDocumento10) as 'SOCOIS'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' 
--AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (21,23,22,24,29)


-----saldo en monto

select sum(ISNULL(C.MontodeDesembolso22,0))
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (21,23,22,24,29)
AND c.Monedadelcredito17='01' 
--and UPPER(ISNULL(TIPO_afil,'xx')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

select sum(C.MontodeDesembolso22)
from ANEXOS_RIESGOS..Cabecera c WHERE c.FechaCorte1='20210630' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (21,23,22,24,29)
and c.Monedadelcredito17='02' 
--AND (UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%')
and ISNULL(CapitalRefinanciado28,0) = 0



/************************PEQUEÑA EMPRESA***********************************/
/************************PEQUEÑA EMPRESA***********************************/
/************************PEQUEÑA EMPRESA***********************************/
/************************PEQUEÑA EMPRESA***********************************/
/************************PEQUEÑA EMPRESA***********************************/
/************************PEQUEÑA EMPRESA***********************************/
---GENERO

select a.Genero4,count(1) from (select CodigoSocio7,c.Genero4,count(1)nro from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c
WHERE 
c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0  AND TipodeProducto43 IN (15,16,17,18,19)
group by CodigoSocio7,c.Genero4)a
group by a.Genero4
order by Genero4 desc


--O
--F
--M
--TIPO DE CREDITO
select 
case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end TxtTipoCredito
,sum(Saldodecolocacionescreditosdirectos24)Saldo,count(1) cantidad

from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (15,16,17,18, 19)
group by case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end


--select c.TipodeCredito19,count(1) 
--from Cabecera c WHERE c.FechaCorte1='20200531' and c.Saldodecolocacionescreditosdirectos24>0
--group by TipodeCredito19
--09
--08
--10
--13
--12
-------
--saldo de cartera bruta clasificada()
--SALDO TOTAL
--92651183.7600
--REGISTROS - 9091

/*saldos vigente, refinanciado, judicial, vencido*/

		select SUM(C.CapitalVigente26) as 'capital vigente'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (15,16,17,18,19)

		select SUM(C.CapitalRefinanciado28) as 'capital refinanciado'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN(15,16,17,18,19)

		select SUM(C.CapitalVencido29) as 'capital vencido'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (15,16,17,18,19)

		select SUM(C.CapitalenCobranzaJudicial30) as 'cobranza judicial'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (15,16,17,18,19)
		-----------------------------------------------------------------
		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.CapitalVencido29)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
		--and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND C.DiasdeMora33>=0  AND TipodeProducto43 IN (15,16,17,18,19)
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end 

/*saldos vigente, refinanciado, judicial, vencido*/





-----------------------
--NUMERO DE CREDITO
--9091

select COUNT(C.NumerodeCredito18)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' and
 c.Saldodecolocacionescreditosdirectos24>0 AND 
 TipodeProducto43 IN (15,16,17,18,19) --and UPPER(TIPO_afil) NOT like '%REF%'
--233

select COUNT(C.NumerodeCredito18)
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (15,16,17,18,19) 
--and UPPER(isnull(TIPO_afil,'xx')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

----------
--MONTO DESEMBOLSADO DE LOS CREDITO
--2350355.6500
select SUM(C.MontodeDesembolso22) as 'monto de créditos durante el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (15,16,17,18,19)
--and UPPER(isnull(TIPO_afil,'XX')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

--SALDO CASTIGADO 'no genera los castigados durante el periodo'
--1864854.9200
select SUM(ISNULL(C.SaldosdeCreditosCastigados38,0))
from anexos_riesgos..Cabecera c WHERE c.FechaCorte1='20221231'   and c.Saldodecolocacionescreditosdirectos24=0
AND TipodeProducto43 IN (15,16,17,18,19)

---------
--SOCIOS
--
--SOCIOS NUEVOS

select 
FechaCorte1,sum(case when (c.TIPO_afil like '%NVO%' or c.TIPO_afil like '%nuev%') then 1 else 0 end )
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1<='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (15,16,17,18,19)
group by FechaCorte1
order by FechaCorte1


select 
COUNT(DISTINCT NumerodeDocumento10) as socios
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' 
--AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (15,16,17,18,19)


-----saldo en monto

select sum(ISNULL(C.MontodeDesembolso22,0))
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (15,16,17,18,19)
AND c.Monedadelcredito17='01' 
--and UPPER(ISNULL(TIPO_afil,'xx')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

select sum(C.MontodeDesembolso22)
from Cabecera c WHERE c.FechaCorte1='20210630' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (15,16,17,18,19)
and c.Monedadelcredito17='02' 
--AND (UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%')
and ISNULL(CapitalRefinanciado28,0) = 0




/************************MEDIANA EMPRESA***********************************/
/************************MEDIANA EMPRESA***********************************/
/************************MEDIANA EMPRESA***********************************/
/************************MEDIANA EMPRESA***********************************/
/************************MEDIANA EMPRESA***********************************/
/************************MEDIANA EMPRESA***********************************/
---GENERO

select a.Genero4,count(1) from (select CodigoSocio7,c.Genero4,count(1)nro from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c
WHERE 
c.FechaCorte1='20221231' and 
c.Saldodecolocacionescreditosdirectos24>0  AND TipodeProducto43 IN (95,96,97,98,99)
group by CodigoSocio7,c.Genero4)a
group by a.Genero4


--O
--F
--M
--TIPO DE CREDITO
select 
case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end TxtTipoCredito
,sum(Saldodecolocacionescreditosdirectos24)Saldo,count(1) cantidad

from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (95,96,97,98,99)
group by case 
when c.TipodeCredito19='06' then 'Créditos Corporativos'
when c.TipodeCredito19='07' then 'Créditos a Grandes Empresas'
when c.TipodeCredito19='08' then 'Créditos a Medianas Empresas'
when c.TipodeCredito19='09' then 'Créditos a Pequeñas Empresas'
when c.TipodeCredito19='10' then 'Créditos a Microempresas'
when c.TipodeCredito19='11' then 'Créditos de Consumo Revolventes'
when c.TipodeCredito19='12' then 'Créditos de Consumo No Revolventes'
when c.TipodeCredito19='13' then 'Créditos Hipotecarios para Vivienda'
when c.TipodeCredito19='20' then 'Créditos a COOPAC'
end


--select c.TipodeCredito19,count(1) 
--from Cabecera c WHERE c.FechaCorte1='20200531' and c.Saldodecolocacionescreditosdirectos24>0
--group by TipodeCredito19
--09
--08
--10
--13
--12
-------
--saldo de cartera bruta clasificada()
--SALDO TOTAL
--92651183.7600
--REGISTROS - 9091

/*saldos vigente, refinanciado, judicial, vencido*/

		select SUM(C.CapitalVigente26) as 'capital vigente'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (95,96,97,98,99)

		select SUM(C.CapitalRefinanciado28) as 'capital refinanciado'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN(95,96,97,98,99)

		select SUM(C.CapitalVencido29) as 'capital vencido'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (95,96,97,98,99)

		select SUM(C.CapitalenCobranzaJudicial30) as 'capital en cobranza judicial'
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' and c.Saldodecolocacionescreditosdirectos24>0
		AND TipodeProducto43 IN (95,96,97,98,99)
		----------------------------------------------------------------
		select 
		CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end Tramos  ,
		SUM(C.CapitalVencido29)
		from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
		--and c.Saldodecolocacionescreditosdirectos24>0
		--AND UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%' AND (C.SITUAC<>'JU' OR C.SITUAC IS NULL)
		AND C.DiasdeMora33>=0  AND TipodeProducto43 IN (95,96,97,98,99)
		group by CASE
		WHEN C.DiasdeMora33>0 AND C.DiasdeMora33<=30 THEN 'a.[01-30]' 
		WHEN C.DiasdeMora33>30 AND C.DiasdeMora33<=60 THEN 'b.[31-60]'
		WHEN C.DiasdeMora33>60 AND C.DiasdeMora33<=90 THEN 'c.[61-90]'
		WHEN C.DiasdeMora33>90 AND C.DiasdeMora33<=180 THEN 'd.[91-180]'
		WHEN C.DiasdeMora33>180 AND C.DiasdeMora33<=365 THEN 'e.[181-365]'
		else 'f.[+365>'end 

/*saldos vigente, refinanciado, judicial, vencido*/





-----------------------
--NUMERO DE CREDITO
--9091

select COUNT(C.NumerodeCredito18) as 'número de créditos'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' and
 c.Saldodecolocacionescreditosdirectos24>0 AND 
 TipodeProducto43 IN (95,96,97,98,99) --and UPPER(TIPO_afil) NOT like '%REF%'
--233

select COUNT(C.NumerodeCredito18) as 'número de créditos desembolsados durante el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (95,96,97,98,99)
--and UPPER(isnull(TIPO_afil,'xx')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

----------
--MONTO DESEMBOLSADO DE LOS CREDITO
--2350355.6500
select SUM(C.MontodeDesembolso22) as 'monto desembolsado durante el periodo'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (95,96,97,98,99)
--and UPPER(isnull(TIPO_afil,'XX')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

--SALDO CASTIGADO
--1864854.9200
select SUM(ISNULL(C.SaldosdeCreditosCastigados38,0))
from Cabecera c WHERE c.FechaCorte1='20210630'   and c.Saldodecolocacionescreditosdirectos24=0
AND TipodeProducto43 IN (15,16,17, 18, 19)

---------
--SOCIOS
--
--SOCIOS NUEVOS
select 
sum(case when c.TIPO_afil like '%NVO%' then 1 else 0 end ) as 'socios nuevos'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' 
AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (95,96,97,98,99)

--total de socios
select 
COUNT(DISTINCT NumerodeDocumento10) as 'total de socios'
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c 
WHERE c.FechaCorte1='20221231' 
--AND C.FechaCorte1=EOMONTH(FechadeDesembolso21)  
and c.Saldodecolocacionescreditosdirectos24>0
AND TipodeProducto43 IN (95,96,97,98,99)


-----saldo en monto

select sum(ISNULL(C.MontodeDesembolso22,0))
from EXPERIMENTOS..COPIAPRUEBAJUANJOSE c WHERE c.FechaCorte1='20211231' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (15,16,17, 18, 19)
AND c.Monedadelcredito17='01' 
--and UPPER(ISNULL(TIPO_afil,'xx')) NOT like '%REF%'
and ISNULL(CapitalRefinanciado28,0) = 0

select sum(C.MontodeDesembolso22)
from Cabecera c WHERE c.FechaCorte1='20210630' and 
c.Saldodecolocacionescreditosdirectos24>0 and 
C.FechaCorte1=EOMONTH(FechadeDesembolso21) and 
C.TipodeProducto43 IN (15,16,17, 18, 19)
and c.Monedadelcredito17='02' 
--AND (UPPER(ISNULL(C.TIPO_afil,'XX')) NOT LIKE '%REF%')
and ISNULL(CapitalRefinanciado28,0) = 0






