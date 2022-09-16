# ОПТИМИЗАЦИЯ ГИПЕРПАРАМЕТРОВ МОДЕЛИ


## Оглавление  
[1. Описание задания](#описание-задания)  
[2. Какую задачу решаем?](#какую-задачу-решаем)  
[3. Краткая информация о данных](#краткая-информация-о-данных)  
[4. Результат](#Результат)    
[5. Выводы](#Выводы) 

### Описание задания    
Практическое задание, направленное на практику оптимизации гиперпараметров моделей классификации.

:arrow_up:[к оглавлению](#оглавление)


### Какую задачу решаем?    
Необходимо предсказать биологический ответ молекул (столбец 'Activity') по их химическому составу (столбцы D1-D1776).  

### Цель
Максимизация метрики f1.


**Что практикуем** 
Использование базовых и продвинутых методов оптимизации гиперпараметров модели.

**Основные составляющие работы**  
* создание моделей логистической регрессии и случайного леса
* подготовка оптимизаторов 
* использование оптимизаторов
* расчет целевой метрики
* анализ полученных результатов

### Краткая информация о данных
Практика основана на соревновании [Kaggle: Predicting a Biological Response](https://www.kaggle.com/c/bioresponse) (Прогнозирование биологического ответа).
Данные представлены в формате CSV.  Каждая строка представляет молекулу.  
Первый столбец Activity содержит экспериментальные данные, описывающие фактический биологический ответ [0, 1];  
Остальные столбцы D1-D1776 представляют собой молекулярные дескрипторы — это вычисляемые свойства, которые могут фиксировать некоторые характеристики молекулы, например размер, форму или состав элементов.  
Предварительная обработка не требуется, данные уже закодированы и нормализованы.
  
:arrow_up:[к оглавлению](#Оглавление)


### Результаты:  
Оптимизация не показала прироста метрики относительно моделей по умолчанию. 

:arrow_up:[к оглавлению](#Оглавление)


### Выводы:  
Максимальное значение метрики (0.80) достигается во всех моделях случайного леса, за исключением оптимизированного Optuna. Optuna показал результат немного ниже (0.79).  
Логистическая регрессия предсказывала класс с точностью несколько хуже (f1 = 0.78), при этом Optuna также показала результат ниже остальных оптимизаторов (0.77).  
Минимальное время оптимизации было у RandomizeSearch для случайного леса (чуть менеьше минуты), максимальное (более 20 минут) у GridSearch.  
Модели случайного леса были более склонны к переобучению, показывая более высокие значения метрики на обучающей выборке.

:arrow_up:[к оглавлению](#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами