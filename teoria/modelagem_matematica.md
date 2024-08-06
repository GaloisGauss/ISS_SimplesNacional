# Modelagem Matemática da Alíquota do ISS no Simples Nacional

## Receita Bruta Acumulada

Definimos RBT12 como a receita bruta acumulada nos 12 meses anteriores ao período de apuração:

\[ RBT12 = \sum_{i=1}^{12} R_i \]

onde \( R_i \) é a receita bruta mensal no mês \( i \).

## Alíquota Nominal

A alíquota nominal (\( \tau_{nom} \)) é determinada pela receita bruta acumulada (RBT12) e é dada por uma função \( f \):

\[ f(RBT12) = \tau_{nom} \]

## Alíquota Efetiva

A alíquota efetiva (\( \tau_{efetiva} \)) é calculada a partir da alíquota nominal ajustada pela parcela a deduzir (PD):

\[ \tau_{efetiva} = \frac{(RBT12 \times \tau_{nom}) - PD}{RBT12} \]

## Percentual Efetivo de Repartição

Os percentuais efetivos de cada tributo (\( p_{tributo} \)) são derivados da alíquota efetiva (\( \tau_{efetiva} \)) multiplicada pelo percentual de repartição específico de cada tributo (\( k_{tributo} \)):

\[ p_{tributo} = \tau_{efetiva} \times k_{tributo} \]

## Limitação do Percentual Destinado ao ISS

O percentual efetivo máximo destinado ao ISS é de 5%. Se o valor calculado exceder este limite, a diferença será transferida proporcionalmente aos tributos federais:

\[ p_{ISS} = \min(5\%, \tau_{efetiva} \times k_{ISS}) \]

Se \( p_{ISS} < \tau_{efetiva} \times k_{ISS} \):

\[ \Delta = (\tau_{efetiva} \times k_{ISS}) - 5\% \]

\[ p_{tributos federais} += \Delta \]

## Correção de Diferenças Centesimais

Eventual diferença centesimal entre o total dos percentuais e a alíquota efetiva será transferida para o tributo com maior percentual de repartição:

Se \( \sum p_{tributo} \neq \tau_{efetiva} \):

\[ \epsilon = \tau_{efetiva} - \sum p_{tributo} \]

\[ p_{maior} += \epsilon \]
