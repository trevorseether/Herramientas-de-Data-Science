declare @fechacorte as datetime
set @fechacorte = '20230228'


---------------
SELECT Nro_Fincore, CodigoSocio7, NumerodeCredito18, Monedadelcredito17, ApellidosyNombresRazonSocial2,
Saldodecolocacionescreditosdirectos24, CapitalenCobranzaJudicial30,
CapitalVencido29, A.NUEVA_PLANILLA, ClasificaciondelDeudorconAlineamiento15, Nro,
Situacion_Credito, Origen_Coopac, P.EMPRESA, P.PLANILLA_CORREGIDA
,
'=BUSCARV(ESPACIOS(I2);[poner aqui la columna];1;0)' AS 'BUSQUEDA1 (NUEVA_PLANILLA)',
'=BUSCARV(ESPACIOS(O2);[poner aqui la columna];1;0)' AS 'BUSQUEDA2 (PLANILLA_CORREGIDA)', 
CASE
WHEN ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) = 1 
THEN '=SI.ERROR(ESPACIOS(Q2);SI.ERROR(ESPACIOS(P2);"BUSCAR"))' ELSE '' END AS 'BUSQUEDA3 (corregido)',
CASE
WHEN ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) = 1 
THEN '=ESPACIOS(O2)=ESPACIOS(O3)' ELSE '' END AS 'VERIFICADOR DE IGUALDAD',
'' AS 'IMPORTE ENVIADO S/.',
'' AS 'RECIBIDO MASIVO',
'' AS 'RECIBIDO INDEP.',
'' AS 'CUOTA MES CON LIQUIDACION',
'' AS 'PAGO JUDICIALES',
'' AS 'PAGO EXCEDENTE LIQUIDACIÓN',
CASE
WHEN ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) = 1 
THEN '=SI.ERROR(T2;0)' ELSE '' END AS 'Desc_Envio',
CASE
WHEN ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) = 1 
THEN '=SUMA(U2:Y2)' ELSE '' END AS 'Desc_Pago',
CASE
WHEN ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) = 1 
THEN '=SI.ERROR(AA2/Z2;0)' ELSE '' END AS 'RECAUDACIÓN'


FROM  anexos_riesgos2..Anx06_preliminar A

LEFT JOIN Anexos_Riesgos..PLANILLA2 P
ON (LTRIM(RTRIM(A. NUEVA_PLANILLA)) =  LTRIM(RTRIM(P.NUEVA_PLANILLA)))
WHERE FechaCorte1 = @fechacorte

ORDER BY A.NUEVA_PLANILLA

------------SI SE ENCUENTRA ALGUNA CORRESPONDENCIA, LA COLUMNA PLANILLA_CORREGIDA SE PEGA EN
------------EL REPORTE DE RECAUDACIÓN DE HARRIS, PARA QUE HAGA MATCH
----------------------------------------------------------------------------
-- codigo para hacer la tablita que se subirá al SQL
SELECT FechaCorte1 as 'FechaCorte',
	CodigoSocio7 as 'CodSocio',
	NumerodeCredito18 as 'CodCredito',
	Monedadelcredito17 as 'CodMoneda',
	'' as 'Desc_Envio',
	'' as 'Desc_pago',
	'' as 'recaudacion',
	Nro_Fincore as 'Nro_Fincore'

FROM  anexos_riesgos2..Anx06_preliminar A
where FechaCorte1 = @fechacorte

----------------------------------------------------------------------------

---buscando los nombres
declare @texto as varchar(50) = '%SALES%'
select * from Anexos_Riesgos..planilla2
where NUEVA_PLANILLA like @texto
or NUEVA_PLANILLA_creada like @texto

----------------------------------------------------------------------
--INSERT INTO Anexos_Riesgos..planilla2
--VALUES (
--'ASOCIACIONES DE TRABAJADORES DEL SENATI - A.T.S.',
--'ASOCIACIONES DE TRABAJADORES DEL SENATI - A.T.S.',
--'ASOCIACIONES DE TRABAJADORES DEL SENATI - A.T.S.',
--''
--)


----------------------------------------------------------------------
--para insertar la recaudación una vez creada
--insert into Anexos_Riesgos..Cabecera_Pagos
--select * from Anexos_Riesgos2.recaudacion.recaudacion20230228
----------------

----creando un esquema nuevo para más orden
/*
use anexos_riesgos2
go
CREATE SCHEMA recaudacion
go
*/

