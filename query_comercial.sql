/*
ahora todos los anexos estarán en anexos_riesgos2
*/
use Comercial
go
/*
los anexos06 actuales son

ANEXOS_RIESGOS2..Anx06_preliminar
ANEXOS_RIESGOS2..Anx06

*/

--en el excel, primero eliminar filas y columnas vacías, por si acaso
--segundo, aplicar formato texto desde D hasta K, y desde M hasta T
--arreglar la fecha de desembolso con esta fórmula, creando una columna a su derecha:
--=AÑO(V2)&DERECHA("00"&MES(V2);2)&DERECHA("00"&DIA(V2);2)
--------------------------------------------------------------------------------------------------
--una vez subido el anexo06 del mes, nos vamos a ejecutar el procedimiento almacenado
--este anexo debe estar como dbo.Anx06_20230131

---------------------------------Aquí creando una copia por si se malogra la tabla 'Cabecera'
--select *
--into anexos_riesgos2..cabecera_copia_febero2023 ---aqui hay una copia antes del corte de enero 2023
--from anexos_riesgos2..cabecera order by FechaCorte1

--drop table anexos_riesgos2..cabecera

--select *
--into  anexos_riesgos2..cabecera ----renovando la tabla cabecera si es que salió mal
--from anexos_riesgos2..cabecera_copia_enero2023


exec [Anexos_Riesgos2].[dbo].[SP_Cabecera] '20230331'                    -------en marzo ha funcionado, sino hay que abrir y meterlo desde adentro uwu
exec [Anexos_Riesgos2].[dbo].[SP_HELPNRO_CABECERA] '20230331'
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
if OBJECT_ID('TEMPDB..#T')IS NOT NULL 
DROP TABLE #T
select a.NumerodeCredito18,Monedadelcredito17,a.NUEVO_PROMOTOR,a.PROMOTOR,a.NUEVA_PLANILLA,TIPO, Nro_Fincore,ADMINISTRADOR, TipodeProducto43
INTO #T
from Anexos_Riesgos2..Anx06_preliminar a 
where a.FechaCorte1='20230228' -- aqui se pone el de hace 2 meses

--codigo para eliminar si es que hay mes actual y salió mal
delete from Anexos_Riesgos2..Anx06_preliminar where FechaCorte1='20230331'--AQUI SE PONE EL MES PASADO

--UPDATE A SET 
--A.PLANILLA=C.PLANILLA
----SELECT C.PLANILLA,A.PLANILLA,C.* 
--FROM Anexos_Riesgos..Cabecera C 
--JOIN #ANXII06 A ON (C.NumerodeCredito18=A.NumerodeCredito18 AND C.Monedadelcredito17=A.Monedadelcredito17)
--WHERE C.PLANILLA<>A.PLANILLA AND C.FechaCorte1='20200630'

--que quede precedente de que tuve que modificar el tipo de dato de una columna porque no entraba en la celda
--alter table anexos_riesgos2..anx06_preliminar alter column [TIPO_afil] varchar(255)


insert into Anexos_Riesgos2..Anx06_preliminar (
[FechaCorte1]
      ,[ApellidosyNombresRazonSocial2]
      ,[FechadeNacimiento3]
      ,[Genero4]
      ,[EstadoCivil5]
      ,[SigladelaEmpresa6]
      ,[CodigoSocio7]
      ,[PartidaRegistral8]
      ,[TipodeDocumento9]
      ,[NumerodeDocumento10]
      ,[TipodePersona11]
      ,[Domicilio12]
      ,[RelacionLaboralconlaCooperativa13]
      ,[ClasificaciondelDeudor14]
      ,[ClasificaciondelDeudorconAlineamiento15]
      ,[CodigodeAgencia16]
      ,[Monedadelcredito17]
      ,[NumerodeCredito18]
      ,[TipodeCredito19]
      ,[SubTipodeCredito20]
      ,[FechadeDesembolso21]
      ,[MontodeDesembolso22]
      ,[TasadeInteresAnual23]
      ,[Saldodecolocacionescreditosdirectos24]
      ,[CuentaContable25]
      ,[CapitalVigente26]
      ,[CapitalReestrucutado27]
      ,[CapitalRefinanciado28]
      ,[CapitalVencido29]
      ,[CapitalenCobranzaJudicial30]
      ,[CarteraAtrasada]
      ,[CapitalContingente31]
      ,[CuentaContableCapitalContingente32]
      ,[DiasdeMora33]
      ,[SaldosdeGarantiasPreferidas34]
      ,[SaldodeGarantiasAutoliquidables35]
      ,[ProvisionesRequeridas36]
      ,[ProvisionesConstituidas37]
      ,[SaldosdeCreditosCastigados38]
      ,[CuentaContableCreditoCastigado39]
      ,[Rendimiento_Devengado40]
      ,[InteresesenSuspenso41]
      ,[IngresosDiferidos42]
      ,[TipodeProducto43]
      ,[NumerodeCuotasProgramadas44]
      ,[NumerodeCuotasPagadas45]
      ,[Periodicidaddelacuota46]
      ,[PeriododeGracia47]
      ,[FechadeVencimientoOriguinaldelCredito48]
      ,[FechadeVencimientoAnualdelCredito49]
      ,[SITUAC]
      ,[FEC_SIT]
      ,[TIPO_afil]
      ,[AMORTIZA]
      ,[PROMOTOR]---------------------------
      ,[PLANILLA]
      ,[REGIMEN_LABORAL]
      ,[ESTADO]
      ,[CAMPAÑA]
      ,[EMPRESA]
      ,[IMPORTE_A_DESCONTAR]
      ,[IMPORTE_PAGADO]
      ,[Nro]
      ,[Reprogramados]
      ,[MDesembolsadoxM]
      ,[mora]
     -- ,[NUEVO_PROMOTOR]
      --,[Situacion_Credito]
      --,[TIPO]
	  ,Origen_Coopac
	  ,[Nro_Fincore]
	  ,Departamento
	  ,Provincia
	  ,Distrito
	  ,Reprogramados52
	  ,Refinanciado
	  ,nuevo_capitalvencido
	  ,originador
	  ,[Funcionario Actual]
	  ,[Nombre Negocio]
	  ,[Domicilio Negocio]
	  ,[Distrito Negocio]
	  ,[Dpto Negocio] 
	  ,[Provincia Negocio] )
