# Entrega 3: Análisis temporal de las disposiciones del BOE

En esta entrega analizamos nuestros datos teniendo en cuenta la componente temporal. Además, usamos los modelos ARIMAX, SARIMAX, modelos profundos, GARCH y ARCH para contrastar nuestra hipótesis:

``` Entre 1995 y 2024, la proporción de titulares del BOE relacionados con tecnología en universidades públicas de la Comunidad de Madrid aumenta moderadamente (≈ +1.1% anual), mientras que los relativos a empleo muestran una tendencia variable con disminución general (≈ -2.3% anual), lo que sugiere un cambio gradual de foco institucional desde temas laborales hacia la innovación tecnológica. ``` 
## 1. Visualizaciones

## 2. ARIMAX y SARIMAX

## 3. GARCH y ARCH
En esta sección analizamos la volatilidad de la influencia de tecnología y empleo en las universidades públicas de Madrid mediante GARCH y ARCH.

### 3.1 Tecnología
En primer lugar, llevamos a cabo el test ADF, con los valores de 1%, 5% y 10% vemos que nuestro ADF statistic (-15.78) es mucho menor que el nivel 1% (-3.43), nivel 5% (-2.86) y el nivel 10% (-2.56), lo que nos confirma que la serie es estacionaria con un nivel de confianza altísimo, perfecto para aplicar GARCH.

**Retornos**
Después calculamos los retornos
 ![Retornos tec](./imgs/retornos_tec.png)

Y representamos el PACF, Partial Autocorrelation Function (Función de Autocorrelación Parcial), que es una herramienta que nos ayuda a entender cómo una serie temporal se relaciona consigo misma en distintos periodos de tiempo. 

 ![PACF tec](./imgs/PACF_tec.png)
 
## Conclusiones
