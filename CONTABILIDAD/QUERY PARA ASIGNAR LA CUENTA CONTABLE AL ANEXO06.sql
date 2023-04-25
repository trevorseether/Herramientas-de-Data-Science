

--[Capital Vigente 26/]	[Capital Refinanciado 28/]	[Capital Vencido 29/]	[Capital en Cobranza Judicial 30/]

select *,

----solessss -----vigente
case 
	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '08' and ([Capital Vigente 26/] > [Capital Refinanciado 28/] 
										and [Capital Vigente 26/] > [Capital Vencido 29/]
										and [Capital Vigente 26/] > [Capital en Cobranza Judicial 30/])

	then '1411120600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '09' and ([Capital Vigente 26/] > [Capital Refinanciado 28/] 
										and [Capital Vigente 26/] > [Capital Vencido 29/]
										and [Capital Vigente 26/] > [Capital en Cobranza Judicial 30/])

	then '1411130600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '10' and ([Capital Vigente 26/] > [Capital Refinanciado 28/] 
										and [Capital Vigente 26/] > [Capital Vencido 29/]
										and [Capital Vigente 26/] > [Capital en Cobranza Judicial 30/])

	then '1411020600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '12' and ([Capital Vigente 26/] > [Capital Refinanciado 28/] 
										and [Capital Vigente 26/] > [Capital Vencido 29/]
										and [Capital Vigente 26/] > [Capital en Cobranza Judicial 30/])

	then '1411030604' 


	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '13' and ([Capital Vigente 26/] > [Capital Refinanciado 28/] 
										and [Capital Vigente 26/] > [Capital Vencido 29/]
										and [Capital Vigente 26/] > [Capital en Cobranza Judicial 30/])

	then '1411040601' 


----solessss -----refinanciado

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '08' and ([Capital Refinanciado 28/] >  [Capital Vigente 26/]
										and [Capital Refinanciado 28/] > [Capital Vencido 29/]
										and [Capital Refinanciado 28/] > [Capital en Cobranza Judicial 30/])

	then '1414120600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '09' and ([Capital Refinanciado 28/] >  [Capital Vigente 26/]
										and [Capital Refinanciado 28/] > [Capital Vencido 29/]
										and [Capital Refinanciado 28/] > [Capital en Cobranza Judicial 30/])

	then '1414130600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '10' and ([Capital Refinanciado 28/] >  [Capital Vigente 26/]
										and [Capital Refinanciado 28/] > [Capital Vencido 29/]
										and [Capital Refinanciado 28/] > [Capital en Cobranza Judicial 30/])

	then '1414020600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '12' and ([Capital Refinanciado 28/] >  [Capital Vigente 26/]
										and [Capital Refinanciado 28/] > [Capital Vencido 29/]
										and [Capital Refinanciado 28/] > [Capital en Cobranza Judicial 30/])

	then '1414030604' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '13' and ([Capital Refinanciado 28/] >  [Capital Vigente 26/]
										and [Capital Refinanciado 28/] > [Capital Vencido 29/]
										and [Capital Refinanciado 28/] > [Capital en Cobranza Judicial 30/])

	then '1414040601' 

----solessss -----VENCIDO

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '08' and ([Capital Vencido 29/] >  [Capital Vigente 26/]
										and [Capital Vencido 29/] > [Capital Refinanciado 28/]
										and [Capital Vencido 29/] > [Capital en Cobranza Judicial 30/])

	then '1415120600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '09' and ([Capital Vencido 29/] >  [Capital Vigente 26/]
										and [Capital Vencido 29/] > [Capital Refinanciado 28/]
										and [Capital Vencido 29/] > [Capital en Cobranza Judicial 30/])

	then '1415130600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '10' and ([Capital Vencido 29/] >  [Capital Vigente 26/]
										and [Capital Vencido 29/] > [Capital Refinanciado 28/]
										and [Capital Vencido 29/] > [Capital en Cobranza Judicial 30/])

	then '1415020600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '12' and ([Capital Vencido 29/] >  [Capital Vigente 26/]
										and [Capital Vencido 29/] > [Capital Refinanciado 28/]
										and [Capital Vencido 29/] > [Capital en Cobranza Judicial 30/])

	then '1415030604' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '13' and ([Capital Vencido 29/] >  [Capital Vigente 26/]
										and [Capital Vencido 29/] > [Capital Refinanciado 28/]
										and [Capital Vencido 29/] > [Capital en Cobranza Judicial 30/])

	then '1415040601' 

