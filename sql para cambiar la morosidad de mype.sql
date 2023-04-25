--ESTO ELIMINA TODO DE TODA LA COLUMNA nuevo_capitalvencido
--si la friegas con esto creas la tabla de nuevo

--drop table [experimentos].[dbo].[copiaAnex062]
----SELECT * FROM [experimentos].[dbo].[copiaAnex062]
--select * 
--into [experimentos].[dbo].[copiaAnex062]
--from Comercial..anx06
-----------------------------------------------------------------------------------------------
--select * from [experimentos].[dbo].[copiaAnex062]
--where CapitalenCobranzaJudicial30 >0
--and nuevo_capitalvencido > 0
------------------------------comprobación de este caso----------------------------------------
--select FechaCorte1,
--ApellidosyNombresRazonSocial2,
--MontodeDesembolso22,
--Saldodecolocacionescreditosdirectos24,
--CapitalRefinanciado28,
--CapitalenCobranzaJudicial30,
--CapitalVigente26,
--CapitalVencido29,
--CarteraAtrasada,
--DiasdeMora33,
--TipodeProducto43,
--Nro_Fincore,
--nuevo_capitalvencido from [experimentos].[dbo].[copiaAnex062]
----WHERE nuevo_capitalvencido IS NULL
--where nro_fincore = '00081920'
-----------------------------------------------------------------------------------------------
--pensé que este código estaba bien pero en realidad no porque no toma en cuenta los ceros que he colocado :/
--update [experimentos].[dbo].[copiaAnex062]
--set nuevo_capitalvencido = NULL

--DECLARE @fechacortada as datetime
--set @fechacortada = '20220930'
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
--COLOCANDO EL 100% DEL SALDO DE COLOCACIÓN DENTRO DEL CAPITAL VENCIDO POR TENER MÁS DE 30 DÍAS DE RETRASO
--PARA MICRO Y PEQUEÑA EMPRESA
--
--select *, nuevo_capitalvencido, CapitalVencido29 from  Comercial..Anx06
--update [experimentos].[dbo].[copiapruebajuanjose]
--set nuevo_capitalvencido = CapitalVencido29
--where fechacorte1 = '20220930'



--
update a
set a.nuevo_capitalvencido = b.Saldodecolocacionescreditosdirectos24
--and set CapitalVigente26 = 0
from [experimentos].[dbo].[copiaAnex062] as a
join [experimentos].[dbo].[copiaAnex062] as b
on  ((a.nro_fincore = b.nro_fincore and a.FechaCorte1 = b.FechaCorte1) 
or (a.ApellidosyNombresRazonSocial2 = b.ApellidosyNombresRazonSocial2 
and a.FechaCorte1 = b.FechaCorte1 
and a.NumerodeCredito18 = b.NumerodeCredito18)
)
-- and a.FechaCorte1 = b.FechaCorte1)
where a.TipodeProducto43 in (21,22,23,24,25,29,15,16,17,18,19)
and a.DiasdeMora33 > 30
AND a.nuevo_capitalvencido is NULL
--
------------ESTE CÓDIGO ES PARA COMPROBAR QUIENES SON LOS AFECTADOS------------
--select FechaCorte1,
--ApellidosyNombresRazonSocial2,
--MontodeDesembolso22,
--Saldodecolocacionescreditosdirectos24,
--CapitalRefinanciado28,
--CapitalenCobranzaJudicial30,
--CapitalVigente26,
--CapitalVencido29,
--CarteraAtrasada,
--DiasdeMora33,
--TipodeProducto43,
--Nro_Fincore,
--nuevo_capitalvencido
-- from [experimentos].[dbo].[copiaAnex062]
--where TipodeProducto43 in (21,22,23,24,25,29,15,16,17,18,19)
--and DiasdeMora33 > 30
----and nuevo_capitalvencido Is NULL
--order by Nro_Fincore
--
--and a.FechaCorte1 = b.FechaCorte1 --importante para que la asignación sea del más antiguo

--and a.FechaCorte1 = '20220930'
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
--COLOCANDO CEROS EN: Capital Vigente 26/, Capital Reestrucutado 27/, Capital Refinanciado 28/
--PARA MICRO Y PEQUEÑA EMPRESA
update [experimentos].[dbo].[copiaAnex062]
SET CapitalVigente26 = 0, CapitalRefinanciado28 = 0
where TipodeProducto43 in (21,22,23,24,25,29,15,16,17,18,19)
and DiasdeMora33 > 30
AND nuevo_capitalvencido IS NOT NULL
and CapitalenCobranzaJudicial30 = 0

