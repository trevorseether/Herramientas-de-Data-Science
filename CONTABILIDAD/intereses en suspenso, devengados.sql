declare @fecha as datetime
set @fecha = '20221231'
select
 [Registro 1/],
[Capital Vigente 26/]*((power(1+([Tasa Diaria]/100),[DH vs CS]))-1) as 'rendimiento devengado en sql',
datediff(d,[Fecha Venc de Ult Cuota Cancelada_Contabilidad], @fecha) as 'dias',
--as 'intereses en suspenso en sql'
[Capital Vencido 29/]*((power(1+([Tasa Diaria]/100),datediff(d,[Fecha Venc de Ult Cuota Cancelada_Contabilidad], @fecha)))-1) as 'interesese en suspenso'

from contabilidad..anx06_dic2022_contabilidad
order by [Registro 1/]
GO



--------------

declare @fecha as datetime
set @fecha = '20221231';

WITH cte AS (
  SELECT 
    [Registro 1/],
    [Capital Vigente 26/],
    [Tasa Diaria],
    [DH vs CS],
    [Fecha Venc de Ult Cuota Cancelada_Contabilidad],
    [Capital Vencido 29/]
  FROM contabilidad..anx06_dic2022_contabilidad
)
SELECT 
  cte.*,
  cte.[Capital Vigente 26/] * ((POWER(1 + (cte.[Tasa Diaria] / 100), cte.[DH vs CS])) - 1) AS 'rendimiento devengado en sql',
  DATEDIFF(day, cte.[Fecha Venc de Ult Cuota Cancelada_Contabilidad], '20221231') AS 'dias',
  cte.[Capital Vencido 29/] * ((POWER(1 + (cte.[Tasa Diaria] / 100), DATEDIFF(day, cte.[Fecha Venc de Ult Cuota Cancelada_Contabilidad], '20221231'))) - 1) AS 'intereses en suspenso'
FROM cte
ORDER BY cte.[Registro 1/]