SELECT c.[FechaCorte1]
      ,c.[ApellidosyNombresRazonSocial2]
      ,c.[FechadeNacimiento3]
      ,c.[Genero4]
      ,c.[EstadoCivil5]
      ,c.[SigladelaEmpresa6]
      ,c.[CodigoSocio7]
      ,c.[PartidaRegistral8]
      ,c.[TipodeDocumento9]
      ,c.[NumerodeDocumento10]
      ,c.[TipodePersona11]
      ,c.[Domicilio12]
      ,c.[RelacionLaboralconlaCooperativa13]
      ,c.[ClasificaciondelDeudor14]
      ,c.[ClasificaciondelDeudorconAlineamiento15]
      ,c.[CodigodeAgencia16]
      ,c.[Monedadelcredito17]
      ,c.[NumerodeCredito18]
      ,c.[TipodeCredito19]
      ,c.[SubTipodeCredito20]
      ,c.[FechadeDesembolso21]
      ,c.[MontodeDesembolso22]
      ,c.[TasadeInteresAnual23]
      ,c.[Saldodecolocacionescreditosdirectos24]
      ,c.[CuentaContable25]
      ,c.[CapitalVigente26]
      ,c.[CapitalReestrucutado27]
      ,c.[CapitalRefinanciado28]
      ,c.[CapitalVencido29]
      ,c.[CapitalenCobranzaJudicial30]
      ,c.[CarteraAtrasada]
      ,c.[CapitalContingente31]
      ,c.[CuentaContableCapitalContingente32]
      ,c.[DiasdeMora33]
      ,c.[SaldosdeGarantiasPreferidas34]
      ,c.[SaldodeGarantiasAutoliquidables35]
      ,c.[ProvisionesRequeridas36]
      ,c.[ProvisionesConstituidas37]
      ,c.[SaldosdeCreditosCastigados38]
      ,c.[CuentaContableCreditoCastigado39]
      ,c.[Rendimiento_Devengado40]
      ,c.[InteresesenSuspenso41]
      ,c.[IngresosDiferidos42]
      ,c.[TipodeProducto43]
      ,c.[NumerodeCuotasProgramadas44]
      ,c.[NumerodeCuotasPagadas45]
      ,c.[Periodicidaddelacuota46]
      ,c.[PeriododeGracia47]
      ,c.[FechadeVencimientoOriguinaldelCredito48]
      ,c.[FechadeVencimientoAnualdelCredito49]
      ,c.[SITUAC]
      ,c.[FEC_SIT]
      ,c.[TIPO_afil]
      ,c.[AMORTIZA]
      ,c.[PROMOTOR]
      ,c.[PLANILLA]
      ,c.[REGIMEN_LABORAL]
      ,c.[ESTADO]
      ,c.[CAMPAÑA]
      ,c.[EMPRESA]
      ,c.[IMPORTE_A_DESCONTAR]
      ,c.[IMPORTE_PAGADO]
      ,c.[Nro]
      ,c.[Reprogramados]
      ,c.[MDesembolsadoxM]
      ,c.[mora]
	  ,c.Origen_Coopac
	  ,c.[Nro_Fincore]
	  ,c.Departamento
	  ,c.Provincia
	  ,c.Distrito
	  ,c.Reprogramados52
	  ,c.Refinanciado
	  , c.[CapitalVencido29]
	  ,c.[Funcionario Originador]
	  ,c.[Funcionario Actual]
	  ,c.[Nombre Negocio]
	  ,c.[Domicilio Negocio]
	  ,c.[Distrito Negocio]
	  ,c.[Dpto Negocio] 
	  ,c.[Provincia Negocio]

  FROM [Anexos_Riesgos2]..[Cabecera] c left join Anexos_Riesgos2..Anx06_preliminar a
   on (C.Nro_Fincore=A.Nro_Fincore AND c.NumerodeCredito18=a.NumerodeCredito18 and c.Monedadelcredito17=a.Monedadelcredito17 and c.FechaCorte1=a.FechaCorte1)
where c.FechaCorte1='20230331' and a.NumerodeCredito18 is null ------SE PONE MES PASADO