------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
--COLOCANDO EL 100% DEL SALDO DE COLOCACIÓN DENTRO DEL CAPITAL VENCIDO POR TENER MÁS DE 30 DÍAS DE RETRASO
--PARA MEDIANA EMPRESA
update a
set a.nuevo_capitalvencido = (b.Saldodecolocacionescreditosdirectos24)
--and set CapitalVigente26 = 0

from [experimentos].[dbo].[copiaAnex062] a
join [experimentos].[dbo].[copiaAnex062]  b
on  ((a.nro_fincore = b.nro_fincore and a.FechaCorte1 = b.FechaCorte1) 
or (a.ApellidosyNombresRazonSocial2 = b.ApellidosyNombresRazonSocial2 
and a.FechaCorte1 = b.FechaCorte1 
and a.NumerodeCredito18 = b.NumerodeCredito18)
)
where a.TipodeProducto43 in (95,96,97,98,99)
and a.DiasdeMora33 > 15
AND a.nuevo_capitalvencido IS NULL
and a.FechaCorte1 = b.FechaCorte1 --importante para que la asignación sea del más antiguo

------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
--COLOCANDO CEROS EN: Capital Vigente 26/, Capital Reestrucutado 27/, Capital Refinanciado 28/
--PARA MEDIANA EMPRESA
update [experimentos].[dbo].[copiaAnex062]
SET CapitalVigente26 = 0, CapitalReestrucutado27 = 0, CapitalRefinanciado28 = 0
where TipodeProducto43 in (95,96,97,98,99)
and DiasdeMora33 > 15
AND nuevo_capitalvencido IS NULL

------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
--rellenando los espacios faltantes con el antiguo capital vencido
update a
set a.nuevo_capitalvencido = b.CapitalVencido29
--and set CapitalVigente26 = 0

from [experimentos].[dbo].[copiaAnex062] a
join [experimentos].[dbo].[copiaAnex062] b
on  ((a.nro_fincore = b.nro_fincore and a.FechaCorte1 = b.FechaCorte1) 
or (a.ApellidosyNombresRazonSocial2 = b.ApellidosyNombresRazonSocial2 
and a.FechaCorte1 = b.FechaCorte1 
and a.NumerodeCredito18 = b.NumerodeCredito18)
)
where a.nuevo_capitalvencido IS NULL
--and a.FechaCorte1 = b.FechaCorte1 --importante para que la asignación sea del más reciente

------------------------------------------------------------------------------------
update a
set a.nuevo_capitalvencido = b.CapitalVencido29
--and set CapitalVigente26 = 0

from [experimentos].[dbo].[copiaAnex062] a WITH (NOLOCK)
join [experimentos].[dbo].[copiaAnex062] b WITH (NOLOCK)
on  (a.nro_fincore = b.nro_fincore and a.FechaCorte1 = b.FechaCorte1)
where a.nuevo_capitalvencido IS NULL
go
update a
set a.nuevo_capitalvencido = b.CapitalVencido29
--and set CapitalVigente26 = 0

from [experimentos].[dbo].[copiaAnex062] a WITH (NOLOCK)
join [experimentos].[dbo].[copiaAnex062] b WITH (NOLOCK)
on  (a.ApellidosyNombresRazonSocial2 = b.ApellidosyNombresRazonSocial2 
and a.FechaCorte1 = b.FechaCorte1 
and a.NumerodeCredito18 = b.NumerodeCredito18)
where a.nuevo_capitalvencido IS NULL
-----------------------------------------------------------------------------------

select *,CapitalVencido29, nuevo_capitalvencido, CarteraAtrasada, Nueva_CarAtra  from [experimentos].[dbo].[copiaAnex062] where FechaCorte1 = '20220930'


--SELECT * FROM Comercial..Anx06 WITH (NOLOCK)

--select * from [experimentos].[dbo].[copiaAnex062]
--where nuevo_capitalvencido > 0
--and CapitalVigente26 > 0 


--select * from Comercial..Transicion
--order by Fechacorte1
