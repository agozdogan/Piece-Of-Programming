/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [DocumentId],
      Count(Cluster) as KMeans
  FROM [SmallWordsEducation].[dbo].[KMeansResult] 
  WHERE DocumentId = 0 
  GROUP BY DocumentId, Cluster


  SELECT [DocumentId],
      Count(Cluster) as KMeansWithPMI
  FROM [SmallWordsEducation].[dbo].[KMeansPMIResult] 
  WHERE DocumentId = 0 
  GROUP BY DocumentId, Cluster