# News Cluster

##### This repository is a clusterer using news headlines

The clustering algorithms used here are MiniBatchKmeans, Agglomerative clustering, Affinity Propogation, Birch clustering, DBSCAN and couple of other algorithms.

#### Execute the IronPythonNoteBook for the best experience

Execute it using Jupiter Notebook or Google Colabs.

Every other python file except the ones named "newscluster" are the starting versions of it. Although "main.py" does result in generation of png files in "results" folder, it has lesser algorithms implemented in it.

### Information

-   Used the Elbow Method to find the number of clusters and found the optimal number of clusters to be 12. - [ref](https://www.geeksforgeeks.org/elbow-method-for-optimal-value-of-k-in-kmeans/)

-   ###### News Sources

         https://timesofindia.indiatimes.com/
         https://www.thehindu.com/
         https://www.bbc.com/news
         https://www.theguardian.co.uk/
         https://www.hindustantimes.com/
         https://indianexpress.com/
         https://www.dailypioneer.com
         https://www.deccanherald.com/
         https://www.telegraphindia.com/
         https://www.dnaindia.com/
         https://www.deccanchronicle.com/
         https://www.asianage.com/
         https://economictimes.indiatimes.com/
         https://www.tribuneindia.com/

-   The news clustering is based on [newspaper3k](https://pypi.org/project/newspaper3k/) module.
    The module does not make use of RSS feeds for its sources.

Affinity Propogation:

![Affinity Propogation](./data/Aff.PNG)

Agglomerative Clustering:

![Agglomerative Clustering](./data/Agg.PNG)

Birch Clustering:

![Birch Clustering](./data/Birch.PNG)

DBSCAN:

![DBSCAN](./data/DBSCAN.PNG)

KMeans:

![KMeans](./data/KMeans.PNG)

MiniBatchKMeans:
![MiniBatchKMeans](./data/MiniKm.PNG)

Spectral Clustering:
![Spectral Clustering](./data/Spec.PNG)