UPDATE Anexos_Riesgos2..Anx06_preliminar
SET nuevo_capitalvencido = CapitalVencido29
---			SELECT * FROM Anexos_Riesgos2..Anx06_preliminar
WHERE FechaCorte1 = '20230331'
AND nuevo_capitalvencido is null
-------------EJECUTAR ANTES DEL PROCEDURE DE COSECHA 21/01/2020---------------------------


IF OBJECT_ID('TEMPDB..#BASE1') IS NOT NULL 
DROP TABLE #BASE1
SELECT 
NumerodeCredito18,Monedadelcredito17,
NUEVO_PROMOTOR,Nro_Fincore,ADMINISTRADOR,TipodeProducto43, originador,
--TipodeProducto43,
--TipodeCredito19,
NUEVA_PLANILLA 
INTO #BASE1
FROM Anexos_Riesgos2..Anx06_preliminar WHERE FechaCorte1='20230228' --se pone el de hace 2 meses


/*
este es el código al que más hay que echarle el ojo, porque copia y pega los 
NUEVO_PROMOTOR, NUEVA_PLANILLA, ADMINISTRADOR, del mes pasado, para 'evitar' volver 
a hacer correcciones, el problema es que si está mal, sigue arrastrando errores mes a mes
*/
UPDATE A SET
A.NUEVO_PROMOTOR=B.NUEVO_PROMOTOR,
--A.TipodeProducto43=B.TipodeProducto43,
--A.TipodeCredito19=B.TipodeCredito19,
a.NUEVA_PLANILLA=B.NUEVA_PLANILLA,
A.ADMINISTRADOR=B.ADMINISTRADOR,
a.originador = b.originador
--SELECT A.NumerodeCredito18,A.Monedadelcredito17,A.PROMOTOR,A.NUEVO_PROMOTOR,B.NUEVO_PROMOTOR,a.TipodeProducto43,b.TipodeProducto43 
FROM Anexos_Riesgos2..Anx06_preliminar A 
JOIN #BASE1 B ON (A.Nro_Fincore=B.Nro_Fincore AND A.NumerodeCredito18=B.NumerodeCredito18 AND A.Monedadelcredito17=B.Monedadelcredito17)
WHERE A.FechaCorte1='20230331' --- SE PONE EL MES PASADO


-- verificar y pasarle la voz a Daniel o Enrique de estos casos inconsistentes--
UPDATE A SET
A.TipodeProducto43=34
--					SELECT nro_fincore,NumerodeCredito18,Monedadelcredito17,NRO_FINCORE,[ApellidosyNombresRazonSocial2],PLANILLA,NUEVA_PLANILLA,TipodeProducto43,Tipo_producto,FechadeDesembolso21,Origen_Coopac, promotor
FROM Anexos_Riesgos2..Anx06_preliminar A
WHERE A.FechaCorte1='20230331' AND A.TipodeProducto43=30 AND (A.PLANILLA not LIKE '%LIBRE%'
 or a.NUEVA_PLANILLA not LIKE '%LIBRE%' )

/*tambien verificar esta inconsistencia, tambien pasarle la voz a daniel o Enrique*/
UPDATE A SET
A.TipodeProducto43=30
--					select NumerodeCredito18,ApellidosyNombresRazonSocial2,TipodeProducto43, PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR 
from Anexos_Riesgos2..Anx06_preliminar A
where A.FechaCorte1='20230331'
AND A.PLANILLA LIKE '%libre dis%'
and A.TipodeProducto43 <>30

-------------------------------------------
 --ESTE CÓDIGO ES PARA VERIFICAR UN ERROR QUE HABÍA OCURRIDO
 --select FechaCorte1, ApellidosyNombresRazonSocial2, NumerodeCredito18, TipodeCredito19, FechadeDesembolso21,
 --Tipo_producto, TipodeProducto43, TIPO_afil, PLANILLA, EMPRESA, Situacion_Credito, TIPO, NUEVA_PLANILLA
 --from Anexos_Riesgos2..Anx06_preliminar
 --where Nro_Fincore = '00086604'
 ------------------------------------------
 --AQUI LO ARREGLAMOS
 --UPDATE Anexos_Riesgos2..Anx06_preliminar
 --SET TipodeProducto43 = '16'
 --WHERE NumerodeCredito18 = '00086604'
 --AND TipodeProducto43 = '30' 
 ------------------------------------------

update a
set a.NUEVA_PLANILLA='PEQUEÑA EMPRESA'
--			SELECT NRO_FINCORE, *
from Anexos_Riesgos2..Anx06_preliminar a
where FechaCorte1='20230331'
and TipodeProducto43 in (16,15,17,18,19)
and (PLANILLA not like '%pequeña%'
or NUEVA_PLANILLA not like '%pequeña%'
or NUEVA_PLANILLA not like '%independiente%'
or NUEVA_PLANILLA not like '%cooperativa%')

/*
UPDATE A
SET A.TipodeProducto43=23
--					select NumerodeCredito18,ApellidosyNombresRazonSocial2,MontodeDesembolso22,TipodeProducto43, PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR 
from Anexos_Riesgos2..Anx06_preliminar A
where A.FechaCorte1='20230331'
AND A.PLANILLA LIKE '%MICROEMPRESA%'
AND MontodeDesembolso22>30000
AND NUEVA_PLANILLA NOT LIKE '%PEQUEÑA EMPRESA%'
AND NUEVA_PLANILLA NOT LIKE '%INDEPENDIENTE%'
and( A.TipodeProducto43 <>23 and a.TipodeProducto43<>22 and a.TipodeProducto43<>24 and a.TipodeProducto43<>29 and a.TipodeProducto43<>21 and a.TipodeProducto43 <>25)
*/

