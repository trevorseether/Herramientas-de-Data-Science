
---------query para el reporte trimestral anteriormente conocido como:
--------------	Base cuadrantes
--------------  ahora es LABORATORIO DE CLIENTES TRIMESTRAL ENE - FEB - MAR - 2023

select
TipodeDocumento9 as 'cli_tipo_doc',
NumerodeDocumento10 as 'cli_nro_doc',
ApellidosyNombresRazonSocial2 as 'cli_nombre',
CONVERT(varchar,FechaCorte1,112) as 'cli_periodo',
Saldodecolocacionescreditosdirectos24 as 'cli_deuda',
Monedadelcredito17 as 'cli_moneda',
TipodeCredito19 as 'cli_tipo_credito',
DiasdeMora33 as 'cli_dias_mora',
iif(CuentaContableCreditoCastigado39 >0,'1', '0') as 'cli_castigo',
iif(tipodecredito19 = '13','1', '0') as 'cli_garantia'
from anexos_riesgos2..Anx06_preliminar
where FechaCorte1 >= '20230131'
order by FechaCorte1, cli_nombre

