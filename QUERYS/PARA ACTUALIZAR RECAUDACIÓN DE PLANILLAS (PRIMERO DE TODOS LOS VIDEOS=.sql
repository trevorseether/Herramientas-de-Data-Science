SELECT Nro_Fincore, CodigoSocio7, NumerodeCredito18, Monedadelcredito17, ApellidosyNombresRazonSocial2,
Saldodecolocacionescreditosdirectos24, CapitalenCobranzaJudicial30,
CapitalVencido29, A.NUEVA_PLANILLA, ClasificaciondelDeudorconAlineamiento15, Nro,
Situacion_Credito, Origen_Coopac, P.EMPRESA, P.PLANILLA_CORREGIDA

FROM  experimentos..copiapruebajuanjose A

LEFT JOIN Anexos_Riesgos..PLANILLA2 P
ON (LTRIM(RTRIM(A. NUEVA_PLANILLA)) =  LTRIM(RTRIM(P.NUEVA_PLANILLA)))
WHERE FechaCorte1 = '20221130'


----------------------------------------------------------------------------
-- codigo para hacer la tablita que se subirá al SQL
SELECT FechaCorte1 as 'FechaCorte',
	CodigoSocio7 as 'CodSocio',
	NumerodeCredito18 as 'CodCredito',
	Monedadelcredito17 as 'CodMoneda',
	null as 'Desc_Envio',
	null as 'Desc_pago',
	null as 'recaudacion',
	Nro_Fincore as 'Nro_Fincore'

FROM  experimentos..copiapruebajuanjose A
where FechaCorte1 = '20221130'

----------------------------------------------------------------------------

---buscando los nombres
declare @texto as varchar(50) = '%anka%'
select * from Anexos_Riesgos..planilla2
where NUEVA_PLANILLA like @texto
or NUEVA_PLANILLA_creada like @texto

----------------------------------------------------------------------

insert into Anexos_Riesgos..Cabecera_Pagos
select * from Anexos_Riesgos..recaudacion20221130


select * from Anexos_Riesgos..cabecera_pagos
where FechaCorte = '20221130'

select * from Comercial..anx06
select * from Anexos_Riesgos..anx06_20221130