UPDATE ccccccccc
SET ccccccccc.TipodeProducto43=30 
--				select NumerodeCredito18,ApellidosyNombresRazonSocial2,TipodeProducto43, PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR 
from Anexos_Riesgos2..Anx06_preliminar as ccccccccc
where ccccccccc.FechaCorte1='20230331'
AND ccccccccc.PLANILLA LIKE '%LIBRE%'
and ccccccccc.TipodeProducto43 <> 30

UPDATE A
SET A.TipodeProducto43=34
--				select NumerodeCredito18,ApellidosyNombresRazonSocial2,TipodeProducto43, PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR,NRO_FINCORE 
from Anexos_Riesgos2..Anx06_preliminar as A
where A.FechaCorte1='20230331'
AND A.PLANILLA NOT LIKE '%GARANTIA%'
and A.TipodeProducto43 =45
AND A.PLANILLA NOT LIKE '%LIBRE%'
AND A.PLANILLA NOT LIKE '%MICROEMPRESA%'

UPDATE A
SET A.TipodeProducto43=23
--					select NumerodeCredito18,ApellidosyNombresRazonSocial2,TipodeProducto43, PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR, MontodeDesembolso22
from Anexos_Riesgos2..Anx06_preliminar as A
where A.FechaCorte1='20230331'
AND A.PLANILLA LIKE '%MICROEMPRESA%'
and A.TipodeProducto43 <>23
and A.TipodeProducto43 <>22
and A.TipodeProducto43 <>24
and A.TipodeProducto43 <>29
and a.TipodeProducto43=36

UPDATE A
SET A.TipodeProducto43=34
--							select FechaCorte1, FechadeDesembolso21,NumerodeCredito18,ApellidosyNombresRazonSocial2,MontodeDesembolso22,TipodeProducto43, PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR , MontodeDesembolso22
from Anexos_Riesgos2..Anx06_preliminar A
where A.FechaCorte1='20230331'
and A.TipodeProducto43  in(21,22,23,24,25,29)
AND A.PLANILLA NOT LIKE '%MICROEMPRESA%'
AND A.PLANILLA NOT LIKE '%PEQUEÑA%'
AND A.PLANILLA NOT LIKE '%LIBRE DIS%'
AND A.PLANILLA NOT LIKE '%GARANTIA%'
AND A.PLANILLA NOT LIKE '%INDEPENDIENTE%'

-- 00079602
-- 00079098
----------------------------------
--select  FechaCorte1, NumerodeCredito18,ApellidosyNombresRazonSocial2,MontodeDesembolso22,TipodeProducto43, PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR , MontodeDesembolso22
--from Anexos_Riesgos2..Anx06_preliminar
--WHERE NumerodeCredito18 = '00079098'

--------------------------------

UPDATE A
SET A.TipodeProducto43=30
--					select NumerodeCredito18,ApellidosyNombresRazonSocial2,TipodeProducto43, PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR 
from Anexos_Riesgos2..Anx06_preliminar A
where A.FechaCorte1='20230331'
AND A.PLANILLA LIKE '%libre%'
and A.TipodeProducto43 IN (34,35,39,36)


UPDATE A
SET A.TipodeProducto43=41
--					select nro_fincore,ApellidosyNombresRazonSocial2,TipodeProducto43, MontodeDesembolso22,PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR 
from Anexos_Riesgos2..Anx06_preliminar A
where A.FechaCorte1='20230331'
AND A.PLANILLA LIKE '%garantia%'
AND A.PLANILLA not LIKE '%GARANTIA CAPITAL S.A.C.%'
and A.TipodeProducto43 IN (34,35,39,36)

update A
set a.TipodeProducto43=41
--					select  nro_fincore,ApellidosyNombresRazonSocial2,TipodeProducto43, PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR
from Anexos_Riesgos2..Anx06_preliminar A
where a.FechaCorte1='20230331'
and a.PLANILLA like '%independiente%'
and a.TipodeProducto43 in (34,35,39,36)
and NUEVA_PLANILLA like '%independ%'

update A
set a.TipodeProducto43=34
--					select  nro_fincore,ApellidosyNombresRazonSocial2,Saldodecolocacionescreditosdirectos24,TipodeProducto43, PLANILLA,NUEVA_PLANILLA, NUEVO_PROMOTOR, PROMOTOR
from Anexos_Riesgos2..Anx06_preliminar A
where a.FechaCorte1='20230331'
and a.PROMOTOR like '%proseva%'
and a.TipodeProducto43 <>34
and a.TipodeProducto43<>35
and a.TipodeProducto43<>39
and a.TipodeProducto43<>30
and a.TipodeProducto43<>36

UPDATE A SET
A.NUEVO_PROMOTOR=A.PROMOTOR
--						SELECT PLANILLA,PROMOTOR,NUEVO_PROMOTOR  
FROM Anexos_Riesgos2..Anx06_preliminar A WHERE A.FechaCorte1='20230331' AND A.NUEVO_PROMOTOR is null
AND A.TipodeProducto43 IN (34,39,35,36) AND PROMOTOR LIKE '%PROSEVA%'


