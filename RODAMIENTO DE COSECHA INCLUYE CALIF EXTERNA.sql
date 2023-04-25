------RODAMIENTO DE COSECHA CALIF EXTERNA---------------
--------------------------------------------------------
--172.16.1.162
select a.FechaCorte1 Mes_Corte_Grafico, a.FechaCorte1 Mes_Corte, a.FechadeDesembolso21 Mes_Desembolso,concat(DATENAME(MONTH, a.FechadeDesembolso21),'/', year(a.FechadeDesembolso21)) Mes_desembolso,
concat(DATENAME(MONTH, a.FechaCorte1),'/', year(a.FechaCorte1)) Mes_corte2
 ,a.NumerodeDocumento10, a.TipodeDocumento9, a.CodigoSocio7, a.ApellidosyNombresRazonSocial2, 
 c.calif_externa, c.calif_externa_calculada,
 a.NumerodeCredito18,a.nro_fincore,A.MDesembolsadoxM,a.Monedadelcredito17,a.MontodeDesembolso22, 
 a.Saldodecolocacionescreditosdirectos24, a.CapitalVencido29, a.nuevo_capitalvencido, a.CapitalenCobranzaJudicial30,
a.CarteraAtrasada, a.NUEVO_PROMOTOR AS ORIGINADOR,A.PROMOTOR,A.NUEVO_PROMOTOR, a.administrador, a.TipodeProducto43, a.FechadeNacimiento3, 
a.SaldodeGarantiasAutoliquidables35,a.SaldosdeCreditosCastigados38 ,a.mcastigadoxm,A.MtotalCastigadoxM,
iif(a.SaldosdeCreditosCastigados38>0,'CASTIGADO','VIGENTE')ESTAO,b.NUEVA_PLANILLA_creada Planilla2, a.NUEVA_PLANILLA,

CASE WHEN NUEVO_PROMOTOR LIKE '%PROSEVA%' OR  NUEVO_PROMOTOR LIKE '%CAÑETE%' THEN 'PROVINCIA'
	ELSE 'LIMA' END AS 'FILTRO_PROVINCIA',

CASE 
	WHEN a.NUEVO_PROMOTOR LIKE '%PIURA%' THEN 'PIURA' 
	WHEN a.NUEVO_PROMOTOR LIKE '%CHINCHA%' THEN 'CHINCHA'
	WHEN a.NUEVO_PROMOTOR LIKE '%TACNA%' THEN 'TACNA'
	WHEN a.NUEVO_PROMOTOR LIKE '%CHICLAYO%' THEN 'CHICLAYO'
	WHEN a.NUEVO_PROMOTOR LIKE '%AREQUIPA%' THEN 'AREQUIPA'
	WHEN a.NUEVO_PROMOTOR LIKE '%ICA%' and a.NUEVO_PROMOTOR not like '%ricardo%' THEN 'ICA'
	WHEN a.NUEVO_PROMOTOR LIKE '%HUACHO%' THEN 'HUACHO'
	WHEN a.NUEVO_PROMOTOR LIKE '%JAEN%' THEN 'JAEN'
	WHEN a.NUEVO_PROMOTOR LIKE '%TRUJILLO%' THEN 'TRUJILLO'
	WHEN a.NUEVO_PROMOTOR LIKE '%TUMBES%' THEN 'TUMBES'
	WHEN a.NUEVO_PROMOTOR LIKE '%CAÑETE%' THEN 'CAÑETE'
	WHEN a.NUEVO_PROMOTOR LIKE '%CAJAMARCA%' THEN 'CAJAMARCA'
	when a.NUEVO_PROMOTOR like '%TARAPOTO%' then 'TARAPOTO'
	when a.NUEVO_PROMOTOR like '%CUSCO%' OR a.NUEVO_PROMOTOR like '%CUZCO%' then 'CUSCO'

ELSE 'LIMA' END ZONAS,
CASE WHEN a.TipodeProducto43 in (21,22,23,24,25,29) THEN 'MICRO EMPRESA'  ----------------------------faltaban 21,24,25,29
WHEN a.TipodeProducto43 in (30,33, 31, 32) THEN 'LIBRE DISPONIBILIDAD'  ------------------------------fatlaban 31,32
WHEN a.TipodeProducto43 IN (16,15,17,18,19) and a.FechaCorte1>='20210930' THEN 'PEQUEÑA EMPRESA'----------fatlaban 18,19
WHEN a.TipodeProducto43 IN (41,45) THEN 'HIPOTECARIO'
WHEN a.TipodeProducto43 IN (34,39,35,36) THEN 'DXP'
else 'OTROS' end Producto,

case 
when a.NUEVO_PROMOTOR like '%Alicia%' or a.NUEVO_PROMOTOR like '%andrea bilbao%' or a.NUEVO_PROMOTOR like '%borja%' or a.NUEVO_PROMOTOR like '%giovanna%' or a.NUEVO_PROMOTOR like '%gustavo%' or a.NUEVO_PROMOTOR like '%july%' or a.NUEVO_PROMOTOR like '%elias%' OR a.NUEVO_PROMOTOR LIKE '%RAMOS%' then 'ILLIANOVICH PAREJA'
WHEN a.NUEVO_PROMOTOR like '%AZUCENA%' or a.NUEVO_PROMOTOR like '%CHUQUISUTA%' or a.NUEVO_PROMOTOR like '%ludhiana%' or a.NUEVO_PROMOTOR like '%maldonado%' or a.NUEVO_PROMOTOR like '%roxana%' or a.NUEVO_PROMOTOR like '%laureano%' then 'KARL AZAHUANCHE'
WHEN a.NUEVO_PROMOTOR like '%PROSEVA%' then 'EDUARDO SALAS' 
ELSE 'OTROS'END 'SUPERVISORES'

from experimentos..copiaanx06cosecha22222222222222222222222 a
left join Anexos_Riesgos..planilla2 b
on(a.NUEVA_PLANILLA=b.NUEVA_PLANILLA)
left join Anexos_Riesgos..laboratorio_clientes_junio  c
on  (a.NumerodeDocumento10=c.documentoidenti and c.documentoidenti is not null and cli_periodo='20220630')