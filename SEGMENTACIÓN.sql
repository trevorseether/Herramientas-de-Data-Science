------------------------------------------------------------------------------
--ESTE CÓDIGO YA ES OBSOLETO, HAY OTRO QUE HACE TODO EL TRABAJO EN PYTHON-----
------------------------------------------------------------------------------
--SE TRATA DE 'AVALES SEGMENTACION.py'
--CUYA UBICACIÓN ES:
--C:\Users\sanmiguel38\Desktop\Joseph\QUERYS\python scripts

----CODIGO PARA GENERAR EL REPORTE DE SEGMENTACIÓN DE CADA MES
--ESTE CÓDIGO ES LA PRIMERA PARTE DEL PROCESO, SOLO SE DEBE CAMBIAR LA FECHA DE CORTE

declare @fechacorte datetime
set @fechacorte = '20230228'


select NumerodeDocumento10 as 'DNI SOCIOS', 
Saldodecolocacionescreditosdirectos24 AS 'SALDO DE CARTERA',
Saldodecolocacionescreditosdirectos24-IngresosDiferidos42 AS 'SALDO DE CARTERA NETA',--???? consultar
TipodeCredito19 AS 'TIPO DE CREDITO',
Situacion_Credito AS 'SITUACION',
DiasdeMora33 AS 'DIAS DE ATRASO',
NumerodeCuotasProgramadas44 AS 'PLAZO TOTAL',
PeriododeGracia47 AS 'PLAZO DE GRACIA',
TipodePersona11 AS 'TIPO DE SOCIO',
'CREDITOS - DIRECTOS' as 'MODALIDAD CREDITICIA',
'' AS 'Dni - Asociado - indirecta',
ClasificaciondelDeudorconAlineamiento15 AS 'CLASIFICACION CREDITICIA'

from anexos_riesgos2..Anx06_preliminar
where FechaCorte1 = @fechacorte
and SaldosdeCreditosCastigados38 = 0

----POSTERIORMENTE A LA GENERACIÓN DE ESTE EXCEL
/* 
TE ENVIAN EL ARCHIVO DE AVALES, SE SUMA A LOS AVALES HISTÓRICOS, LUEGO SE HACE UN MATCH CON LOS DNI QUE ESTÁN EN LA LISTA DE SEGMENTACIÓN
Y SE VUELVE A DUPLICAR LOS QUE HACEN MATCH AL FINAL, Y LE AGREGAS EL DNI DEL AVAL, Y EN MODALIDAD LE PONES CREDITOS-INDIRECTOS
*/