/*aqui entro yo para actualizar los promotores que indico Juan Jose Seminario*/
/*para mi no es necesario pero esta para verificarlo en la sgte carga*/

--UPDATE A SET
--A.NUEVO_PROMOTOR=A.PROMOTOR
----SELECT a.PLANILLA,a.PROMOTOR,a.NUEVO_PROMOTOR,f.promotores  
--FROM Anexos_Riesgos2..Anx06_preliminar A inner JOIN [Anexos_Riesgos]..[planilla2] F 
--ON (A.PLANILLA=F.NUEVA_PLANILLA)
--WHERE A.FechaCorte1='20210630' and a.NUEVO_PROMOTOR is null
--and f.promotores is not NULL 
--AND A.TipodeProducto43 IN (34,39,35) and a.PLANILLA not like '%planilla liquidados%'
--and a.PLANILLA not like '%planilla fallecidos%'
--and a.PROMOTOR not like '%proseva%'


/*
SELECT a.PLANILLA,a.PROMOTOR,a.NUEVO_PROMOTOR,f.promotores  
FROM Anexos_Riesgos2..Anx06_preliminar A inner JOIN [Anexos_Riesgos]..[planilla2] F 
ON (A.PLANILLA=F.NUEVA_PLANILLA)
WHERE A.FechaCorte1='20210630' and a.NUEVO_PROMOTOR is null
and f.promotores is not NULL 
AND A.TipodeProducto43 IN (34,39,35) and a.PLANILLA not like '%planilla liquidados%'
and a.PLANILLA not like '%planilla fallecidos%'
and a.PROMOTOR not like '%proseva%'

*/

UPDATE A SET
A.NUEVO_PROMOTOR=f.funcionario_fox 
--				SELECT a.PLANILLA,a.PROMOTOR,a.NUEVO_PROMOTOR,f.funcionario_fox  
FROM Anexos_Riesgos2..Anx06_preliminar A JOIN [Anexos_Riesgos]..BASE_FUNCIONARIOS F 
ON (A.PROMOTOR=F.Funcionaria_fincore)
WHERE A.FechaCorte1='20230331' AND A.NUEVO_PROMOTOR is null
AND A.TipodeProducto43 IN (34,39,35,36) 


UPDATE A SET
A.NUEVO_PROMOTOR=f.CORRECION_FUNCIONARIOS 
--SELECT a.PLANILLA,a.PROMOTOR,a.NUEVO_PROMOTOR,f.CORRECION_FUNCIONARIOS  
FROM Anexos_Riesgos2..Anx06_preliminar A JOIN [Anexos_Riesgos]..[Funcionarios_nombres_20220331] F 
ON (A.PROMOTOR=F.FUNCIONARIO)
WHERE A.FechaCorte1='20230331' AND A.NUEVO_PROMOTOR is null
AND A.TipodeProducto43 IN (34,39,35,36) 


--select Nro_Fincore, ApellidosyNombresRazonSocial2, NUEVA_PLANILLA
--from Anexos_Riesgos2..Anx06_preliminar
--where FechaCorte1 = '20221031'
--and NUEVA_PLANILLA is null
--and TipodeProducto43 in (15,16,17,18, 19)



UPDATE A SET
A.administrador=f.CORRECION_FUNCIONARIOS 
--SELECT a.PLANILLA,a.PROMOTOR,a.administrador,f.CORRECION_FUNCIONARIOS  
FROM Anexos_Riesgos2..Anx06_preliminar A JOIN [Anexos_Riesgos]..[Funcionarios_nombres_20220331] F 
ON (A.administrador=F.FUNCIONARIO)
WHERE A.FechaCorte1='20230331' 
AND A.NUEVO_PROMOTOR is null
AND A.TipodeProducto43 IN (34,39,35,36) 


UPDATE A SET
A.NUEVO_PROMOTOR=a.PROMOTOR
--SELECT a.PLANILLA,a.PROMOTOR,a.NUEVO_PROMOTOR 
FROM Anexos_Riesgos2..Anx06_preliminar A 
WHERE A.FechaCorte1='20230331' 
AND A.NUEVO_PROMOTOR IS NULL
AND A.TipodeProducto43 IN (34,39,35,36)

update A
set a.NUEVO_PROMOTOR =a.PROMOTOR
--select a.nro_fincore, a.ApellidosyNombresRazonSocial2,a.TipodeProducto43, a.PROMOTOR, a.NUEVO_PROMOTOR,a.planilla, a.nueva_planilla 
from Anexos_Riesgos2..Anx06_preliminar a
where a.FechaCorte1='20230331'
and a.NUEVO_PROMOTOR is null


UPDATE A
SET A.NUEVO_PROMOTOR=f.CORRECION_FUNCIONARIOS 
--SELECT a.PLANILLA,a.PROMOTOR,a.NUEVO_PROMOTOR,f.CORRECION_FUNCIONARIOS  
FROM Anexos_Riesgos2..Anx06_preliminar A JOIN [Anexos_Riesgos]..[Funcionarios_nombres_20220331] F 
ON (A.NUEVO_PROMOTOR=F.FUNCIONARIO)
WHERE A.FechaCorte1='20230331' 


