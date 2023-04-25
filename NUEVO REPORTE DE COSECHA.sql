--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
-----------------------PARA AÑADIR LO QUE FALTA AL REPORTE DE cosecha..cosecha_nuevo--------------
--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
--drop table cosecha..cosecha_nuevo
--select * 
--into cosecha..cosecha_nuevo
--from experimentos..copiapruebajuanjose
--update cosecha..cosecha_nuevo
--set MCastigadoxM = 0
---    [DESEMBOLSO_AGREGADO]


--SELECT * 
--INTO cosecha..cosecha_nuevoCOPIANOV2022
--FROM cosecha..cosecha_nuevo

---------------ANTES DE AÑADIR UN NUEVO MES SE DEBE AÑADIR DEL ANEXO6
--SELECT * 
--INTO cosecha..cosecha_nuevo
--FROM experimentos..copiapruebajuanjose AS A
--WHERE A.FechaCorte1 = '20221231'  -- AQUÍ VA LA MÁS RECIENTE

declare @fechaactual as datetime
set @fechaactual = '20220131' ---- hay que añadir los datos desde adelante hasta atrás, por un año
---- tema pendiente, aprender a usar cursores para añadir estos resultados
INSERT INTO cosecha..cosecha_nuevo (
nro_fincore,
FechadeDesembolso21,
FechaCorte1,
ApellidosyNombresRazonSocial2,
Saldodecolocacionescreditosdirectos24, ---aqui va cero
CapitalVencido29, ------------------------aqui va cero
nuevo_capitalvencido, --------------------aqui va cero
CapitalenCobranzaJudicial30,--------------aqui va cero
MontodeDesembolso22,----------------------aqui va cero
MDesembolsadoxM,
TipodeProducto43,
PROMOTOR,
NUEVO_PROMOTOR,
administrador,
--MCastigadoxM,
MtotalDesembolsadoxM,
Departamento,
provincia,
Distrito,
NumerodeCredito18,
Refinanciado,
Reprogramados52,
Monedadelcredito17,
TipodeDocumento9,
NumerodeDocumento10,
originador)

select
a.nro_fincore,
a.FechadeDesembolso21,
@fechaactual, ---aqui va la fecha de corte en la que se van a insertar datos
a.ApellidosyNombresRazonSocial2,
0, ----SALDO DE CRÉDITO 24
0, ----CAPITAL VENCIDO 29
0, ----NUEVO CAP VENCIDO (DESPUÉS DEL CAMBIO DE METODOLOGÍA PARA MYPE)
0, ----CAPITAL EN COBRANZA JUDICIAL 30
0, ---- MONTO DESEMBOLSADO 22
A.MDesembolsadoxM,
a.TipodeProducto43,
a.PROMOTOR,
a.NUEVO_PROMOTOR,
a.administrador,
--a.MCastigadoxM,
a.MtotalDesembolsadoxM,
a.Departamento,
a.provincia,
a.Distrito,
a.NumerodeCredito18,
a.Refinanciado,
a.Reprogramados52,
A.Monedadelcredito17,
A.TipodeDocumento9,
A.NumerodeDocumento10,
a.originador

FROM EXPERIMENTOS..COPIAPRUEBAJUANJOSE AS A
---     select * from EXPERIMENTOS..COPIAPRUEBAJUANJOSE as A
where DATENAME(MONTH,a.FechaCorte1) = DATENAME(MONTH,a.FechadeDesembolso21)
and year(a.FechaCorte1) = year(a.FechadeDesembolso21)
and a.fechacorte1 < @fechaactual
order by FechaCorte1
--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
------------------------HASTA AQUI SE HA INGRESADO TODO MENOS MtotalCastigadoxM-------------
--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------

---AHORA SÍ, PROCEDEMOS CON EL PASO FINAL
--declare @fechaactual as datetime
--set @fechaactual = '20221130'
/*
INSERT INTO COSECHA..COSECHA (
FechadeDesembolso21,
NRO_FINCORE,
MCastigadoxM,
FechaCorte1,
ApellidosyNombresRazonSocial2,
TipodeProducto43,
PROMOTOR,
NUEVO_PROMOTOR,
administrador,
Departamento,
provincia,
Distrito,
NumerodeCredito18,
Refinanciado,
Reprogramados52,
Monedadelcredito17,
TipodeDocumento9,
NumerodeDocumento10,
originador
)
SELECT 
a.FechadeDesembolso21,
A.NRO_FINCORE, 
A.MCastigadoxM,
@fechaactual,
A.ApellidosyNombresRazonSocial2,
A.TipodeProducto43,
A.PROMOTOR,
A.NUEVO_PROMOTOR,
A.administrador,
a.Departamento,
a.provincia,
a.Distrito,
a.NumerodeCredito18,
a.Refinanciado,
a.Reprogramados52,
A.Monedadelcredito17,
A.TipodeDocumento9,
A.NumerodeDocumento10,
a.originador

FROM experimentos..copiapruebajuanjose AS A
where MCastigadoxM > 0

*/