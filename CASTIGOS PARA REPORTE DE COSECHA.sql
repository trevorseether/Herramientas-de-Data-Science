




----------codigo para hacer lo que quiere ENRIQUE CUANDO HAY CASTIGADOS
update a
set a.MCastigadoxM = ISNULL(b.MCastigadoxM,0)+ ISNULL(b.SaldosdeCreditosCastigados38,0)

-----------------                       select * 
from experimentos..copiapruebajuanjose a
join Comercial..anx06 b on (a.Nro_Fincore = b.Nro_Fincore and year(a.FechaCorte1) = year(b.FechadeDesembolso21) and month(a.FechaCorte1) = month(b.FechadeDesembolso21))
where b.FechaCorte1 = '20221031'
and b.SaldosdeCreditosCastigados38 is not null
and b.SaldosdeCreditosCastigados38 >0

UPDATE experimentos..copiapruebajuanjose
SET MCastigadoxM = 0
WHERE  MCastigadoxM IS NULL


---TABLITA DE CASTIGADOS QUE ESTÁ EN EL REPORTE DE COSECHA
select ( DateName(year,FechadeDesembolso21)+ ' ' +DateName(month,FechadeDesembolso21)),sum(mcastigadoxm) from Comercial..anx06 
group by ( DateName(year,FechadeDesembolso21)+ ' ' +DateName(month,FechadeDesembolso21))
order by ( DateName(year,FechadeDesembolso21)+ ' ' +DateName(month,FechadeDesembolso21))

select ( DateName(year,FechadeDesembolso21)+ ' ' +DateName(month,FechadeDesembolso21)), sum(mcastigadoxm) from comercial..anx06
group by ( DateName(year,FechadeDesembolso21)+ ' ' +DateName(month,FechadeDesembolso21))
order by  ( DateName(year,FechadeDesembolso21)+ ' ' +DateName(month,FechadeDesembolso21))
-------------CODIGO PARA REHACER LA TABLA DEL ANEXO 06 SI ES QUE SALE MAL
--drop table experimentos..copiapruebajuanjose
--select * into experimentos..copiapruebajuanjose
--from Comercial..anx06