update c set 
c.NUEVA_PLANILLA=C.PLANILLA
--c.planilla=t.planilla
--			select C.FechadeDesembolso21,c.PROMOTOR,c.PLANILLA,C.NUEVO_PROMOTOR,t.NUEVA_PLANILLA,C.PLANILLA,C.Saldodecolocacionescreditosdirectos24
from Anexos_Riesgos2..Anx06_preliminar c 
join #T t on (c.nro_fincore=t.nro_fincore and   c.NumerodeCredito18=t.NumerodeCredito18 and c.Monedadelcredito17=t.Monedadelcredito17)
where c.FechaCorte1='20230331' AND C.NUEVA_PLANILLA IS NULL AND C.TipodeProducto43 IN (34,39,35,36)


update c set 
c.NUEVA_PLANILLA=C.PLANILLA
--select C.FechadeDesembolso21, C.NRO_FINCORE, c.ApellidosyNombresRazonSocial2, c.PROMOTOR,c.TipodeProducto43,C.NUEVO_PROMOTOR,C.Saldodecolocacionescreditosdirectos24 , C.PLANILLA , c.NUEVA_PLANILLA
from Anexos_Riesgos2..Anx06_preliminar c 
where c.FechaCorte1='20230331' AND C.NUEVA_PLANILLA IS NULL

update a
set a.NUEVA_PLANILLA='PEQUEÑA EMPRESA',
a.EMPRESA='PEQUEÑA EMPRESA',
a.PLANILLA='PEQUEÑA EMPRESA'
--select Nro_Fincore,ApellidosyNombresRazonSocial2, MontodeDesembolso22, FechadeDesembolso21, TipodeProducto43, PLANILLA, NUEVA_PLANILLA
from Anexos_Riesgos2..Anx06_preliminar a
where FechaCorte1='20230331'
and PLANILLA is null
and NUEVA_PLANILLA is null
and TipodeProducto43 in (15,16,17,18, 19)



/************************************************SEGUIMOS************************************/
/****VIGENTE A TODO *****/
update c set
c.Situacion_Credito='VIGENTE'
--select c.NUEVO_PROMOTOR,c.PROMOTOR,c.FechadeDesembolso21,c.Situacion_Credito,* 
from Anexos_Riesgos2..Anx06_preliminar c where C.FechaCorte1='20230331' 
--and c.TipodeProducto43 in (34,39) 
and c.Saldodecolocacionescreditosdirectos24>0 

/****VENCIDO****/
update c set
c.Situacion_Credito='VENCIDOS'
--select c.NUEVO_PROMOTOR,c.PROMOTOR,c.FechadeDesembolso21,c.Situacion_Credito,* 
from Anexos_Riesgos2..Anx06_preliminar c where C.FechaCorte1='20230331' 
--and c.TipodeProducto43 in (34,39) 
and c.Saldodecolocacionescreditosdirectos24>0 
AND isnull(c.CapitalVencido29,0)+isnull(c.CapitalenCobranzaJudicial30,0)>0


/***REFINANCIADOS**/
update c set
c.Situacion_Credito='REFINANCIADO'
--select c.NUEVO_PROMOTOR,c.PROMOTOR,c.FechadeDesembolso21,c.Situacion_Credito,* 
from Anexos_Riesgos2..Anx06_preliminar c where C.FechaCorte1='20230331' 
--and c.TipodeProducto43 in (34,39)
 and c.Saldodecolocacionescreditosdirectos24>0 AND isnull(c.CapitalRefinanciado28,0) > 0--ISNULL(C.TIPO_afil,'XX') LIKE '%REF%'

/******JUDICIAL******/
update c set
c.Situacion_Credito='JUDICIAL'
--select c.NUEVO_PROMOTOR,c.PROMOTOR,c.FechadeDesembolso21,c.Situacion_Credito,* 
from Anexos_Riesgos2..Anx06_preliminar c where C.FechaCorte1='20230331' 
--and c.TipodeProducto43 in (34,39)
 and c.Saldodecolocacionescreditosdirectos24>0 AND ISNULL(c.CapitalenCobranzaJudicial30,0) > 0--ISNULL(C.SITUAC,'XX') LIKE '%JU%'

/******CASTIGADO******/
update c set
c.Situacion_Credito='CASTIGADO'
--select c.NUEVO_PROMOTOR,c.PROMOTOR,c.FechadeDesembolso21,c.Situacion_Credito,* 
from Anexos_Riesgos2..Anx06_preliminar c where C.FechaCorte1='20230331' 
--and c.TipodeProducto43 in (34,39)
AND c.Situacion_Credito is null
and c.SaldosdeCreditosCastigados38>0

/**************AHORA EMPEZAMOS CON EL TIPO*************/

UPDATE C set 
c.TIPO=CASE WHEN c.TIPO_afil LIKE '%NUEVO%' THEN 'NVO'
 WHEN c.TIPO_afil LIKE '%AMPLIACION%' THEN 'AMP' END 