----solessss -----COBRANZA JUDICIAL

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '08' and ([Capital en Cobranza Judicial 30/] >  [Capital Vigente 26/]
										and [Capital en Cobranza Judicial 30/] > [Capital Refinanciado 28/]
										and [Capital en Cobranza Judicial 30/] > [Capital Vencido 29/])

	then '1416120600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '09' and ([Capital en Cobranza Judicial 30/] >  [Capital Vigente 26/]
										and [Capital en Cobranza Judicial 30/] > [Capital Refinanciado 28/]
										and [Capital en Cobranza Judicial 30/] > [Capital Vencido 29/])

	then '1416130600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '10' and ([Capital en Cobranza Judicial 30/] >  [Capital Vigente 26/]
										and [Capital en Cobranza Judicial 30/] > [Capital Refinanciado 28/]
										and [Capital en Cobranza Judicial 30/] > [Capital Vencido 29/])

	then '1416020600' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '12' and ([Capital en Cobranza Judicial 30/] >  [Capital Vigente 26/]
										and [Capital en Cobranza Judicial 30/] > [Capital Refinanciado 28/]
										and [Capital en Cobranza Judicial 30/] > [Capital Vencido 29/])

	then '1416030604' 

	when [Moneda del crédito 17/] = '01' 
	and [Tipo de Crédito 19/] = '13' and ([Capital en Cobranza Judicial 30/] >  [Capital Vigente 26/]
										and [Capital en Cobranza Judicial 30/] > [Capital Refinanciado 28/]
										and [Capital en Cobranza Judicial 30/] > [Capital Vencido 29/])

	then '1416040601' 
--------------------------------------------------------
--------------------------------------------------------
-----DOLARES -------- CAPITAL VIGENTE
	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '08' and ([Capital Vigente 26/] > [Capital Refinanciado 28/] 
										and [Capital Vigente 26/] > [Capital Vencido 29/]
										and [Capital Vigente 26/] > [Capital en Cobranza Judicial 30/])

	then '1421120600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '09' and ([Capital Vigente 26/] > [Capital Refinanciado 28/] 
										and [Capital Vigente 26/] > [Capital Vencido 29/]
										and [Capital Vigente 26/] > [Capital en Cobranza Judicial 30/])

	then '1421130600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '10' and ([Capital Vigente 26/] > [Capital Refinanciado 28/] 
										and [Capital Vigente 26/] > [Capital Vencido 29/]
										and [Capital Vigente 26/] > [Capital en Cobranza Judicial 30/])

	then '1421020600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '12' and ([Capital Vigente 26/] > [Capital Refinanciado 28/] 
										and [Capital Vigente 26/] > [Capital Vencido 29/]
										and [Capital Vigente 26/] > [Capital en Cobranza Judicial 30/])

	then '1421030604' 


	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '13' and ([Capital Vigente 26/] > [Capital Refinanciado 28/] 
										and [Capital Vigente 26/] > [Capital Vencido 29/]
										and [Capital Vigente 26/] > [Capital en Cobranza Judicial 30/])

	then '1421040601' 


----DOLARES-----refinanciado

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '08' and ([Capital Refinanciado 28/] >  [Capital Vigente 26/]
										and [Capital Refinanciado 28/] > [Capital Vencido 29/]
										and [Capital Refinanciado 28/] > [Capital en Cobranza Judicial 30/])

	then '1424120600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '09' and ([Capital Refinanciado 28/] >  [Capital Vigente 26/]
										and [Capital Refinanciado 28/] > [Capital Vencido 29/]
										and [Capital Refinanciado 28/] > [Capital en Cobranza Judicial 30/])

	then '1424130600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '10' and ([Capital Refinanciado 28/] >  [Capital Vigente 26/]
										and [Capital Refinanciado 28/] > [Capital Vencido 29/]
										and [Capital Refinanciado 28/] > [Capital en Cobranza Judicial 30/])

	then '1424020600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '12' and ([Capital Refinanciado 28/] >  [Capital Vigente 26/]
										and [Capital Refinanciado 28/] > [Capital Vencido 29/]
										and [Capital Refinanciado 28/] > [Capital en Cobranza Judicial 30/])

	then '1424030604' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '13' and ([Capital Refinanciado 28/] >  [Capital Vigente 26/]
										and [Capital Refinanciado 28/] > [Capital Vencido 29/]
										and [Capital Refinanciado 28/] > [Capital en Cobranza Judicial 30/])

	then '1424040601' 

