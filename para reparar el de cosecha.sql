---codigo para arreglar la tabla si se daña
drop table experimentos..ENVEJE_REPARADO
select
FechaCorte1 AS Mes_Origen,FechaCorte1 AS Mes_Corte ,ApellidosyNombresRazonSocial2 AS ApellidosyNombresRazonSocial2,
NumerodeDocumento10  AS NumerodeDocumento10, Nro_Fincore AS Nro_Fincore, FechadeDesembolso21 AS FechadeDesembolso21,
MontodeDesembolso22 AS MontodeDesembolso22,
TasadeInteresAnual23 AS TasadeInteresAnual23, Saldodecolocacionescreditosdirectos24 AS Saldodecolocacionescreditosdirectos24,
CapitalVigente26 AS CapitalVigente26,CapitalReestrucutado27 AS CapitalReestrucutado27, 
CapitalRefinanciado28 AS CapitalRefinanciado28,
CapitalVencido29 AS CapitalVencido29, CapitalenCobranzaJudicial30 AS CapitalenCobranzaJudicial30,
TipodeProducto43 AS TipodeProducto43, NUEVA_PLANILLA AS NUEVA_PLANILLA, 
NUEVO_PROMOTOR AS NUEVO_PROMOTOR,EMPRESA AS EMPRESA,
ClasificaciondelDeudorconAlineamiento15 AS Clasificacion_Corte_anterior,
ClasificaciondelDeudorconAlineamiento15 AS Clasificacion_corte_actual, DiasdeMora33 AS Dias_mora_mes_anterior , 
DiasdeMora33 AS Dias_mora_mes_analisis, Saldodecolocacionescreditosdirectos24 AS Saldo_mes_anterior
into experimentos..ENVEJE_REPARADO
from Comercial..Anx06 
where FechaCorte1 = '20211231'
------
exec envej_reparado2 '20220131'
exec envej_reparado2 '20220228'
exec envej_reparado2 '20220331'
exec envej_reparado2 '20220430'
exec envej_reparado2 '20220531'
exec envej_reparado2 '20220630'
exec envej_reparado2 '20220731'
exec envej_reparado2 '20220831'
exec envej_reparado2 '20220930'
exec envej_reparado2 '20221031'
exec anexos_riesgos..envej_reparado2 '20221130'
exec anexos_riesgos..envej_reparado2 '20221231' 
exec ENVEJECIMIENTO..envejecimiento_reporte '20230131' ---hasta aquí se ha ejecutado
exec ENVEJECIMIENTO..envejecimiento_reporte '20230228' ---hasta aquí se ha ejecutado
---

--------------------ejecutar este código antes de ejecutar el procedimiento de cosecha
--------------------este código es para reemplazar todo el archivo comercial..anx06
--drop table comercial..anx06
--select * 
--into comercial..anx06
--from experimentos..copiapruebajuanjose

----------------------en caso solo quieras añadir el último anx06
------INSERT INTO Comercial..anx06
------SELECT * FROM experimentos..copiapruebajuanjose
------WHERE FechaCorte1 = '20221231'


-------------------------------------------------------------------------------------------
---codigo para arreglar la tabla si se daña
drop table experimentos..ENVEJE_REPARADO
select
FechaCorte1 AS Mes_Origen,FechaCorte1 AS Mes_Corte ,ApellidosyNombresRazonSocial2 AS ApellidosyNombresRazonSocial2,
NumerodeDocumento10  AS NumerodeDocumento10, Nro_Fincore AS Nro_Fincore, FechadeDesembolso21 AS FechadeDesembolso21,
MontodeDesembolso22 AS MontodeDesembolso22,
TasadeInteresAnual23 AS TasadeInteresAnual23, Saldodecolocacionescreditosdirectos24 AS Saldodecolocacionescreditosdirectos24,
CapitalVigente26 AS CapitalVigente26,CapitalReestrucutado27 AS CapitalReestrucutado27, 
CapitalRefinanciado28 AS CapitalRefinanciado28,
CapitalVencido29 AS CapitalVencido29, CapitalenCobranzaJudicial30 AS CapitalenCobranzaJudicial30,
TipodeProducto43 AS TipodeProducto43, NUEVA_PLANILLA AS NUEVA_PLANILLA, 
NUEVO_PROMOTOR AS NUEVO_PROMOTOR,EMPRESA AS EMPRESA,
ClasificaciondelDeudorconAlineamiento15 AS Clasificacion_Corte_anterior,
ClasificaciondelDeudorconAlineamiento15 AS Clasificacion_corte_actual, DiasdeMora33 AS Dias_mora_mes_anterior , 
DiasdeMora33 AS Dias_mora_mes_analisis, Saldodecolocacionescreditosdirectos24 AS Saldo_mes_anterior
into experimentos..ENVEJE_REPARADO
from Comercial..Anx06 
where FechaCorte1 = '20200131'
------
exec envej_reparado2 '20200229'
exec envej_reparado2 '20200331'
exec envej_reparado2 '20200430'
exec envej_reparado2 '20200531'
exec envej_reparado2 '20200630'
exec envej_reparado2 '20200731'
exec envej_reparado2 '20200831'
exec envej_reparado2 '20200930'
exec envej_reparado2 '20201031'
exec envej_reparado2 '20201130'
exec envej_reparado2 '20201231' -------este posiblemente tiene un error [Error al convertir el tipo de datos varchar a datetime]]]]]]]]]]

exec envej_reparado2 '20210131'
exec envej_reparado2 '20210229'
exec envej_reparado2 '20210331'
exec envej_reparado2 '20210430'
exec envej_reparado2 '20210531'
exec envej_reparado2 '20210630'
exec envej_reparado2 '20210731'
exec envej_reparado2 '20210831'
exec envej_reparado2 '20210930'
exec envej_reparado2 '20211031'
exec envej_reparado2 '20211130'
exec envej_reparado2 '20211231'

exec envej_reparado2 '20220131'
exec envej_reparado2 '20220228'
exec envej_reparado2 '20220331'
exec envej_reparado2 '20220430'
exec envej_reparado2 '20220531'
exec envej_reparado2 '20220630'
exec envej_reparado2 '20220731'
exec envej_reparado2 '20220831'
exec envej_reparado2 '20220930'
exec envej_reparado2 '20221031'
exec anexos_riesgos..envej_reparado2 '20221130'
