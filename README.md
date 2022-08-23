# Surfs Up: Module 9 Challenge

## Overview of Project

### Background and Purpose

You have come up with an idea for a new venture - a surf and shake shop, serving surf boards and ice cream in Hawaii. You have some savings you are willing to invest, but will need some real investor backing to get this off the ground. After putting together a strong business plan, you reach out to an investor, W. Avy, who is famous for his love of surfing. He's extremely serious about weather analysis, as he invested in a surf shop early in his career and that early venture was rained out of existence. W. Avy knows you've been learning how to properly analyze data and asks if you can run some analytics on a weather dataset he has from the very island where you'd like to open your shop - the beautiful Oahu. He also wants temperature data for the months of June and December in order to determine if the surf and ice cream shop business is sustainable year-round.

### Resources

- Data Sources: hawaii.sqlite
- Software: Anaconda 4.13, Jupyter Notebook, Matplotlib 3.5.1, Python 3.7.13, Visual Studio Code 1.68.1

## Results

### Three Key Differences

+ The temperatures in June on Oahu are pretty close to ideal for a surf and ice cream shop, with a max temp of 85°F and an average temp of 75°F. The max temp for December is only slightly lower at 83°F and the average temp is a little lower as well at 71°F.

+ The biggest difference between June and December is the min temp - December's min temp is about 8°F lower at 56°F, compared to June's min temp of 64°F. At 56°F, those interested in surfing may just need to wear a wetsuit to stay warm.

+ The standard deviations for both months are also a little different at 3.26 for June temperatures and 3.75 for December temperatures. This means that December has a little more variation in temperatures than June.

*Figure 1: Summary Statistics for June Temps*

![June_Temps_Summary](https://user-images.githubusercontent.com/106830513/186251252-f26bb5e5-adbb-4c99-bb0e-8c67be75cca0.png)

*Figure 2: Summary Statistics for December Temps*

![Dec_Temps_Summary](https://user-images.githubusercontent.com/106830513/186251196-dcabb72d-0857-4cb6-bf8a-c33b54eae78c.png)

## Summary

### High-Level Summary
Despite the key differences highlighted above, the temperatures for June and December do not showcase any concern for opening up a surf and ice cream shop. They both have highs in the 80s with average temps in the 70s. When temps drop lower than that, surfers may opt to wear a wetsuit while surfing to maintain warmth, which should not be a deterrent. Most wear wetsuits anyway to help prevent chafing from the board while paddling and also for protection from the sun.

### Additional Queries

Since W. Avy's first venture was "rained out," I created two queries to look at rainfall specifically for the months of June and December.

*Figure 3: Summary Statistics for June Rainfall*

![June_Rain_Summary](https://user-images.githubusercontent.com/106830513/186251227-abcd5dc8-8a5e-451b-8e42-fb6e6d1efc31.png)

*Figure 4: Summary Statistics for December Rainfall*

![Dec_Rain_Summary](https://user-images.githubusercontent.com/106830513/186251150-82488d55-2f79-4641-8743-b704eef29e5a.png)

The average amount of precipitation for December is 0.27 with a max precipitation amount of 6.42. June has an average precipitation of 0.14 and a max precipitation of 4.43. Both months have days without any precipitation, hence why the min for both is 0. Based on this data, it appears that there are the rare days within both months with a decent amount of rainfall, but most days are either dry or have very little precipitation. Considering all of the factors discussed, a surf and ice cream shop in Oahu seems to have a very good chance at success.