--
--select NUEVO_PROMOTOR,PROMOTOR,MontodeDesembolso22,TIPO_afil,NumerodeCredito18,Monedadelcredito17,c.TIPO,
--CASE WHEN c.TIPO_afil LIKE '%NUEVO%' THEN 'NVO'
-- WHEN c.TIPO_afil LIKE '%AMPLIACION%' THEN 'AMP' END 
from Anexos_Riesgos2..Anx06_preliminar c where C.FechaCorte1='20230331' 
--and c.TipodeProducto43 in (34,39) 
--and c.Saldodecolocacionescreditosdirectos24>0 
--and c.Situacion_Credito in ('VIGENTE','VENCIDOS')
--ISNULL(TIPO_afil,'XX') NOT LIKE '%REF%'

/*ACTUALIZAR LA EMPRESA DE ANEXO06 DEL MES*/
update c
set C.EMPRESA=B.Empresa
--select c.Empresa, B.empresa
from Anexos_Riesgos2..Anx06_preliminar C
LEFT JOIN  Anexos_Riesgos..planilla2 B
ON (C.NUEVA_PLANILLA=B.NUEVA_PLANILLA)
where c.FechaCorte1='20230331'
and c.Empresa is null

update a
set a.administrador=a.NUEVO_PROMOTOR
--select*
from Anexos_Riesgos2..Anx06_preliminar a
where FechaCorte1='20230331'
and administrador is null


UPDATE A SET
A.administrador=f.CORRECION_FUNCIONARIOS 
--SELECT a.PLANILLA,a.PROMOTOR,a.administrador,f.CORRECION_FUNCIONARIOS  
FROM Anexos_Riesgos2..Anx06_preliminar A JOIN [Anexos_Riesgos]..[Funcionarios_nombres_20220331] F 
ON (A.administrador=F.FUNCIONARIO)
WHERE A.FechaCorte1 ='20230331' 
AND A.NUEVO_PROMOTOR is null

--SELECT * FROM [Anexos_Riesgos]..[Funcionarios_nombres_20220331]

/*****FIN DE PROCESO*********/

--cosas raras que algún día debería preguntar, ya ni recuerdo qué tenían de raras
select Nro_Fincore, TipodeProducto43,PLANILLA, ApellidosyNombresRazonSocial2, empresa
 from Anexos_Riesgos2..Anx06_preliminar
--where  NUEVA_PLANILLA IS NULL
where FechaCorte1 = '20230331'
and planilla like '%independ%'
and TipodeProducto43 in (22,23,24,25)
/*
00005496 raraso
00079602 bien
00079098 bien
00001463 bien
*/

--select nro_fincore, ApellidosyNombresRazonSocial2, MontodeDesembolso22, TipodeProducto43,PLANILLA,  FechadeDesembolso21, FechaCorte1
--from Anexos_Riesgos2..Anx06_preliminar
--where Nro_Fincore = '00079098'
--order by FechaCorte1

--select * from Anexos_Riesgos2..Anx06_preliminar
--where administrador is null
--and FechaCorte1 = '20220930'

update Anexos_Riesgos2..Anx06_preliminar set
administrador = 'OFICINA CAÑETE',
nuevo_promotor = 'OFICINA CAÑETE'
FROM Anexos_Riesgos2..Anx06_preliminar
WHERE FECHACORTE1 = '20230331'
AND ADMINISTRADOR LIKE '%CAÑETE%'

------------------------------------------------------------------------------------
---------------------CODIGO PARA ARREGLAR A PROSEVA CAÑETE Y PONERLA COMO OFICINA CAÑETE
UPDATE A
SET A.administrador = 'OFICINA CAÑETE',
A.NUEVO_PROMOTOR = 'OFICINA CAÑETE'
FROM Anexos_Riesgos2..Anx06_preliminar AS  A -- AQUÍ VA LA TABLA
WHERE FechaCorte1 = '20230331'
AND ADMINISTRADOR LIKE '%CAÑETE%'

--------------------------------------------------------------------------------------

--buscando columnas en las que el administrador está vacío por razones misteriosas
select *,Nro_Fincore,TipodeProducto43,PROMOTOR,NUEVO_PROMOTOR,administrador 
from Anexos_Riesgos2..Anx06_preliminar 
where FechaCorte1 = '20230331'
and administrador is null

--aqui relleno ese espacio duplicando lo que hay en nuevo promotor
UPDATE A
SET a.administrador = a.nuevo_promotor
from Anexos_Riesgos2..Anx06_preliminar a
where a.administrador is null
and FechaCorte1 = '20230331'

-----------------------------------------------------------------------------------
--codigo para añadir más originadores en caso de null
---CREANDO TABLA TEMPORAL Y AÑADIENDO EL ORIGINADOR DEL MES PASADO
--ESTO YA NO HACE FALTA
/*
if OBJECT_ID('TEMPDB..#TEMP_ORIGINADOR')IS NOT NULL 
DROP TABLE #TEMP_ORIGINADOR
SELECT Nro_Fincore, Originador, min(a.FechaCorte1) as 'fecha corte' 
FROM Anexos_Riesgos2..Anx06_preliminar as a
WHERE originador is not null
AND a.FechaCorte1 = '20230331' ----------------------AQUI SE PONE EL DE HACE 2 MESES
group by Nro_Fincore, originador

UPDATE A
SET A.ORIGINADOR = B.ORIGINADOR,
	A.ADMINISTRADOR = B.ADMINISTRADOR
FROM  Anexos_Riesgos2..Anx06_preliminar AS A
JOIN TEMPDB..#TEMP_ORIGINADOR AS B
ON (A.NRO_FINCORE = B.NRO_FINCORE)
WHERE A.FECHACORTE1  = '20230331'
*/
-----------------------------------------------------------------------------------