----DOLARES -----VENCIDO

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '08' and ([Capital Vencido 29/] >  [Capital Vigente 26/]
										and [Capital Vencido 29/] > [Capital Refinanciado 28/]
										and [Capital Vencido 29/] > [Capital en Cobranza Judicial 30/])

	then '1425120600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '09' and ([Capital Vencido 29/] >  [Capital Vigente 26/]
										and [Capital Vencido 29/] > [Capital Refinanciado 28/]
										and [Capital Vencido 29/] > [Capital en Cobranza Judicial 30/])

	then '1425130600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '10' and ([Capital Vencido 29/] >  [Capital Vigente 26/]
										and [Capital Vencido 29/] > [Capital Refinanciado 28/]
										and [Capital Vencido 29/] > [Capital en Cobranza Judicial 30/])

	then '1425020600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '12' and ([Capital Vencido 29/] >  [Capital Vigente 26/]
										and [Capital Vencido 29/] > [Capital Refinanciado 28/]
										and [Capital Vencido 29/] > [Capital en Cobranza Judicial 30/])

	then '1425030604' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '13' and ([Capital Vencido 29/] >  [Capital Vigente 26/]
										and [Capital Vencido 29/] > [Capital Refinanciado 28/]
										and [Capital Vencido 29/] > [Capital en Cobranza Judicial 30/])

	then '1425040601' 

----DOLARES -----COBRANZA JUDICIAL

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '08' and ([Capital en Cobranza Judicial 30/] >  [Capital Vigente 26/]
										and [Capital en Cobranza Judicial 30/] > [Capital Refinanciado 28/]
										and [Capital en Cobranza Judicial 30/] > [Capital Vencido 29/])

	then '1426120600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '09' and ([Capital en Cobranza Judicial 30/] >  [Capital Vigente 26/]
										and [Capital en Cobranza Judicial 30/] > [Capital Refinanciado 28/]
										and [Capital en Cobranza Judicial 30/] > [Capital Vencido 29/])

	then '1426130600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '10' and ([Capital en Cobranza Judicial 30/] >  [Capital Vigente 26/]
										and [Capital en Cobranza Judicial 30/] > [Capital Refinanciado 28/]
										and [Capital en Cobranza Judicial 30/] > [Capital Vencido 29/])

	then '1426020600' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '12' and ([Capital en Cobranza Judicial 30/] >  [Capital Vigente 26/]
										and [Capital en Cobranza Judicial 30/] > [Capital Refinanciado 28/]
										and [Capital en Cobranza Judicial 30/] > [Capital Vencido 29/])

	then '1426030604' 

	when [Moneda del crédito 17/] = '02' 
	and [Tipo de Crédito 19/] = '13' and ([Capital en Cobranza Judicial 30/] >  [Capital Vigente 26/]
										and [Capital en Cobranza Judicial 30/] > [Capital Refinanciado 28/]
										and [Capital en Cobranza Judicial 30/] > [Capital Vencido 29/])

	then '1426040601' 
ELSE ''
end as 'CUENTA CONTABLE ELABORADA'

from contabilidad..ene2023_v2
--where [Registro 1/] is not null
--and [Apellidos y Nombres / Razón Social 2/] is not null
--and [Nro Prestamo _Fincore] = 00088186
order by [Registro 1/]

-----utilizar este código para verificar si han subido bien los datos
select * from contabilidad..ene2023_v2
where [Capital Vigente 26/] is null
or [Capital en Cobranza Judicial 30/] is null
or [Capital Refinanciado 28/] is null
or [Capital Vencido 29/] is null
or [Moneda del crédito 17/] is null
or [Tipo de Crédito 19/] is null

/*
update contabilidad..ene2023_v2
set [Capital Vigente 26/] = 5410.02
---				select * from contabilidad..ene2023_v2
where [Registro 1/] = 4051
and [Apellidos y Nombres / Razón Social 2/] like '%cisneros escobedo%'
*/
