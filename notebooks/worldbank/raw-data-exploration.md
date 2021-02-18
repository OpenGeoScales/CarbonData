-   [Get data](#get-data)
-   [Total GHG emissions](#total-ghg-emissions)
    -   [Plot](#plot)
-   [References](#references)

In this notebook wi will explore ghg emissions data published from world
bank.

# Get data

Let’s identify datasets related to ghg emissions

``` r
library(WDI)
new_wdi_cache <- WDIcache() 
datasets = WDIsearch("*emissions.", cache = new_wdi_cache)
print(head(datasets))
```

    ##      indicator       
    ## [1,] "EE.BOD.CGLS.ZS"
    ## [2,] "EE.BOD.CHEM.ZS"
    ## [3,] "EE.BOD.FOOD.ZS"
    ## [4,] "EE.BOD.MTAL.ZS"
    ## [5,] "EE.BOD.OTHR.ZS"
    ## [6,] "EE.BOD.PAPR.ZS"
    ##      name                                                                 
    ## [1,] "Water pollution, clay and glass industry (% of total BOD emissions)"
    ## [2,] "Water pollution, chemical industry (% of total BOD emissions)"      
    ## [3,] "Water pollution, food industry (% of total BOD emissions)"          
    ## [4,] "Water pollution, metal industry (% of total BOD emissions)"         
    ## [5,] "Water pollution, other industry (% of total BOD emissions)"         
    ## [6,] "Water pollution, paper and pulp industry (% of total BOD emissions)"

# Total GHG emissions

``` r
data = WDI(indicator=c("wb_total_ghg_emissions" = "EN.ATM.GHGT.KT.CE"))

print(head(datasets))
```

    ##      indicator       
    ## [1,] "EE.BOD.CGLS.ZS"
    ## [2,] "EE.BOD.CHEM.ZS"
    ## [3,] "EE.BOD.FOOD.ZS"
    ## [4,] "EE.BOD.MTAL.ZS"
    ## [5,] "EE.BOD.OTHR.ZS"
    ## [6,] "EE.BOD.PAPR.ZS"
    ##      name                                                                 
    ## [1,] "Water pollution, clay and glass industry (% of total BOD emissions)"
    ## [2,] "Water pollution, chemical industry (% of total BOD emissions)"      
    ## [3,] "Water pollution, food industry (% of total BOD emissions)"          
    ## [4,] "Water pollution, metal industry (% of total BOD emissions)"         
    ## [5,] "Water pollution, other industry (% of total BOD emissions)"         
    ## [6,] "Water pollution, paper and pulp industry (% of total BOD emissions)"

## Plot

``` r
library(dplyr)
```

    ## 
    ## Attaching package: 'dplyr'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

``` r
emission_FR <- data %>% filter(iso2c == "FR")
emission_USA <- data %>% filter(iso2c == "US")

library(plotly)
```

    ## Loading required package: ggplot2

    ## 
    ## Attaching package: 'plotly'

    ## The following object is masked from 'package:ggplot2':
    ## 
    ##     last_plot

    ## The following object is masked from 'package:stats':
    ## 
    ##     filter

    ## The following object is masked from 'package:graphics':
    ## 
    ##     layout

``` r
fig <- plot_ly(emission_FR, x = ~year, y = ~wb_total_ghg_emissions, 
               type = 'scatter', mode = 'lines')

fig
```

<div id="htmlwidget-f54713266c324179b277" style="width:672px;height:480px;" class="plotly html-widget"></div>
<script type="application/json" data-for="htmlwidget-f54713266c324179b277">{"x":{"visdat":{"3e3829454552":["function () ","plotlyVisDat"]},"cur_data":"3e3829454552","attrs":{"3e3829454552":{"x":{},"y":{},"mode":"lines","alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"margin":{"b":40,"l":60,"t":25,"r":10},"xaxis":{"domain":[0,1],"automargin":true,"title":"year"},"yaxis":{"domain":[0,1],"automargin":true,"title":"wb_total_ghg_emissions"},"hovermode":"closest","showlegend":false},"source":"A","config":{"showSendToCloud":false},"data":[{"x":[2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,1990,1989,1988,1987,1986,1985,1984,1983,1982,1981,1980,1979,1978,1977,1976,1975,1974,1973,1972,1971,1970],"y":[499146.634492193,502656.654982811,532133.040360555,527525.776542167,544424.0617,540947.1359,547361.3761,557130.1263,560648.8432,564607.176,557850.1275,565204.3298,559922.199,563699.027,577851.541,565220.99,572529.08,543013.14,538140.6,541094.38,564014.19,580971.95,554685.28,547917.63,533912.04,547516.39,549474.89,561940.72,575218.36,584373.15,597074.4,621534.31,675156.85,697434.69,687571.95,667440.965,679365.4,634882.235,674903,691091.495,650356.94,629907.505,614501.57],"mode":"lines","type":"scatter","marker":{"color":"rgba(31,119,180,1)","line":{"color":"rgba(31,119,180,1)"}},"error_y":{"color":"rgba(31,119,180,1)"},"error_x":{"color":"rgba(31,119,180,1)"},"line":{"color":"rgba(31,119,180,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.2,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>

# References

-   rendering
    [github_document](https://rmarkdown.rstudio.com/github_document_format.html)