---------------------------------------------------------
---hora de llenar espacios en blanco en PLANILLA, NUEVA_PLANILLA, EMPRESA
select empresa, planilla, NUEVA_PLANILLA,TipodeProducto43,MontodeDesembolso22,* from Anexos_Riesgos2..Anx06_preliminar
where FechaCorte1 = '20230331'
and (planilla is null
or NUEVA_PLANILLA is null
or empresa is null)
---------------------------------------------------------------------------MICRO
UPDATE Anexos_Riesgos2..Anx06_preliminar
SET EMPRESA = 'MICROEMPRESA'
where EMPRESA IS NULL
AND TipodeProducto43 IN (21,22,23,24,25,29)
UPDATE Anexos_Riesgos2..Anx06_preliminar
SET PLANILLA = 'MICROEMPRESA'
where PLANILLA IS NULL
AND TipodeProducto43 IN (21,22,23,24,25,29)
UPDATE Anexos_Riesgos2..Anx06_preliminar
SET NUEVA_PLANILLA = 'MICROEMPRESA'
where NUEVA_PLANILLA IS NULL
AND TipodeProducto43 IN (21,22,23,24,25,29)
--------------------------------------------------------------------------PEQUEÑA
UPDATE Anexos_Riesgos2..Anx06_preliminar
SET EMPRESA = 'PEQUEÑA EMPRESA'
where EMPRESA IS NULL
AND TipodeProducto43 IN (15,16,17,18,19)
UPDATE Anexos_Riesgos2..Anx06_preliminar
SET PLANILLA = 'PEQUEÑA EMPRESA'
where PLANILLA IS NULL
AND TipodeProducto43 IN (15,16,17,18,19)
UPDATE Anexos_Riesgos2..Anx06_preliminar
SET NUEVA_PLANILLA = 'PEQUEÑA EMPRESA'
where NUEVA_PLANILLA IS NULL
AND TipodeProducto43 IN (15,16,17,18,19)
--------------------------------------------------------------------------MEDIANA
UPDATE Anexos_Riesgos2..Anx06_preliminar
SET EMPRESA = 'MEDIANA EMPRESA'
where EMPRESA IS NULL
AND TipodeProducto43 IN (95,96,97,98,99)
UPDATE Anexos_Riesgos2..Anx06_preliminar
SET PLANILLA = 'MEDIANA EMPRESA'
where PLANILLA IS NULL
AND TipodeProducto43 IN (95,96,97,98,99)
UPDATE Anexos_Riesgos2..Anx06_preliminar
SET NUEVA_PLANILLA = 'MEDIANA EMPRESA'
where NUEVA_PLANILLA IS NULL
AND TipodeProducto43 IN (95,96,97,98,99)

----------------------------------------------------------------------------------
----para unificar los nombres de los funcionarios::::
update anexos_riesgos2..Anx06_preliminar
set originador = 'ALICIA OVIEDO'
where originador like '%ALICIA OVIEDO VELASQUEZ%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'ANDREA BILBAO'
where originador like '%ANDREA BILBAO BRICEÑO%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'EVELYN LOJA'
where originador like '%EVELYN LOJA PINEDO%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'FIGARI VEGA'
where originador like '%FIGARI VEGA AYQUIPA%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'GIOVANNA HERRERA'
where originador like '%GIOVANNA HERRERA MATHEWS%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'GUSTAVO PALLETE'
where originador like '%GUSTAVO PALLETE ALFERANO%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'JERSON ALVA'
where originador like '%JERSON ALVA FARFAN%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'JIMN MENDOZA'
where originador like '%JIMN MENDOZA%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'JONATHAN ESTRADA'
where originador like '%JONATHAN ESTRADA%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'JOSE SANCHEZ'
where originador like '%JOSE SANCHEZ FLORES%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'KATHERIN RAMOS'
where originador like '%KATHERIN RAMOS CCAMA%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'LUIS BUSTAMANTE'
where originador like '%LUIS ALBERTO BUSTAMANTE GONZALES%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'MARGIORY ELIAS'
where originador like '%MARGIORY ELIAS BENAVIDES%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'MILTON JUAREZ'
where originador like '%MILTON MERLYN JUAREZ HORNA%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'ROSA MALDONADO'
where originador like '%ROSA MALDONADO FIGUREOA%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'ROXANA QUISPE'
where originador like '%ROXANA QUISPE CHAVEZ%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'JULY OLGA'
where originador like '%JULY GARCIA ALCANTARA%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'JULY OLGA'
where originador like '%JULY GARCIA%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'OFICINA CAÑETE'
where originador like '%CAÑETE%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'MARIBEL PUCHO'
where originador like '%MARIBEL PUCHO%'

update anexos_riesgos2..Anx06_preliminar
set administrador = 'MARIBEL PUCHO'
where administrador like '%MARIBEL PUCHO%'

update anexos_riesgos2..Anx06_preliminar
set originador = 'JHONY SALDAÑA'
where originador like '%JONY SALDAÑA%'

update anexos_riesgos2..Anx06_preliminar
set administrador = 'JHONY SALDAÑA'
where administrador like '%JONY SALDAÑA%'
