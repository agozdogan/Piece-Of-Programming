import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np



df  = pd.DataFrame({'x': [39.472778,
32.506993,
27.863137,
55.726274,
74.301699,
78.945555,
18.575425,
48.760490,
23.219281,
23.219281,
9.287712,
39.472778,
27.863137,
25.541209,
30.185065,
30.185065,
44.116634,
11.609640,
23.219281,
39.472778,
3.863137,
4.828921,
6.116634,
21.150850,
7.726274,
2.897353,
3.863137,
10.575425,
20.975797,
1.287712,
13.219281,
25.541209,
5.287712,
11.609640,
4.643856,
16.253497,
6.965784,
11.609640,
32.506993,
15.863137,
3.863137,
4.506993,
18.506993,
7.082418,
2.575425,
6.438562,
13.219281,
17.162015,
0.000000,
2.643856,
9.534453,
15.863137,
13.348234,
20.975797,
20.975797,
9.534453,
17.162015,
27.863137,
19.828921,
3.863137,
9.013987,
31.726274,
7.082418,
9.013987,
4.506993,
27.760490,
20.975797,
1.287712,
5.287712,
32.417140,
17.185065,
7.627562,
36.230921,
15.255125,
3.813781,
22.882687,
55.726274,
25.116634,
4.506993,
9.013987,
43.623627,
13.520980,
8.692059,
5.150850,
21.150850,
7.627562,
0.000000,
14.541209,
34.370130,
21.150850,
10.575425,
58.164836,
18.506993,
7.931569,
21.150850,
74.301699,
21.150850,
4.506993,
7.726274,
10.623627,
12.233268,
7.726274,
6.438562,
18.506993,
19.068906,
1.287712,
17.185065,
47.589411,
19.828921,
37.013987,
63.452549,
37.013987,
26.438562,
37.013987,
78.945555,
31.726274,
7.082418,
7.082418,
13.520980,
50.233268,
5.472778,
8.048202,
17.185065,
28.603359,
2.253497,
23.794706,
32.417140,
26.438562,
32.417140,
55.299827,
32.417140,
19.068906,
38.137812,
18.575425,
11.897353,
2.575425,
9.013987,
8.692059,
31.726274,
5.472778,
4.185065,
23.794706,
3.813781,
0.000000,
6.609640,
43.603359,
14.541209,
2.906891,
49.417140,
23.255125,
20.348234,
23.255125,
48.760490,
15.863137,
6.438562,
4.506993,
5.150850,
26.438562,
8.048202,
4.185065,
22.472778,
9.534453,
0.321928,
6.609640,
18.575425,
19.828921,
20.897353,
41.794706,
18.575425,
20.897353,
25.541209,
23.219281,
10.575425,
3.219281,
6.760490,
5.150850,
18.506993,
4.185065,
5.794706,
5.472778,
1.906891,
0.000000,
3.965784,
11.627562,
11.897353,
0.000000,
37.789578,
5.813781,
11.627562,
29.068906
],
        'y': [
23.219281,
14.541209,
2.897353,
3.541209,
1.287712,
13.219281,
4.828921,
0.643856,
1.609640,
1.321928,
4.185065,
25.116634,
31.292830,
9.253497,
37.551396,
6.258566,
37.551396,
37.551396,
43.809962,
9.287712,
5.287712,
0.000000,
1.287712,
0.000000,
5.287712,
2.253497,
0.000000,
0.321928,
0.000000,
24.789578,
15.863137,
1.287712,
6.609640,
3.219281,
0.321928,
1.287712,
5.150850,
5.472778,
39.472778,
13.219281,
0.643856,
1.287712,
3.541209,
17.185065,
5.794706,
1.609640,
1.609640,
3.965784,
36.230921,
3.863137,
30.185065,
17.185065,
27.863137,
23.219281,
20.897353,
34.828921,
39.472778,
27.863137,
14.541209,
1.609640,
5.472778,
4.185065,
23.794706,
5.472778,
4.828921,
2.575425,
5.287712,
19.068906,
1.287712,
17.185065,
14.541209,
9.534453,
28.603359,
15.255125,
3.813781,
17.162015,
25.541209,
5.287712,
3.863137,
4.185065,
5.150850,
19.828921,
6.438562,
3.541209,
4.828921,
11.897353,
13.348234,
1.609640,
17.185065,
20.975797,
34.828921,
53.404346,
9.287712,
13.931569,
44.116634,
30.185065,
6.609640,
2.253497,
1.287712,
1.287712,
18.506993,
5.472778,
0.321928,
2.897353,
0.000000,
22.882687,
3.219281,
15.863137,
9.534453,
19.828921,
15.863137,
18.506993,
10.575425,
31.726274,
30.185065,
2.643856,
3.541209,
6.116634,
7.082418,
31.726274,
9.335915,
5.472778,
5.794706,
17.185065,
3.813781,
0.321928,
13.219281,
28.603359,
30.404346,
15.863137,
18.775698,
12.517132,
62.585660,
44.116634,
9.253497,
3.541209,
2.575425,
2.253497,
18.506993,
5.472778,
2.575425,
2.575425,
2.643856,
22.882687,
1.287712,
11.897353,
15.255125,
5.287712,
18.506993,
18.775698,
13.931569,
27.863137,
11.609640,
3.965784,
1.609640,
0.643856,
0.965784,
13.219281,
3.219281,
2.253497,
2.897353,
5.287712,
22.882687,
5.150850,
19.828921,
3.813781,
7.931569,
10.575425,
12.517132,
13.931569,
50.233268,
23.219281,
6.609640,
2.897353,
3.863137,
2.575425,
18.506993,
6.438562,
2.575425,
3.541209,
13.219281,
26.696468,
5.472778,
22.472778,
17.162015,
25.116634,
31.726274,
62.585660,
27.863137,
50.233268]
       })

np.random.seed(200)
k = 2
# centroids[i] = [x, y]
centroids = {
    i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}
    
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()


def assignment(df, centroids):
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (float(df['x'][0]) - centroids[i][0]) ** 2
                + (float(df['y'][0]) - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

df = assignment(df, centroids)
print(df.head())

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()
